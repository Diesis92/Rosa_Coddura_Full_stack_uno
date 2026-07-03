"""
text_to_sql.py — Terzo canale di retrieval: filtro SQL robusto e safe.
FIX: normalizzazione categorie + fallback intelligente + no blocchi hard.
"""

import re
import sqlparse
from app.db_mysql import get_connection
from app.ollama_client import chat


# ─────────────────────────────────────────────
# 1. SCHEMA
# ─────────────────────────────────────────────

SCHEMA_DESCRIZIONE = """
tabella: prodotti
colonne:
  id             INT
  nome           VARCHAR
  categoria      VARCHAR
  prezzo         DECIMAL
  disponibile    TINYINT(1)
"""


# ─────────────────────────────────────────────
# 2. NORMALIZZAZIONE DOMANDA (FIX CRITICO)
# ─────────────────────────────────────────────

CATEGORIA_MAP = {
    "scarpe": "calzature",
    "scarpa": "calzature",
    "shoes": "calzature",
    "trekking shoes": "calzature"
}


def normalizza_domanda(domanda: str) -> str:
    d = domanda.lower()
    for k, v in CATEGORIA_MAP.items():
        d = d.replace(k, v)
    return d


# ─────────────────────────────────────────────
# 3. SYSTEM PROMPT (FIXATO)
# ─────────────────────────────────────────────

SYSTEM_PROMPT = f"""
Sei un generatore di query SQL.

REGOLE FONDAMENTALI:
- Usa SOLO queste categorie:
  calzature, abbigliamento, zaini, campeggio, sicurezza, idratazione, accessori

- NON inventare categorie (es: NON usare "scarpe")

- Se l'utente dice "scarpe" → usa "calzature"

- Se non sei sicuro, NON filtrare per categoria

Schema:
{SCHEMA_DESCRIZIONE}

Regole:
- SOLO SELECT
- SOLO tabella prodotti
- sempre SELECT nome
- aggiungi LIMIT 50 se manca
"""


# ─────────────────────────────────────────────
# 4. VINCOLO STRUTTURATO
# ─────────────────────────────────────────────

PATTERN_VINCOLO = re.compile(
    r"\b(sotto|meno di|inferiore|tra|fra|piu di|almeno|massimo|minimo)\b.{0,20}\d+"
    r"|\b\d+\s*(euro|eur|€)\b",
    re.IGNORECASE,
)


def contiene_vincolo_strutturato(domanda: str) -> bool:
    return bool(PATTERN_VINCOLO.search(domanda))


# ─────────────────────────────────────────────
# 5. GENERAZIONE SQL
# ─────────────────────────────────────────────

def genera_sql(domanda: str) -> str | None:
    domanda = normalizza_domanda(domanda)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Domanda: {domanda}\nSQL:"},
    ]

    risposta = chat(messages, stream=False)

    if not risposta:
        return None

    # FIX generator / strip / JSON sporco
    if hasattr(risposta, "__iter__") and not isinstance(risposta, str):
        risposta = "".join(list(risposta))

    sql = str(risposta).strip()

    sql = re.sub(r"^```sql|```$", "", sql, flags=re.IGNORECASE).strip()
    sql = sql.rstrip(";").strip()

    return sql or None


# ─────────────────────────────────────────────
# 6. VALIDAZIONE SICURA
# ─────────────────────────────────────────────

TABELLE_AMMESSE = {"prodotti"}

PAROLE_VIETATE = (
    "DROP", "DELETE", "UPDATE", "INSERT",
    "ALTER", "TRUNCATE", "GRANT"
)


def valida_query(sql: str) -> bool:
    if not sql:
        return False

    try:
        statements = sqlparse.parse(sql)
    except Exception:
        return False

    if len(statements) != 1:
        return False

    parsed = statements[0]

    if parsed.get_type() != "SELECT":
        return False

    sql_upper = sql.upper()
    if any(p in sql_upper for p in PAROLE_VIETATE):
        return False

    if "prodotti" not in sql_lower(sql):
        return False

    return True


def sql_lower(sql: str) -> str:
    return sql.lower()


# ─────────────────────────────────────────────
# 7. LIMIT SAFETY
# ─────────────────────────────────────────────

def _forza_limit(sql: str, limite: int = 50) -> str:
    if re.search(r"\bLIMIT\b", sql, re.IGNORECASE):
        return sql
    return f"{sql} LIMIT {limite}"


# ─────────────────────────────────────────────
# 8. DB EXECUTION
# ─────────────────────────────────────────────

def esegui_query(sql: str) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 9. ENTRYPOINT (FIX IMPORTANTE)
# ─────────────────────────────────────────────

def filtra_per_vincoli(domanda: str) -> set[str] | None:
    """
    FIX PRINCIPALE:
    - None = nessun filtro
    - set() = filtro valido ma zero risultati
    """

    if not contiene_vincolo_strutturato(domanda):
        return None

    sql = genera_sql(domanda)

    if not sql:
        return None

    sql = _forza_limit(sql)

    if not valida_query(sql):
        return None

    try:
        righe = esegui_query(sql)
    except Exception:
        return None

    # ⚠️ NON bloccare pipeline se vuoto
    return {r["nome"] for r in righe if "nome" in r}