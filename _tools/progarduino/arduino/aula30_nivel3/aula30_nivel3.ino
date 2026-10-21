// Aula 30 – Nível 3: Trocar o estado de dois LEDs
// pecas: botao 2; led 8 vermelho; led 9 verde
// Cada toque troca os estados dos LEDs usando uma função com ponteiros
#define PINO_BOTAO 2                    // botão no pino 2
bool vermelho = true, verde = false;    // estado de cada LED

void trocar(bool *a, bool *b) {         // troca dois bool pelos endereços
  bool aux = *a;                        // guarda o valor apontado por a
  *a = *b;                              // o valor apontado por b vai para a
  *b = aux;                             // o valor guardado vai para b
}

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);    // PINO_BOTAO como entrada com pull-up interno
  pinMode(8, OUTPUT);                   // 8 como saída
  pinMode(9, OUTPUT);                   // 9 como saída
}

void loop() {                           // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {   // botão apertado?
    trocar(&vermelho, &verde);          // passa os endereços
    delay(300);                         // espera 300 ms
  }
  digitalWrite(8, vermelho);            // 8 recebe vermelho (verdadeiro acende, falso apaga)
  digitalWrite(9, verde);               // 9 recebe verde (verdadeiro acende, falso apaga)
}
