"""
test_text_to_sql.py — Test standalone del canale text-to-SQL.

Non richiede nessuna modifica a main.py: e' un modulo eseguibile a se'
stante che chiama esattamente le stesse funzioni che hybrid_search.py
usa in produzione, cosi' puoi vedere passo-passo cosa succede prima di
integrarlo nella CLI principale.

Uso:
    docker compose run --rm app python -m app.test_text_to_sql "scarpe sotto i 50 euro"
    docker compose run --rm app python -m app.test_text_to_sql "scarpe comode da camminare"
"""

import sys

from app.text_to_sql import (
    contiene_vincolo_strutturato,
    genera_sql,
    valida_query,
    esegui_query,
    _forza_limit,
)


def main():
    if len(sys.argv) < 2:
        print('Uso: python -m app.test_text_to_sql "la tua domanda"')
        sys.exit(1)

    domanda = " ".join(sys.argv[1:])
    print(f'\nDomanda: "{domanda}"\n')

    # Passaggio 1
    ha_vincolo = contiene_vincolo_strutturato(domanda)
    print(f"1. Vincolo strutturato rilevato: {ha_vincolo}")
    if not ha_vincolo:
        print("   -> nessun filtro verra' applicato, il retrieval procede come sempre.\n")
        return

    # Passaggi 2-3: generazione
    sql = genera_sql(domanda)
    if not sql:
        print("2. Il modello non ha prodotto SQL utilizzabile. Nessun filtro applicato.\n")
        return
    sql = _forza_limit(sql)
    print(f"2. SQL generato dal modello (LIMIT forzato se assente):\n   {sql}\n")

    # Passaggio 4: validazione
    valida = valida_query(sql)
    print(f"3. Query validata dal guardrail: {valida}")
    if not valida:
        print("   -> query rifiutata dai controlli di sicurezza. Nessun filtro applicato.\n")
        return

    # Passaggio 5: esecuzione
    try:
        righe = esegui_query(sql)
    except Exception as e:
        print(f"4. Errore durante l'esecuzione su MySQL: {e}\n")
        return

    nomi = sorted({r["nome"] for r in righe if "nome" in r})
    print(f"4. Prodotti che rispettano il vincolo ({len(nomi)}):")
    if nomi:
        for nome in nomi:
            print(f"   - {nome}")
    else:
        print("   (nessuno — il filtro azzererebbe i risultati)")
    print()


if __name__ == "__main__":
    main()
