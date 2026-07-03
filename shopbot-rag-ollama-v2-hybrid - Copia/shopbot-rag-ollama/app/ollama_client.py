"""
ollama_client.py — Client Ollama stabile (chat + embeddings)

FIX principali:
- embedding endpoint corretto: /api/embeddings
- chat non-stream sicura
- streaming robusto (JSON line-by-line)
"""

import json
import requests
from app import config


# ─────────────────────────────────────────────
# EMBEDDINGS (FIXED)
# ─────────────────────────────────────────────

def get_embedding(testo: str) -> list[float]:
    """
    Genera embedding vettoriale usando Ollama.
    Endpoint corretto: /api/embeddings
    """
    url = f"{config.OLLAMA_BASE_URL}/api/embeddings"

    payload = {
        "model": config.OLLAMA_EMBED_MODEL,
        "prompt": testo,   # ⚠️ corretto per Ollama embeddings API
    }

    resp = requests.post(url, json=payload, timeout=60)
    resp.raise_for_status()

    data = resp.json()

    # risposta tipica: {"embedding": [...]}
    return data["embedding"]


# ─────────────────────────────────────────────
# CHAT (STABILE)
# ─────────────────────────────────────────────

def chat(messages: list[dict], stream: bool = True):
    """
    Chat Ollama.
    stream=True -> generator
    stream=False -> stringa completa
    """

    url = f"{config.OLLAMA_BASE_URL}/api/chat"

    payload = {
        "model": config.OLLAMA_CHAT_MODEL,
        "messages": messages,
        "stream": stream,
        "options": {
            "temperature": 0.3
        }
    }

    # ───────── NON STREAM (PIÙ STABILE) ─────────
    if not stream:
        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["message"]["content"]

    # ───────── STREAM ROBUSTO ─────────
    with requests.post(url, json=payload, stream=True, timeout=120) as resp:
        resp.raise_for_status()

        buffer = ""

        for line in resp.iter_lines():
            if not line:
                continue

            decoded = line.decode("utf-8")

            # Ollama manda JSON line-by-line
            try:
                chunk = json.loads(decoded)
            except json.JSONDecodeError:
                continue

            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content

            if chunk.get("done"):
                break