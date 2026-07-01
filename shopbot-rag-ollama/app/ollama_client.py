"""
ollama_client.py — Client Ollama per chat ed embedding
Usa la libreria requests (già in requirements.txt).
Chiama direttamente le API REST native di Ollama.
"""

import json
import requests
from app import config


# ── Embedding ─────────────────────────────────────────────────────────

def get_embedding(testo: str) -> list[float]:
    """
    Genera un embedding vettoriale per il testo dato.
    Usa OLLAMA_EMBED_MODEL (default: nomic-embed-text).
    """
    url = f"{config.OLLAMA_BASE_URL}/api/embed"
    payload = {
        "model": config.OLLAMA_EMBED_MODEL,
        "input": testo,
    }
    resp = requests.post(url, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    # /api/embed restituisce {"embeddings": [[...]] }
    return data["embeddings"][0]


# ── Chat ──────────────────────────────────────────────────────────────

def chat(messages: list[dict], stream: bool = True):
    """
    Invia una lista di messaggi al modello chat Ollama.

    Se stream=True (default): genera chunk di testo uno alla volta.
    Se stream=False: restituisce la stringa completa.

    messages: [{"role": "system"|"user"|"assistant", "content": "..."}]
    """
    url = f"{config.OLLAMA_BASE_URL}/api/chat"
    payload = {
        "model":    config.OLLAMA_CHAT_MODEL,
        "messages": messages,
        "stream":   stream,
        "options": {
            "temperature": 0.3,
        },
    }

    if not stream:
        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["message"]["content"]

    # Streaming: Ollama invia una riga JSON per ogni token
    with requests.post(url, json=payload, stream=True, timeout=120) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if not line:
                continue
            chunk = json.loads(line)
            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content
            if chunk.get("done"):
                break
