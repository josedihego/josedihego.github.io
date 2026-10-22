// Aula 19 – Nível 3: Semáforo com botão de pedestre
// Máquina de estados: verde, amarelo, vermelho; o botão encurta o verde
#include <Arduino.h>                            // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                            // botão no pino 2
#define VERDE 8                                 // LED verde no pino 8
#define AMARELO 9                               // LED amarelo no pino 9
#define VERMELHO 10                             // LED vermelho no pino 10
int estado = 0;                                 // 0 = verde, 1 = amarelo, 2 = vermelho
unsigned long inicio = 0;                       // quando o estado atual começou
const unsigned long DURACAO[] = {6000, 2000, 4000};   // duração de verde, amarelo e vermelho (ms)

void setup() {                                  // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);            // PINO_BOTAO como entrada com pull-up interno
  pinMode(VERDE, OUTPUT);                       // VERDE como saída
  pinMode(AMARELO, OUTPUT);                     // AMARELO como saída
  pinMode(VERMELHO, OUTPUT);                    // VERMELHO como saída
}

void loop() {                                   // repete para sempre
  unsigned long tempo = millis() - inicio;      // há quanto tempo está no estado atual
  bool pedido = digitalRead(PINO_BOTAO) == LOW;   // pedestre apertou?
  if (tempo >= DURACAO[estado] || (estado == 0 && pedido && tempo > 1500)) {   // acabou o tempo ou pediram
    estado = (estado + 1) % 3;                  // próximo estado
    inicio = millis();                          // marca o início do novo estado
  }
  digitalWrite(VERDE, estado == 0);             // VERDE recebe estado == 0 (verdadeiro acende, falso apaga)
  digitalWrite(AMARELO, estado == 1);           // AMARELO recebe estado == 1 (verdadeiro acende, falso apaga)
  digitalWrite(VERMELHO, estado == 2);          // VERMELHO recebe estado == 2 (verdadeiro acende, falso apaga)
}
