#!/usr/bin/env bash
# Builds the portable kit "kit-c-arduino" for Linux x86_64, needing no installation and no sudo:
#   vscode/   VS Code in portable mode (vscode/data), in Portuguese, with C/C++ and Code Runner
#   gcc/      static gcc (musl.cc); bin/gcc adds -static so programs run on any distribution
#   arduino/  arduino-cli with the Arduino Uno (AVR) core and the Servo library
#   bin/      helper commands used by the VS Code tasks (arduino-compilar, arduino-enviar, arduino-monitor)
#   exemplos/ the course examples (C and Arduino), if a folder is given
# Uso: construir_kit.sh <pasta de saída> [pasta de exemplos]
set -euo pipefail
SAIDA=$(realpath -m "${1:?informe a pasta de saída}")
EXEMPLOS=${2:-}
AQUI=$(cd "$(dirname "$0")" && pwd)
KIT=$SAIDA/kit-c-arduino
CACHE=$SAIDA/downloads
mkdir -p "$CACHE"
rm -rf "$KIT"
mkdir -p "$KIT"/{bin,arduino}

baixar() {   # baixar <url> <arquivo>: downloads once into the cache
  [ -s "$CACHE/$2" ] || curl -fsSL --retry 3 -o "$CACHE/$2" "$1"
}

echo "== Baixando"
baixar https://update.code.visualstudio.com/latest/linux-x64/stable vscode.tar.gz
baixar https://musl.cc/x86_64-linux-musl-native.tgz gcc-musl.tgz
baixar https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz arduino-cli.tar.gz

echo "== VS Code (modo portátil)"
mkdir -p "$KIT/vscode"
tar -xzf "$CACHE/vscode.tar.gz" -C "$KIT/vscode" --strip-components=1
mkdir -p "$KIT/vscode/data/user-data/User"          # a pasta data/ liga o modo portátil
for extensao in ms-vscode.cpptools formulahendry.code-runner MS-CEINTL.vscode-language-pack-pt-BR; do
  "$KIT/vscode/bin/code" --install-extension "$extensao" --force   # baixa do Marketplace a versão para Linux x64
done
cp "$AQUI"/vscode/settings.json "$AQUI"/vscode/tasks.json "$AQUI"/vscode/keybindings.json "$KIT/vscode/data/user-data/User/"
cp "$AQUI"/vscode/argv.json "$KIT/vscode/data/argv.json"
python3 "$AQUI/gerar_languagepacks.py" "$KIT"                  # português já na primeira vez que abrir

echo "== gcc"
mkdir -p "$KIT/gcc"
tar -xzf "$CACHE/gcc-musl.tgz" -C "$KIT/gcc" --strip-components=1

echo "== arduino-cli"
tar -xzf "$CACHE/arduino-cli.tar.gz" -C "$KIT/arduino" arduino-cli
export ARDUINO_DIRECTORIES_DATA=$KIT/arduino/data ARDUINO_DIRECTORIES_DOWNLOADS=$CACHE/arduino ARDUINO_DIRECTORIES_USER=$KIT/arduino/user
"$KIT/arduino/arduino-cli" core update-index >/dev/null
"$KIT/arduino/arduino-cli" core install arduino:avr >/dev/null
"$KIT/arduino/arduino-cli" lib install Servo >/dev/null
# IntelliSense dos sketches: só as pastas avr/ e util/ do avr-libc (sem o stdio.h do AVR, que atrapalharia os programas C)
mkdir -p "$KIT/arduino/intellisense"
AVR_INCLUDE=$(cd "$KIT/arduino/intellisense" && ls -d ../data/packages/arduino/tools/avr-gcc/*/avr/include | head -1)
ln -sfn "$AVR_INCLUDE/avr" "$KIT/arduino/intellisense/avr"
ln -sfn "$AVR_INCLUDE/util" "$KIT/arduino/intellisense/util"

echo "== Scripts e exemplos"
cp "$AQUI"/bin/* "$KIT/bin/"
cp "$AQUI"/abrir-vscode.sh "$AQUI"/criar-atalho.sh "$AQUI"/restaurar-exemplos.sh "$AQUI"/verificar-placa.sh "$AQUI"/LEIA-ME.txt "$KIT/"
chmod +x "$KIT"/bin/* "$KIT"/*.sh
if [ -n "$EXEMPLOS" ]; then cp -r "$EXEMPLOS" "$KIT/exemplos"; else mkdir -p "$KIT/exemplos"; fi
cp -r "$KIT/exemplos" "$KIT/.exemplos-originais"                 # cópia intacta para restaurar-exemplos.sh

echo "== Limpeza"
rm -rf "$KIT/vscode/data/user-data/CachedExtensionVSIXs" "$KIT/vscode/data/user-data/logs" "$KIT/vscode/data/user-data/machineid"   # caches da instalação (languagepacks.json fica: é ele que liga o português)
rm -rf "$KIT/gcc/share/man" "$KIT/gcc/share/info" "$KIT/gcc/share/doc"                     # documentação do gcc

echo "== Pacote"
tar -C "$SAIDA" -I 'xz -T0 -6' -cf "$SAIDA/kit-c-arduino-linux-x64.tar.xz" kit-c-arduino   # xz em todos os núcleos
cp "$AQUI/instalar.sh" "$AQUI/LEIA-ME.txt" "$SAIDA/"              # vão para o pendrive junto do pacote
du -sh "$KIT" "$SAIDA/kit-c-arduino-linux-x64.tar.xz"
