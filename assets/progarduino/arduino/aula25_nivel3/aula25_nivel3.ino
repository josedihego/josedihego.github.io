// Aula 25 – Nível 3: Guardar 10 leituras
// Cada toque guarda uma leitura; com 10 guardadas, mostra todas
#include <Arduino.h>                            // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                            // botão no pino 2
int leituras[10];                               // declara leituras[10] (int)
int quantidade = 0;                             // leituras guardadas até agora

void setup() {                                  // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);            // PINO_BOTAO como entrada com pull-up interno
  Serial.begin(9600);                           // abre o Monitor Serial a 9600 baud
  Serial.println("Aperte o botão para guardar uma leitura");   // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                   // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {         // botão apertado?
    leituras[quantidade] = analogRead(A0);      // guarda na próxima posição livre
    Serial.print("Guardada #");                 // envia o texto ao Monitor Serial
    Serial.println(quantidade + 1);             // envia quantidade + 1 ao Monitor Serial e quebra a linha
    quantidade++;                               // uma a mais
    delay(300);                                 // um toque, uma leitura
    if (quantidade == 10) {                     // vetor cheio
      for (int i = 0; i < 10; i++) {            // 10 voltas
        Serial.print(leituras[i]);              // envia leituras[i] ao Monitor Serial
        Serial.print(i < 9 ? ", " : "\n");      // envia i < 9 ? " ao Monitor Serial
      }
      quantidade = 0;                           // recomeça
    }
  }
}
