// Aula 21 – Nível 1: Luz em porcentagem
// map + constrain: converte a leitura do LDR em 0 a 100% de escuridão
#include <Arduino.h>                             // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                   // roda uma vez, quando a placa liga
  Serial.begin(9600);                            // abre o Monitor Serial a 9600 baud
}

void loop() {                                    // repete para sempre
  int leitura = analogRead(A0);                  // lê o A0 (0 a 1023)
  int escuro = map(leitura, 100, 900, 0, 100);   // faixa útil do sensor
  escuro = constrain(escuro, 0, 100);            // corta valores fora de 0..100
  Serial.print("Escuridão: ");                   // envia o texto ao Monitor Serial
  Serial.print(escuro);                          // envia escuro ao Monitor Serial
  Serial.println("%");                           // envia o texto ao Monitor Serial e quebra a linha
  delay(200);                                    // espera 200 ms
}
