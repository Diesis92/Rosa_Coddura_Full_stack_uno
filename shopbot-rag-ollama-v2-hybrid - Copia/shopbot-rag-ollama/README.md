# ShopBot RAG con MySQL, ChromaDB e Ollama

Progetto didattico semplice per costruire un chatbot RAG su un catalogo prodotti.

Questa versione segue le slide, ma sostituisce OpenAI con Ollama:

- MySQL: database prodotti, fonte di verità.
- ChromaDB: indice vettoriale per cercare i prodotti più simili alla domanda.
- Ollama: modelli locali per embedding e risposta del chatbot.
- Python: codice del chatbot e pipeline RAG.

Il flusso è questo:

1. MySQL contiene la tabella `prodotti`.
2. Python legge i prodotti disponibili da MySQL.
3. Ollama crea gli embedding dei prodotti.
4. ChromaDB salva embedding e metadati.
5. Ogni domanda viene cercata in ChromaDB.
6. Il chatbot manda al LLM solo i prodotti trovati.
7. Ollama genera la risposta usando solo quel contesto.

## Requisiti

Per la classe consiglio Docker:

- Docker Desktop
- Almeno 8 GB di RAM disponibili
- Connessione internet per scaricare immagini Docker e modelli Ollama

Modelli usati di default:

- Chat: `llama3.2:3b`
- Embedding: `nomic-embed-text`

`llama3.2:3b` è leggero e adatto a molti portatili. Su macchine più potenti puoi provare modelli più grandi.

## Avvio con Docker

Dalla cartella del progetto:

```bash
docker compose up -d mysql ollama
```

Scarica i modelli Ollama:

```bash
docker compose exec ollama ollama pull llama3.2:3b
docker compose exec ollama ollama pull nomic-embed-text
```

Costruisci l'app Python:

```bash
docker compose build app
```

Indicizza i prodotti MySQL in ChromaDB:

```bash
docker compose run --rm app python -m app.main setup --reset
```

Avvia il chatbot:

```bash
docker compose run --rm app python -m app.main chat
```

Per uscire scrivi:

```text
esci
```

## Database MySQL

Il database viene creato automaticamente al primo avvio del container MySQL.

File SQL:

```text
docker/mysql/init/01_schema.sql
```

Contiene:

- `CREATE TABLE prodotti`
- 20 prodotti di esempio
- campo `disponibile`
- campo `updated_at`
- prezzo, categoria e tag

Credenziali Docker:

```text
host: localhost
porta: 3306
database: shopbot
utente: shopbot
password: shopbot
root password: root
```

Dentro Docker, l'app usa `MYSQL_HOST=mysql`.

## Variabili d'ambiente (docker-compose.yml)

| Variabile | Default | Descrizione |
|---|---|---|
| `OLLAMA_CHAT_MODEL` | `llama3.2:3b` | Modello per la risposta |
| `OLLAMA_EMBED_MODEL` | `nomic-embed-text` | Modello per gli embedding |
| `TOP_K` | `5` | Prodotti passati al LLM per query |
| `MAX_DISTANCE` | `1.2` | Soglia coseno: prodotti più lontani vengono scartati |
| `MAX_TURNS` | `8` | Turni di storia conversazione mantenuti |
| `COLLECTION_NAME` | `prodotti` | Nome collection ChromaDB |
| `USE_HYBRID` | `true` | Attiva hybrid search (dense + BM25 via RRF) |

## Hybrid Search — BM25 + Dense via RRF

Dalla v2 il chatbot usa retrieval ibrido: oltre alla ricerca semantica (ChromaDB),
interroga anche un indice BM25 lessicale costruito in memoria sugli stessi prodotti.
I due ranking vengono fusi con RRF (Reciprocal Rank Fusion).

Perché serve: il dense retrieval trova similarità di significato ("scarpe per non
bagnarmi i piedi" → trova scarpe impermeabili) ma a volte fatica sui nomi propri
esatti. BM25 fa il contrario: trova "Salomon X Ultra" alla perfezione ma non capisce
sinonimi o parafrasi. Insieme coprono più casi di uno dei due da soli.

File coinvolti:

```text
app/bm25_search.py     # indice BM25 in memoria, costruito da MySQL
app/hybrid_search.py   # fusione RRF tra dense e bm25
```

Comando per vedere il confronto affiancato:

```bash
docker compose run --rm app python -m app.main compare "Salomon X Ultra"
docker compose run --rm app python -m app.main compare "qualcosa per non bagnarmi i piedi"
```

Per disattivare hybrid search e tornare al solo dense retrieval, in
`docker-compose.yml` imposta `USE_HYBRID: "false"`.

## Comandi utili

Reindicizza i prodotti:

```bash
docker compose run --rm app python -m app.main setup --reset
```

Cerca prodotti senza chiamare il chatbot:

```bash
docker compose run --rm app python -m app.main search "scarpe impermeabili per camminare"
```

Mostra statistiche:

```bash
docker compose run --rm app python -m app.main stats
```

Entrare in MySQL:

```bash
docker compose exec mysql mysql -ushopbot -pshopbot shopbot
```

Query di prova:

```sql
SELECT id, nome, categoria, prezzo, disponibile
FROM prodotti
ORDER BY id;
```

Se modifichi `docker/mysql/init/01_schema.sql` dopo il primo avvio, MySQL non lo riesegue automaticamente perché i dati sono già nel volume Docker. Per ripartire da zero:

```bash
docker compose down -v
docker compose up -d mysql ollama
docker compose run --rm app python -m app.main setup --reset
```

## Struttura progetto

```text
shopbot-rag-ollama/
  app/
    __init__.py
    main.py            # CLI: setup, chat, search, compare, stats
    config.py          # configurazione da variabili ambiente
    db_mysql.py        # lettura prodotti da MySQL
    vector_store.py    # ChromaDB + ricerca semantica (dense)
    bm25_search.py      # indice BM25 in memoria (sparse)
    hybrid_search.py    # fusione RRF tra dense e bm25
    ollama_client.py   # API Ollama per chat ed embedding (usa requests)
    chatbot.py         # history + prompt RAG + hybrid search
  docker/
    mysql/init/
      01_schema.sql    # tabella prodotti + dati esempio
  scripts/
    export_docker_bundle.sh
    import_docker_bundle.sh
    install_models.sh
  docker-compose.yml
  Dockerfile
  requirements.txt
  README.md
```

## Come spiegarlo ai ragazzi

Il chatbot non manda tutto il catalogo al modello.

Esempio:

```text
Cliente: Hai scarpe impermeabili?
Python: crea embedding della domanda
ChromaDB: trova prodotti simili
Contesto: Salomon X Ultra 4 GTX, Columbia Redmond V2 WP
Ollama: risponde usando solo quei prodotti
```

Questo è il cuore del RAG:

- **Retrieve**: cerca i prodotti rilevanti.
- **Augment**: aggiunge i prodotti al prompt.
- **Generate**: genera la risposta.

## Avvio senza Docker

Si può fare, ma per la classe lo sconsiglio perché richiede installare MySQL, Ollama e Python localmente.

Se vuoi farlo:

1. Installa MySQL.
2. Crea database e utente `shopbot`.
3. Esegui `docker/mysql/init/01_schema.sql`.
4. Installa Ollama e scarica i modelli.
5. Crea un virtualenv Python e installa `requirements.txt`.

Poi:

```bash
python -m app.main setup --reset
python -m app.main chat
```

## Esportare per gli studenti

Metodo semplice: consegna la cartella e fai eseguire i comandi Docker.

Metodo offline, più pesante:

```bash
chmod +x scripts/*.sh
./scripts/export_docker_bundle.sh
```

Il bundle viene creato in `dist/` e include immagini Docker e modelli Ollama.

Sul computer dello studente:

```bash
chmod +x scripts/*.sh
./scripts/import_docker_bundle.sh
docker compose run --rm app python -m app.main chat
```

Nota: i modelli possono occupare diversi GB. In aula può essere più pratico prepararli prima o scaricarli una sola volta su rete veloce.
