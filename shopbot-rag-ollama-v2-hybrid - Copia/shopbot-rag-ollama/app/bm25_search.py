"""
bm25_search.py — Retrieval sparso con BM25
Indicizza i prodotti con rank_bm25 (in memoria, ricostruito ad ogni avvio).
Complementa vector_store.py: BM25 trova match esatti (nomi propri, codici,
termini tecnici), il dense retrieval trova similarità semantica.

Non richiede nessuna infrastruttura aggiuntiva: gira in RAM, si ricostruisce
leggendo i prodotti da MySQL ogni volta che il processo CLI parte.
"""

from rank_bm25 import BM25Okapi

from app.db_mysql import get_prodotti_disponibili

# Cache in-process: evita di ricostruire l'indice ad ogni chiamata
# all'interno della stessa sessione di chat.
_bm25_index = None
_prodotti_cache = None


def _tokenizza(testo: str) -> list[str]:
    """
    Tokenizzazione minimale: minuscolo + split su spazi/punteggiatura.
    BM25 lavora su token esatti — niente stemming, niente normalizzazione
    avanzata. Volutamente semplice per restare didattico.
    """
    import re
    testo = testo.lower()
    # sostituisce tutto ciò che non è lettera/numero con uno spazio
    testo = re.sub(r"[^a-z0-9àèéìòù]+", " ", testo)
    return testo.split()


def _costruisci_indice():
    """
    Costruisce l'indice BM25 in memoria leggendo i prodotti da MySQL.
    Stesso testo descrittivo usato per gli embedding in vector_store.py,
    così il confronto fra i due retrieval è ad armi pari.
    """
    global _bm25_index, _prodotti_cache

    prodotti = get_prodotti_disponibili()
    _prodotti_cache = prodotti

    corpus_tokenizzato = []
    for p in prodotti:
        testo = f"{p['nome']}. {p['descrizione']} Tag: {p['tag']}."
        corpus_tokenizzato.append(_tokenizza(testo))

    _bm25_index = BM25Okapi(corpus_tokenizzato)


def reset_index():
    """Forza la ricostruzione dell'indice al prossimo utilizzo."""
    global _bm25_index, _prodotti_cache
    _bm25_index = None
    _prodotti_cache = None


def cerca_prodotti_bm25(domanda: str, top_k: int = 10) -> list[dict]:
    """
    Cerca i prodotti più rilevanti per BM25 (match lessicale, non semantico).

    Restituisce una lista di dict con: nome, categoria, prezzo, tag,
    documento, score (più alto = più rilevante), rank (1 = primo).

    A differenza di cerca_prodotti() in vector_store.py, qui lo score
    BM25 non ha un limite superiore fisso — dipende dal corpus.
    """
    global _bm25_index, _prodotti_cache

    if _bm25_index is None:
        _costruisci_indice()

    if not _prodotti_cache:
        return []

    query_tokens = _tokenizza(domanda)
    scores = _bm25_index.get_scores(query_tokens)

    # Abbina ogni prodotto al suo score e ordina per rilevanza decrescente
    risultati = list(zip(_prodotti_cache, scores))
    risultati.sort(key=lambda x: x[1], reverse=True)

    trovati = []
    for rank, (p, score) in enumerate(risultati[:top_k], start=1):
        # Scarta risultati a score 0: nessun termine della query è presente
        if score <= 0:
            continue
        testo = f"{p['nome']}. {p['descrizione']} Tag: {p['tag']}."
        trovati.append({
            "nome":      p["nome"],
            "categoria": p["categoria"],
            "prezzo":    float(p["prezzo"]),
            "tag":       p["tag"],
            "documento": testo,
            "score":     round(float(score), 4),
            "rank":      rank,
        })

    return trovati
