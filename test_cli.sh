#!/bin/bash

# Script de teste da CLI interativa

echo "=== Testando comando help ==="
uv run python -m src.cli --help
echo ""

echo "=== Testando comando list ==="
uv run python -m src.cli list
echo ""

echo "=== Testando comando info ==="
uv run python -m src.cli info
echo ""

echo "=== Para testar o modo interativo (start), execute: ==="
echo "uv run python -m src.cli start"
echo ""
echo "Use as setas ↑↓ para navegar e Enter para selecionar!"
