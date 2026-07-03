"""
hybrid_search.py — Fusione RRF + filtro text-to-SQL FIXATO
"""

from app import config
from app.vector_store import cerca_prodotti as cerca_dense
from app.bm25_search import cerca_prodotti_bm25
from app.text_to_sql import filtra_per_vincoli

RRF_K = 60


def _chiave(prodotto: dict) -> str:
    return prodotto["nome"]


def rrf_fusion(lista_dense, lista_bm25, top_k):
    scores = {}
    prodotti = {}
    fonte = {}

    for rank, p in enumerate(lista_dense, start=1):
        k = _chiave(p)
        scores[k] = scores.get(k, 0) + 1 / (RRF_K + rank)
        prodotti[k] = p
        fonte.setdefault(k, set()).add("dense")

    for rank, p in enumerate(lista_bm25, start=1):
        k = _chiave(p)
        scores[k] = scores.get(k, 0) + 1 / (RRF_K + rank)
        prodotti.setdefault(k, p)
        fonte.setdefault(k, set()).add("bm25")

    sorted_keys = sorted(scores, key=scores.get, reverse=True)

    out = []
    for k in sorted_keys[:top_k]:
        p = dict(prodotti[k])
        p["score_rrf"] = round(scores[k], 5)

        if fonte[k] == {"dense", "bm25"}:
            p["fonte"] = "entrambi"
        elif fonte[k] == {"dense"}:
            p["fonte"] = "dense"
        else:
            p["fonte"] = "bm25"

        out.append(p)

    return out


def cerca_prodotti_hybrid(domanda: str, top_k: int | None = None) -> list[dict]:
    if top_k is None:
        top_k = config.TOP_K

    n = max(top_k * 2, 10)

    risultati_dense = cerca_dense(domanda, top_k=n)
    risultati_bm25 = cerca_prodotti_bm25(domanda, top_k=n)

    # ─────────────────────────────────────────────
    # TEXT-TO-SQL FILTER (FIX CRITICO)
    # ─────────────────────────────────────────────
    nomi_ammessi = filtra_per_vincoli(domanda)

    print(f"[DEBUG VINCOLO] {domanda} -> {nomi_ammessi}")

    if nomi_ammessi is None:
        # nessun vincolo → normale RAG
        pass

    elif len(nomi_ammessi) == 0:
        # VINCOLO ATTIVO MA NESSUN RISULTATO → STOP TOTALE
        print("[DEBUG] filtro SQL vuoto -> stop retrieval")
        return []

    else:
        # applica filtro duro
        risultati_dense = [
            p for p in risultati_dense
            if p["nome"] in nomi_ammessi
        ]

        risultati_bm25 = [
            p for p in risultati_bm25
            if p["nome"] in nomi_ammessi
        ]

    return rrf_fusion(risultati_dense, risultati_bm25, top_k)