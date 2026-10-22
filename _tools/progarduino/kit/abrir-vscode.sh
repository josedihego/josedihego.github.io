#!/usr/bin/env bash
# Abre o VS Code do kit com o gcc e o arduino-cli do próprio kit (nada é instalado no computador)
KIT_DIR=$(cd "$(dirname "$(readlink -f "$0")")" && pwd)
export KIT_DIR
export PATH="$KIT_DIR/bin:$KIT_DIR/arduino:$PATH"
export ARDUINO_DIRECTORIES_DATA="$KIT_DIR/arduino/data"
export ARDUINO_DIRECTORIES_DOWNLOADS="$KIT_DIR/arduino/downloads"
export ARDUINO_DIRECTORIES_USER="$KIT_DIR/arduino/user"
# O VS Code guarda caminhos absolutos do pacote de idioma: aponta para onde o kit está agora
IDIOMA="$KIT_DIR/vscode/data/user-data/languagepacks.json"
[ -f "$IDIOMA" ] && sed -i -E "s#\"[^\"]*/vscode/data/extensions/#\"$KIT_DIR/vscode/data/extensions/#g" "$IDIOMA"
# A extensão C/C++ não expande variáveis nas configurações do usuário: grava o caminho atual do gcc e do Arduino
CONFIG="$KIT_DIR/vscode/data/user-data/User/settings.json"
[ -f "$CONFIG" ] && sed -i -E "s#\"[^\"]*/bin/gcc\"#\"$KIT_DIR/bin/gcc\"#; s#\"[^\"]*/arduino/(data/packages|intellisense)#\"$KIT_DIR/arduino/\1#g" "$CONFIG"
# --no-sandbox: sem ele o VS Code não abre em distribuições que bloqueiam o sandbox para programas fora do sistema (ex.: Ubuntu 24.04)
# Pasta de trabalho fora do kit: reinstalar o kit não apaga os trabalhos dos estudantes (a conta é compartilhada)
AREA="$HOME/C-e-Arduino"
mkdir -p "$AREA/trabalhos"
[ -e "$AREA/exemplos" ] || ln -s "$KIT_DIR/exemplos" "$AREA/exemplos"
[ -e "$AREA/trabalhos/LEIA-ME.txt" ] || printf 'Crie aqui uma pasta com o seu nome e salve nela os seus programas.\nA conta é compartilhada: copie os seus arquivos para o seu pendrive no fim da aula.\n' > "$AREA/trabalhos/LEIA-ME.txt"
if [ $# -eq 0 ]; then set -- "$AREA"; fi
exec "$KIT_DIR/vscode/code" --no-sandbox "$@"
