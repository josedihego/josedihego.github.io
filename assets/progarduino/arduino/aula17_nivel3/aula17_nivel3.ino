// Aula 17 – Nível 3: Teste de reflexo
// O LED acende depois de um tempo aleatório; aperte o botão o mais rápido possível
#include <Arduino.h>                             // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                             // botão no pino 2
#define PINO_LED 8                               // LED no pino 8

void setup() {                                   // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);             // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);                     // PINO_LED como saída
  Serial.begin(9600);                            // abre o Monitor Serial a 9600 baud
  randomSeed(analogRead(A5));                    // pino solto gera ruído: sorteios diferentes a cada vez
}

void loop() {                                    // repete para sempre
  Serial.println("Prepare-se...");               // envia o texto ao Monitor Serial e quebra a linha
  delay(random(2000, 5000));                     // espera de 2 a 5 s
  if (digitalRead(PINO_BOTAO) == LOW) {          // apertou antes da hora
    Serial.println("Queimou a largada!");        // envia o texto ao Monitor Serial e quebra a linha
    delay(2000);                                 // espera 2000 ms
    return;                                      // recomeça o loop
  }
  digitalWrite(PINO_LED, HIGH);                  // acende/liga PINO_LED
  unsigned long inicio = millis();               // marca o instante inicial
  while (digitalRead(PINO_BOTAO) == HIGH) {      // espera o toque
  }
  digitalWrite(PINO_LED, LOW);                   // apaga/desliga PINO_LED
  Serial.print("Reflexo: ");                     // envia o texto ao Monitor Serial
  Serial.print(millis() - inicio);               // envia millis() - inicio ao Monitor Serial
  Serial.println(" ms");                         // envia o texto ao Monitor Serial e quebra a linha
  delay(2000);                                   // espera 2000 ms
}
