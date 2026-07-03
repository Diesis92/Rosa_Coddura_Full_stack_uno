# Integrazione Text-to-SQL in ShopBot RAG

## File in questo pacchetto

```
app/text_to_sql.py       NUOVO — genera, valida ed esegue SQL sui vincoli strutturati
app/hybrid_search.py     AGGIORNATO — applica il filtro prima della fusione RRF
app/config.py            AGGIORNATO — aggiunto USE_TEXT_TO_SQL (default: true)
app/test_text_to_sql.py  NUOVO — CLI di test standalone, non tocca main.py
requirements.txt         AGGIORNATO — aggiunta sqlparse (parsing AST per la validazione)
```

## Installazione

1. Copia `app/text_to_sql.py` nella cartella `app/` del progetto (file nuovo).
2. Sovrascrivi `app/hybrid_search.py` e `app/config.py` con quelli qui dentro
   (sono le versioni originali + le modifiche per il canale text-to-SQL,
   nessun'altra logica è stata toccata).
3. Sovrascrivi `requirements.txt`.
4. Ricostruisci l'immagine Docker:

```bash
docker compose build app
docker compose run --rm app python -m app.main chat
```

## Come funziona l'integrazione

`cerca_prodotti_hybrid()` in `hybrid_search.py` ora, prima di fondere con RRF:

1. Chiama `filtra_per_vincoli(domanda)` da `text_to_sql.py`.
2. Se la domanda non ha un vincolo strutturato riconoscibile (prezzo,
   disponibilità, tra X e Y euro), la funzione ritorna `None` e non cambia
   nulla — comportamento identico a prima.
3. Se c'è un vincolo, genera una query SQL sullo schema reale di `prodotti`,
   la valida con `sqlparse` (solo SELECT, solo tabella `prodotti`, nessuna
   parola chiave pericolosa), la esegue, e ottiene l'insieme dei nomi
   prodotto conformi.
4. Quell'insieme filtra le liste dense e BM25 **prima** che RRF le fonda.

## Nota sullo schema

Il deck didattico "Text-to-SQL" usa per generalità un ipotetico campo
`quantita_disponibile`. Lo schema reale del progetto (`docker/mysql/init/01_schema.sql`)
ha invece un campo booleano `disponibile` (1/0). Il codice qui usa lo schema
reale — se in futuro aggiungi una colonna quantità, aggiorna
`SCHEMA_DESCRIZIONE` in `text_to_sql.py` e il prompt few-shot di conseguenza.

## Testare senza toccare main.py

`app/test_text_to_sql.py` è un modulo eseguibile a sé stante che chiama le
stesse funzioni usate in produzione da `hybrid_search.py`, passo per passo:

```bash
docker compose run --rm app python -m app.test_text_to_sql "scarpe sotto i 50 euro"
docker compose run --rm app python -m app.test_text_to_sql "scarpe comode da camminare"
```

Il primo mostra rilevamento vincolo → SQL generato → validazione → prodotti
conformi. Il secondo si ferma al passo 1 (nessun vincolo rilevato).

## Nota onesta su main.py

Non ho il contenuto completo e aggiornato di `main.py` in questa chat — solo
frammenti (imports, `cmd_setup`, l'inizio di `cmd_compare`). Copiare un nuovo
comando CLI `filter` dentro un file che non vedo per intero rischia di
introdurre un disallineamento con l'argparse esistente (nomi di variabili,
flag, dispatch). Per questo ho preferito il modulo standalone sopra, che
funziona da subito senza toccare nulla.

Se vuoi il comando integrato in `main.py` come gli altri (`setup`, `chat`,
`search`, `compare`, `stats`), carica `main.py` in un prossimo messaggio:
aggiungo `filter` con lo stesso pattern usato per `compare`, chirurgicamente.
