#!/usr/bin/env bash
# import_docker_bundle.sh
# Carica immagini Docker e modelli Ollama dal bundle offline.
set -e

DIST="dist"

echo ""
echo "╔══════════════════════════════════════════════╗"
echo "║       SHOPBOT — Import Bundle Offline        ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

# Immagini Docker
if [ -f "$DIST/shopbot-images.tar.gz" ]; then
  echo "▸ Carico immagini Docker..."
  gunzip -c "$DIST/shopbot-images.tar.gz" | docker load
  echo "  ✓ Immagini caricate."
else
  echo "  ⚠️  $DIST/shopbot-images.tar.gz non trovato. Salto."
fi

# Modelli Ollama
if [ -f "$DIST/ollama-models.tar.gz" ]; then
  echo ""
  echo "▸ Avvio Ollama per ripristinare i modelli..."
  docker compose up -d ollama
  sleep 3

  OLLAMA_VOL=$(docker volume inspect shopbot-rag-ollama_ollama_models \
    --format '{{.Mountpoint}}' 2>/dev/null || echo "")

  if [ -n "$OLLAMA_VOL" ]; then
    tar xzf "$DIST/ollama-models.tar.gz" -C "$OLLAMA_VOL"
    echo "  ✓ Modelli ripristinati."
  else
    echo "  ⚠️  Volume ollama_models non trovato."
  fi
else
  echo "  ⚠️  $DIST/ollama-models.tar.gz non trovato. I modelli verranno scaricati online."
fi

echo ""
echo "✅ Import completato. Avvia il progetto:"
echo "   docker compose up -d mysql ollama"
echo "   docker compose run --rm app python -m app.main setup --reset"
echo "   docker compose run --rm app python -m app.main chat"
echo ""
