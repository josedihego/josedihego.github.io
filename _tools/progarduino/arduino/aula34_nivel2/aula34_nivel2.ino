// Aula 34 – Nível 2: Estação com alarmes
// pecas: ldr A0; pot A1; led 8 amarelo; led 9 vermelho; buzzer 7
// LED amarelo: escuro; LED vermelho e buzzer: temperatura acima de 35 °C
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
#define LED_ESCURO 8                    // LED de aviso de escuro no pino 8
#define LED_QUENTE 9                    // LED de alarme de calor no pino 9
#define PINO_BUZZER 7                   // buzzer no pino 7

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(LED_ESCURO, OUTPUT);          // LED_ESCURO como saída
  pinMode(LED_QUENTE, OUTPUT);          // LED_QUENTE como saída
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
  Serial.println("segundos,luz,temperatura,alarme");   // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                           // repete para sempre
  int luz = analogRead(A0);             // lê o sensor de luz (0 a 1023)
  float temperatura = analogRead(A1) * 50.0 / 1023;   // potenciômetro simula 0 a 50 °C
  bool escuro = luz > 600;              // verdadeiro quando está escuro
  bool quente = temperatura > 35;       // verdadeiro acima de 35 °C
  digitalWrite(LED_ESCURO, escuro);     // LED_ESCURO recebe escuro (verdadeiro acende, falso apaga)
  digitalWrite(LED_QUENTE, quente);     // LED_QUENTE recebe quente (verdadeiro acende, falso apaga)
  if (quente) tone(PINO_BUZZER, 1200, 150);   // bipe de alarme
  Serial.print(millis() / 1000); Serial.print(",");   // envia millis() / 1000); Serial.print(" ao Monitor Serial
  Serial.print(luz);             Serial.print(",");   // envia luz);             Serial.print(" ao Monitor Serial
  Serial.print(temperatura, 1);  Serial.print(",");   // envia temperatura ao Monitor Serial
  Serial.println(quente ? "QUENTE" : (escuro ? "ESCURO" : "ok"));   // envia quente ? "QUENTE" : (escuro ? "ESCURO" : "ok") ao Monitor Serial e quebra a linha
  delay(1000);                          // espera 1000 ms
}
