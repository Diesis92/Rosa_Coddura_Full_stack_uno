"""
hybrid_search.py — Fusione RRF tra dense e BM25, con filtro hard text-to-SQL.

formula:  score_rrf(prodotto) = somma di  1 / (k + rank)  su ogni sistema
k = 60 è la costante standard usata in letteratura (Cormack et al. 2009).

v3: prima della fusione, se la domanda contiene un vincolo strutturato
(prezzo, disponibilita', categoria), un modulo text-to-SQL lo risolve con
una query esatta e scarta dai due canali tutto cio' che non rispetta il
vincolo. Vedi text_to_sql.py e il deck "Text-to-SQL — Terzo Canale":
SQL non compete nel ranking, decide chi puo' competere.
"""

from app import config
from app.vector_store import cerca_prodotti as cerca_dense
from app.bm25_search import cerca_prodotti_bm25
from app.text_to_sql import filtra_per_vincoli

RRF_K = 60  # costante standard — vedi deck "RRF — Reciprocal Rank Fusion"


def _chiave(prodotto: dict) -> str:
    """Chiave univoca per identificare lo stesso prodotto nelle due liste."""
    return prodotto["nome"]


def rrf_fusion(lista_dense: list[dict], lista_bm25: list[dict], top_k: int) -> list[dict]:
    """
    Fonde due liste di prodotti ordinate per rilevanza usando RRF.

    lista_dense: risultati da vector_store.cerca_prodotti() (con campo 'distanza')
    lista_bm25:  risultati da bm25_search.cerca_prodotti_bm25() (con campo 'score')

    Entrambe le liste devono già essere ordinate dal più al meno rilevante
    (rank 1 = primo elemento della lista).

    Restituisce una lista di prodotti fusi, ordinata per score RRF decrescente,
    con un campo aggiuntivo 'fonte' che indica se il prodotto è stato trovato
    da entrambi i sistemi, solo dal dense, o solo da BM25.
    """
    scores_rrf: dict[str, float] = {}
    prodotti_per_chiave: dict[str, dict] = {}
    fonte_per_chiave: dict[str, set] = {}

    # Contributo del retrieval denso
    for rank, p in enumerate(lista_dense, start=1):
        k = _chiave(p)
        scores_rrf[k] = scores_rrf.get(k, 0.0) + 1.0 / (RRF_K + rank)
        prodotti_per_chiave[k] = p
        fonte_per_chiave.setdefault(k, set()).add("dense")

    # Contributo del retrieval sparso (BM25)
    for rank, p in enumerate(lista_bm25, start=1):
        k = _chiave(p)
        scores_rrf[k] = scores_rrf.get(k, 0.0) + 1.0 / (RRF_K + rank)
        # Se il prodotto non era nella lista dense, salvalo ora
        prodotti_per_chiave.setdefault(k, p)
        fonte_per_chiave.setdefault(k, set()).add("bm25")

    # Ordina per score RRF decrescente
    chiavi_ordinate = sorted(scores_rrf.keys(), key=lambda k: scores_rrf[k], reverse=True)

    risultati = []
    for k in chiavi_ordinate[:top_k]:
        p = dict(prodotti_per_chiave[k])  # copia per non mutare l'originale
        p["score_rrf"] = round(scores_rrf[k], 5)
        fonti = fonte_per_chiave[k]
        if fonti == {"dense", "bm25"}:
            p["fonte"] = "entrambi"
        elif fonti == {"dense"}:
            p["fonte"] = "solo dense"
        else:
            p["fonte"] = "solo bm25"
        risultati.append(p)

    return risultati


def cerca_prodotti_hybrid(domanda: str, top_k: int | None = None) -> list[dict]:
    """
    Ricerca ibrida: esegue dense + BM25 in parallelo (logicamente),
    applica il filtro hard text-to-SQL se la domanda ha un vincolo
    strutturato, poi fonde i risultati rimasti con RRF.

    Questa è la funzione che chatbot.py chiama al posto di
    vector_store.cerca_prodotti() per ottenere risultati più robusti.
    """
    if top_k is None:
        top_k = config.TOP_K

    # Prendiamo più risultati grezzi di top_k da entrambi i sistemi,
    # così RRF ha materiale sufficiente per fondere bene prima di tagliare.
    n_grezzi = max(top_k * 2, 10)

    risultati_dense = cerca_dense(domanda, top_k=n_grezzi)
    risultati_bm25 = cerca_prodotti_bm25(domanda, top_k=n_grezzi)

    # Filtro hard text-to-SQL: None = nessun vincolo rilevato, nessun filtro.
    # Un insieme (anche vuoto) = applica il filtro sui nomi ammessi.
    if config.USE_TEXT_TO_SQL:
        nomi_ammessi = filtra_per_vincoli(domanda)
        if nomi_ammessi is not None:
            risultati_dense = [p for p in risultati_dense if p["nome"] in nomi_ammessi]
            risultati_bm25 = [p for p in risultati_bm25 if p["nome"] in nomi_ammessi]

    return rrf_fusion(risultati_dense, risultati_bm25, top_k=top_k)
