#!/usr/bin/env bash
# install_models.sh — scarica i modelli Ollama necessari per ShopBot RAG
set -e

echo ""
echo "╔══════════════════════════════════════════════╗"
echo "║       SHOPBOT — Download Modelli Ollama      ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

echo "▸ Modello chat: llama3.2:3b (~2 GB)"
docker compose exec ollama ollama pull llama3.2:3b

echo ""
echo "▸ Modello embedding: nomic-embed-text (~274 MB)"
docker compose exec ollama ollama pull nomic-embed-text

echo ""
echo "✅ Fatto. Modelli disponibili:"
docker compose exec ollama ollama list
echo ""
