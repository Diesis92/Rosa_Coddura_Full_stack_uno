"""
text_to_sql.py — Terzo canale di retrieval: filtro esatto via SQL generato da LLM.

IMPORTANTE (vedi deck "Text-to-SQL — Terzo Canale"): questo modulo NON compete
nel ranking RRF. Genera una query SQL sullo schema reale di `prodotti`, la
valida, la esegue, e restituisce l'insieme dei NOMI prodotto che rispettano
il vincolo. hybrid_search.py usa questo insieme come FILTRO HARD applicato
PRIMA della fusione RRF tra dense e BM25 — non come terzo punteggio da fondere.

Schema reale (vedi docker/mysql/init/01_schema.sql):
    prodotti(id, nome, descrizione, categoria, prezzo, disponibile, tag, updated_at)
"""

import re
import sqlparse
from app.db_mysql import get_connection
from app.ollama_client import chat


# ── Schema dichiarato al modello (solo le colonne utili al filtro) ──────

SCHEMA_DESCRIZIONE = """
tabella: prodotti
colonne:
  id             INT
  nome           VARCHAR
  categoria      VARCHAR
  prezzo         DECIMAL
  disponibile    TINYINT(1)   -- 1 = disponibile, 0 = non disponibile
"""

SYSTEM_PROMPT = f"""Sei un generatore di query SQL per il catalogo di un negozio online.

Usa SOLO questo schema. Non inventare colonne o tabelle:
{SCHEMA_DESCRIZIONE}

Regole obbligatorie:
- Genera SOLO una istruzione SELECT, mai altro.
- Seleziona sempre almeno la colonna nome.
- Non inventare nomi di colonne o tabelle diversi da quelli sopra.
- Se la domanda non specifica un limite, aggiungi LIMIT 50.
- Rispondi SOLO con la query SQL. Niente markdown, niente spiegazioni, niente punto e virgola finale.

Esempio 1:
Domanda: prodotti sotto i 30 euro
SQL: SELECT nome FROM prodotti WHERE prezzo < 30 AND disponibile = 1 LIMIT 50

Esempio 2:
Domanda: scarpe disponibili tra 20 e 60 euro
SQL: SELECT nome FROM prodotti WHERE categoria = 'scarpe' AND prezzo BETWEEN 20 AND 60 AND disponibile = 1 LIMIT 50

Esempio 3:
Domanda: prodotti della categoria zaini
SQL: SELECT nome FROM prodotti WHERE categoria = 'zaini' AND disponibile = 1 LIMIT 50
"""


# ── Passaggio 1: rilevamento del vincolo strutturato ─────────────────────

PATTERN_VINCOLO = re.compile(
    r"\b(sotto|meno di|inferiore|tra|fra|superiore|pi[uù] di|almeno|massimo|minimo)\b.{0,15}\b\d+\b"
    r"|\b\d+\s*(euro|eur|€)\b"
    r"|\bdisponibil[ei]\b",
    re.IGNORECASE,
)


def contiene_vincolo_strutturato(domanda: str) -> bool:
    """
    Euristica leggera: True se la domanda sembra contenere un vincolo
    numerico, di prezzo o di disponibilita' da risolvere con query esatta.
    Un falso negativo qui significa solo "nessun filtro extra": il
    retrieval semantico/lessicale normale procede comunque.
    """
    return bool(PATTERN_VINCOLO.search(domanda))


# ── Passaggi 2+3: schema-aware prompting e generazione ───────────────────

def genera_sql(domanda: str) -> str | None:
    """
    Chiede al modello (Ollama, via ollama_client.chat non-stream) di
    tradurre la domanda in una SELECT sullo schema di prodotti.
    Restituisce None se il modello non produce nulla di utilizzabile.
    """
    messaggi = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Domanda: {domanda}\nSQL:"},
    ]
    risposta = chat(messaggi, stream=False)
    if not risposta:
        return None

    sql = risposta.strip()
    # Il modello a volte avvolge la risposta in ```sql ... ``` nonostante la regola
    sql = re.sub(r"^```sql|```$", "", sql, flags=re.IGNORECASE).strip()
    sql = sql.rstrip(";").strip()
    return sql or None


# ── Passaggio 4: validazione obbligatoria (AST, non regex) ───────────────

TABELLE_AMMESSE = {"prodotti"}
PAROLE_VIETATE = ("DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE",
                   "GRANT", "EXEC", "EXECUTE", "--", ";")


def _tabelle_usate(parsed) -> set[str]:
    """Estrae i nomi di tabella che seguono FROM/JOIN nella query parsata."""
    tabelle = set()
    tokens = list(parsed.flatten())
    for i, tok in enumerate(tokens):
        if tok.ttype is sqlparse.tokens.Keyword and tok.value.upper() in ("FROM", "JOIN"):
            for nxt in tokens[i + 1:]:
                if nxt.is_whitespace:
                    continue
                if nxt.ttype is sqlparse.tokens.Name:
                    tabelle.add(nxt.value.lower())
                break
    return tabelle


def valida_query(sql: str) -> bool:
    """
    Guardrail obbligatorio prima di qualunque esecuzione:
    - una sola istruzione
    - solo SELECT
    - solo tabelle in whitelist
    - nessuna parola chiave pericolosa
    """
    if not sql:
        return False

    statements = sqlparse.parse(sql)
    if len(statements) != 1:
        return False

    parsed = statements[0]
    if parsed.get_type() != "SELECT":
        return False

    if not _tabelle_usate(parsed).issubset(TABELLE_AMMESSE):
        return False

    sql_upper = sql.upper()
    if any(parola in sql_upper for parola in PAROLE_VIETATE):
        return False

    return True


def _forza_limit(sql: str, limite: int = 50) -> str:
    if re.search(r"\bLIMIT\b", sql, re.IGNORECASE):
        return sql
    return f"{sql} LIMIT {limite}"


# ── Passaggio 5: esecuzione ───────────────────────────────────────────────
# Difesa in profondita' consigliata: creare un utente MySQL dedicato con
# permessi SELECT-only su `prodotti` per l'esecuzione di queste query,
# invece di riusare le credenziali applicative con permessi pieni.

def esegui_query(sql: str) -> list[dict]:
    """Esegue una query gia' validata e restituisce le righe come dict."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


# ── Punto di ingresso usato da hybrid_search.py ──────────────────────────

def filtra_per_vincoli(domanda: str) -> set[str] | None:
    """
    Se la domanda contiene un vincolo strutturato, genera+valida+esegue
    la query SQL e restituisce l'insieme dei NOMI prodotto conformi.

    Restituisce None se non c'e' alcun vincolo da applicare: in quel caso
    hybrid_search.py non deve filtrare nulla, il retrieval procede come sempre.

    Nota: None e' intenzionalmente diverso da un insieme vuoto. Un insieme
    vuoto significa "vincolo rilevato ma zero prodotti conformi" (filtro che
    azzera legittimamente i risultati); None significa "nessun filtro".
    """
    if not contiene_vincolo_strutturato(domanda):
        return None

    sql = genera_sql(domanda)
    if not sql:
        return None

    sql = _forza_limit(sql)

    if not valida_query(sql):
        # Query generata non sicura o malformata: meglio nessun filtro
        # che eseguire qualcosa di non validato.
        return None

    try:
        righe = esegui_query(sql)
    except Exception:
        return None

    return {r["nome"] for r in righe if "nome" in r}
