#!/usr/bin/env bash
# export_docker_bundle.sh
# Salva immagini Docker e modelli Ollama in dist/ per distribuzione offline.
set -e

DIST="dist"
mkdir -p "$DIST"

echo ""
echo "╔══════════════════════════════════════════════╗"
echo "║       SHOPBOT — Export Bundle Offline        ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

# Immagini Docker
echo "▸ Salvo immagini Docker..."
docker save mysql:8.4 ollama/ollama:latest shopbot-rag-ollama-app:latest \
  | gzip > "$DIST/shopbot-images.tar.gz"
echo "  ✓ $DIST/shopbot-images.tar.gz"

# Modelli Ollama (copiati dal volume)
echo ""
echo "▸ Salvo modelli Ollama..."
OLLAMA_VOL=$(docker volume inspect shopbot-rag-ollama_ollama_models \
  --format '{{.Mountpoint}}' 2>/dev/null || echo "")

if [ -z "$OLLAMA_VOL" ]; then
  echo "  ⚠️  Volume ollama_models non trovato. Esegui prima install_models.sh"
else
  tar czf "$DIST/ollama-models.tar.gz" -C "$OLLAMA_VOL" .
  echo "  ✓ $DIST/ollama-models.tar.gz"
fi

echo ""
echo "✅ Bundle pronto in $DIST/"
du -sh "$DIST"/*
echo ""
echo "Per importare sul computer dello studente:"
echo "  chmod +x scripts/import_docker_bundle.sh"
echo "  ./scripts/import_docker_bundle.sh"
echo ""
