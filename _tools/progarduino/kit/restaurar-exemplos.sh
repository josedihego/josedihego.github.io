#!/usr/bin/env bash
# Desfaz qualquer alteração nos exemplos das aulas (a pasta trabalhos não é mexida)
KIT_DIR=$(cd "$(dirname "$(readlink -f "$0")")" && pwd)
rm -rf "$KIT_DIR/exemplos"
cp -r "$KIT_DIR/.exemplos-originais" "$KIT_DIR/exemplos"
echo "Exemplos restaurados."
