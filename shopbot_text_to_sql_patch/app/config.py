"""
config.py — Configurazione ShopBot RAG
Legge tutto da variabili d'ambiente con valori di default per sviluppo locale.
"""

import os

# ── MySQL ─────────────────────────────────────────────────────────────
MYSQL_HOST     = os.getenv("MYSQL_HOST",     "localhost")
MYSQL_PORT     = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "shopbot")
MYSQL_USER     = os.getenv("MYSQL_USER",     "shopbot")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "shopbot")

# ── Ollama ────────────────────────────────────────────────────────────
OLLAMA_BASE_URL    = os.getenv("OLLAMA_BASE_URL",    "http://localhost:11434")
OLLAMA_CHAT_MODEL  = os.getenv("OLLAMA_CHAT_MODEL",  "llama3.2:3b")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

# ── ChromaDB ──────────────────────────────────────────────────────────
CHROMA_PATH       = os.getenv("CHROMA_PATH",       "/data/chroma")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "prodotti")

# ── RAG ───────────────────────────────────────────────────────────────
TOP_K        = int(os.getenv("TOP_K",        "5"))    # prodotti passati al LLM
MAX_DISTANCE = float(os.getenv("MAX_DISTANCE", "1.2")) # soglia: scarta risultati troppo lontani
MAX_TURNS    = int(os.getenv("MAX_TURNS",    "8"))    # turni di history da mantenere

# ── Hybrid Search ─────────────────────────────────────────────────────
USE_HYBRID = os.getenv("USE_HYBRID", "true").lower() in ("true", "1", "yes")

# ── Text-to-SQL (filtro hard su vincoli strutturati: prezzo, disponibilita') ──
USE_TEXT_TO_SQL = os.getenv("USE_TEXT_TO_SQL", "true").lower() in ("true", "1", "yes")
