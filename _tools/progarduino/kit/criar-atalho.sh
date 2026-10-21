#!/usr/bin/env bash
# Cria um atalho "Kit C e Arduino" no menu de aplicativos e na área de trabalho (só para o usuário atual)
KIT_DIR=$(cd "$(dirname "$(readlink -f "$0")")" && pwd)
ATALHO="[Desktop Entry]
Type=Application
Name=Kit C e Arduino
Comment=VS Code com C e Arduino (kit portátil)
Exec=\"$KIT_DIR/abrir-vscode.sh\" %F
Icon=$KIT_DIR/vscode/resources/app/resources/linux/code.png
Terminal=false
Categories=Development;"
mkdir -p "$HOME/.local/share/applications"
echo "$ATALHO" > "$HOME/.local/share/applications/kit-c-arduino.desktop"
AREA=$(xdg-user-dir DESKTOP 2>/dev/null || echo "$HOME/Desktop")
if [ -d "$AREA" ]; then
  echo "$ATALHO" > "$AREA/kit-c-arduino.desktop"
  chmod +x "$AREA/kit-c-arduino.desktop"
  gio set "$AREA/kit-c-arduino.desktop" metadata::trusted true 2>/dev/null || true
fi
echo "Atalho criado: procure por \"Kit C e Arduino\" no menu de aplicativos."
