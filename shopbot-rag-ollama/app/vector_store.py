"""
vector_store.py — ChromaDB + ricerca semantica
Gestisce: indicizzazione prodotti, ricerca per similarità coseno.
Usa le variabili COLLECTION_NAME, MAX_DISTANCE, TOP_K dal config.
"""

import chromadb
from chromadb.config import Settings

from app import config
from app.ollama_client import get_embedding


def _get_client() -> chromadb.PersistentClient:
    return chromadb.PersistentClient(
        path=config.CHROMA_PATH,
        settings=Settings(anonymized_telemetry=False),
    )


def _get_collection():
    """Restituisce la collection ChromaDB (la crea se non esiste)."""
    client = _get_client()
    return client.get_or_create_collection(
        name=config.COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def reset_collection():
    """Cancella e ricrea la collection. Usato da 'setup --reset'."""
    client = _get_client()
    try:
        client.delete_collection(config.COLLECTION_NAME)
        print(f"  ✓ Collection '{config.COLLECTION_NAME}' eliminata.")
    except Exception:
        pass  # non esisteva ancora


def indicizza_prodotti(prodotti: list[dict]) -> int:
    """
    Indicizza la lista di prodotti in ChromaDB.
    Per ogni prodotto genera l'embedding con Ollama e lo salva.
    Restituisce il numero di prodotti indicizzati.
    """
    collection = _get_collection()

    ids        = []
    embeddings = []
    documents  = []
    metadatas  = []

    n = len(prodotti)
    print(f"  Genero embedding per {n} prodotti...")

    for i, p in enumerate(prodotti):
        # Testo da embeddare: nome + descrizione + tag
        testo = (
            f"{p['nome']}. "
            f"{p['descrizione']} "
            f"Tag: {p['tag']}."
        )

        print(f"  [{i+1}/{n}] {p['nome']:<45}", end="\r")
        emb = get_embedding(testo)

        ids.append(str(p["id"]))
        embeddings.append(emb)
        documents.append(testo)
        metadatas.append({
            "nome":      p["nome"],
            "categoria": p["categoria"],
            "prezzo":    float(p["prezzo"]),
            "tag":       p["tag"],
        })

    print()  # newline dopo \r

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )
    return len(ids)


def cerca_prodotti(domanda: str, top_k: int | None = None) -> list[dict]:
    """
    Cerca i prodotti più simili alla domanda tramite similarità coseno.

    Filtra i risultati con distanza > MAX_DISTANCE (prodotti troppo lontani).
    Restituisce lista di dict con: nome, categoria, prezzo, tag, documento, distanza.
    """
    if top_k is None:
        top_k = config.TOP_K

    collection = _get_collection()
    n_total = collection.count()
    if n_total == 0:
        return []

    top_k = min(top_k, n_total)
    emb   = get_embedding(domanda)

    results = collection.query(
        query_embeddings=[emb],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    trovati = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        # Scarta risultati troppo lontani semanticamente
        if dist > config.MAX_DISTANCE:
            continue
        trovati.append({
            "nome":      meta["nome"],
            "categoria": meta["categoria"],
            "prezzo":    meta["prezzo"],
            "tag":       meta["tag"],
            "documento": doc,
            "distanza":  round(dist, 4),
        })

    return trovati


def get_stats() -> dict:
    """Restituisce statistiche sulla collection ChromaDB."""
    collection = _get_collection()
    return {
        "collection":             config.COLLECTION_NAME,
        "n_prodotti_indicizzati": collection.count(),
        "chroma_path":            config.CHROMA_PATH,
        "max_distance":           config.MAX_DISTANCE,
    }
