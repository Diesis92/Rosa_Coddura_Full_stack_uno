"""
config.py — Configurazione ShopBot RAG
Legge tutto da variabili d'ambiente (impostate in docker-compose.yml).
Valori di default per avvio locale senza Docker.
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
CHROMA_PATH       = os.getenv("CHROMA_PATH",       "./chroma_db")
COLLECTION_NAME   = os.getenv("COLLECTION_NAME",   "prodotti")

# ── RAG ───────────────────────────────────────────────────────────────
TOP_K        = int(os.getenv("TOP_K",        "5"))    # prodotti passati al LLM
MAX_DISTANCE = float(os.getenv("MAX_DISTANCE", "1.2")) # soglia: scarta risultati troppo lontani
MAX_TURNS    = int(os.getenv("MAX_TURNS",    "8"))    # turni di history da mantenere
