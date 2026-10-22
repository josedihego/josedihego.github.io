#!/usr/bin/env bash
# Diagnóstico do envio para o Arduino: placa conectada, permissão na porta e o serviço brltty
USUARIO=${USER:-$(id -un)}                    # o nome do usuário, mesmo se $USER não estiver definido
problemas=0
echo "== Verificando o Arduino"
PORTAS=$(ls /dev/ttyACM* /dev/ttyUSB* 2>/dev/null)
if [ -z "$PORTAS" ]; then
  echo "- Nenhuma placa conectada (conecte o Arduino pelo cabo USB para testar o envio)."
else
  for p in $PORTAS; do
    if [ -w "$p" ]; then echo "- $p: OK, dá para enviar."; else echo "- $p: SEM PERMISSÃO."; problemas=1; fi
  done
fi
if id -nG | grep -qw dialout; then
  echo "- O usuário $USUARIO está no grupo dialout: envio liberado."
else
  echo "- O usuário $USUARIO NÃO está no grupo dialout: o envio para a placa vai falhar."
  echo "  Alguém com acesso de administrador precisa rodar UMA VEZ neste computador:"
  echo "      sudo usermod -aG dialout $USUARIO"
  echo "  e depois sair e entrar de novo na sessão. Enquanto isso, use o simulador Wokwi."
  problemas=1
fi
if systemctl is-active --quiet brltty 2>/dev/null || pgrep -x brltty >/dev/null; then
  echo "- O serviço brltty está ativo: ele captura placas com chip CH340 (clones do Uno)."
  echo "  Se a placa não aparecer em /dev/ttyUSB0, o administrador deve rodar: sudo apt remove brltty"
fi
exit $problemas
