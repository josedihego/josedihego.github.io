#!/usr/bin/env bash
# Instala o Kit C e Arduino em ~/kit-c-arduino. Copie para a Área de Trabalho os arquivos do pendrive
# (kit-c-arduino-linux-x64.tar.xz, instalar.sh e LEIA-ME.txt), abra o terminal ali e rode:  bash instalar.sh
set -e
AQUI=$(cd "$(dirname "$0")" && pwd)
PACOTE="$AQUI/kit-c-arduino-linux-x64.tar.xz"
[ -f "$PACOTE" ] || { echo "Não encontrei $PACOTE (ele deve estar na mesma pasta deste script)."; exit 1; }
if [ -d "$HOME/kit-c-arduino" ]; then
  echo "Removendo a versão anterior do kit (a pasta ~/C-e-Arduino/trabalhos não é mexida)..."
  rm -rf "$HOME/kit-c-arduino"
fi
echo "Extraindo o kit na pasta pessoal (alguns minutos)..."
tar -xJf "$PACOTE" -C "$HOME"
"$HOME/kit-c-arduino/criar-atalho.sh"
echo
"$HOME/kit-c-arduino/verificar-placa.sh" || true
echo
echo "Pronto! Abra \"Kit C e Arduino\" no menu de aplicativos ou pelo atalho na Área de Trabalho."
echo "Os arquivos copiados do pendrive (kit-c-arduino-linux-x64.tar.xz e instalar.sh) já podem ser apagados."
