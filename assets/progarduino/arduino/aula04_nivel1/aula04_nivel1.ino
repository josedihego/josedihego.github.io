// Aula 4 – Nível 1: Ler o potenciômetro
// Mostra a leitura analógica (0 a 1023) do potenciômetro no pino A0
#include <Arduino.h>                  // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                        // roda uma vez, quando a placa liga
  Serial.begin(9600);                 // abre o Monitor Serial a 9600 baud
}

void loop() {                         // repete para sempre
  int leitura = analogRead(A0);       // conversor de 10 bits: 0 a 1023
  Serial.println(leitura);            // use Ferramentas → Plotter Serial para ver o gráfico
  delay(100);                         // espera 100 ms
}
