#!/usr/bin/env bash
# Compiles every sketch in _tools/progarduino/arduino for the Arduino Uno with the kit's arduino-cli
# Uso: testar_arduino.sh <pasta do kit-c-arduino>
KIT=${1:?informe a pasta do kit}
export ARDUINO_DIRECTORIES_DATA=$KIT/arduino/data ARDUINO_DIRECTORIES_USER=$KIT/arduino/user ARDUINO_DIRECTORIES_DOWNLOADS=/tmp/arduino-downloads
AQUI=$(cd "$(dirname "$0")" && pwd)
falhas=0
for sketch in "$AQUI"/arduino/*/; do
  nome=$(basename "$sketch")
  if saida=$("$KIT/arduino/arduino-cli" compile --fqbn arduino:avr:uno --warnings all "$sketch" 2>&1); then
    avisos=$(echo "$saida" | grep -c "warning:")
    echo "OK $nome: $(echo "$saida" | grep -o 'uses [0-9]* bytes ([0-9]*%) of program' | head -1)${avisos:+ | avisos: $avisos}"
    [ "$avisos" -gt 0 ] && echo "$saida" | grep -A2 "warning:" | head -6
  else
    falhas=$((falhas + 1))
    echo "FALHOU $nome:"; echo "$saida" | grep -E "error|Error" | head -5
  fi
done
echo "falhas: $falhas"
