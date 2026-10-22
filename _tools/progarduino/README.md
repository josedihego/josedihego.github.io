# Ferramentas de "Programação aplicada com C e Arduino" (/progarduino/)

Pasta ignorada pelo Jekyll (começa com `_`), não é publicada. Tudo tem três níveis: 1 Básico, 2 Intermediário, 3 Avançado.

| O quê | Fonte (edite aqui) | Gerado em |
|---|---|---|
| Texto das 36 aulas e exercícios | `_data/progarduino.yml` | página `/progarduino/` |
| C (108 programas) | `c/aulaNN_nivelK.c` (linha 2: `// teste:` com as entradas do testador) | `assets/progarduino/c/` |
| Arduino (108 sketches) | `arduino/aulaNN_nivelK/aulaNN_nivelK.ino` (linha 2: `// pecas:` com o circuito) | `assets/progarduino/arduino/` (+ `diagram.json` do Wokwi) |
| Títulos dos níveis | gerado | `_data/progarduino_exemplos.yml` |
| Link do kit | `_data/progarduino_kit.yml` | botão de download da página |

Peças aceitas em `// pecas:` (separadas por `;`): `led PINO COR`, `botao PINO`, `pot A0`, `ldr A0`, `buzzer PINO`,
`ultrassom TRIG ECHO`, `servo PINO`, `rgb R G B`.

## Comandos (na raiz do site)

```bash
# testa: compila os 108 programas C com -Wall -Wextra, roda com as entradas de teste e aponta linhas sem comentário
python3 _tools/progarduino/testar_c.py

# publica os exemplos (assets/progarduino, zip e títulos); --kit gera também a pasta exemplos do kit
python3 _tools/progarduino/gerar_exemplos.py . --kit /tmp/exemplos

# constrói o kit portátil (VS Code + gcc + arduino-cli) com os exemplos: gera kit-c-arduino-linux-x64.tar.xz
_tools/progarduino/kit/construir_kit.sh /tmp/kit /tmp/exemplos

# compila os 108 sketches para o Arduino Uno com o arduino-cli do kit
_tools/progarduino/testar_arduino.sh /tmp/kit/kit-c-arduino
```

## Kit portátil

- `vscode/data` liga o modo portátil: nada é gravado fora da pasta do kit.
- `bin/gcc` chama o gcc do musl.cc com `-static`: os programas rodam em qualquer Linux sem gcc instalado.
- `abrir-vscode.sh` ajusta PATH e as pastas do arduino-cli, corrige os caminhos do pacote de idioma e abre com `--no-sandbox`
  (necessário em distribuições como o Ubuntu 24.04 para programas fora do sistema).
- `vscode/settings.json` desliga o Copilot e as boas-vindas e configura o Code Runner (▶/F5): C compila para `.out`, `.ino` usa `arduino-rodar`.
- `arduino/intellisense/` expõe só `avr/` e `util/` do avr-libc, para o editor entender os sketches sem trocar o `stdio.h` dos programas C.
- Os sketches começam com `#include <Arduino.h>`: sem ele a extensão C/C++ marca `digitalWrite` etc. como erro.
