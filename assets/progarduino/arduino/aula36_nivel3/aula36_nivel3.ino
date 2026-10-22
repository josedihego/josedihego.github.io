// Aula 36 – Nível 3: Revisão: registro CSV com média móvel
// Revisão: CSV com leitura bruta e média das últimas 5 (vetor circular)
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
int janela[5] = {0, 0, 0, 0, 0};        // as 5 últimas leituras
int pos = 0;                            // onde entra a próxima

void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
  Serial.println("bruto,media");        // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                           // repete para sempre
  int v = analogRead(A0);               // uma leitura
  janela[pos] = v;                      // substitui a leitura mais antiga
  pos = (pos + 1) % 5;                  // avança e volta ao início
  long soma = 0;                        // long: a soma de muitas leituras passa de 32767
  for (int i = 0; i < 5; i++) soma += janela[i];   // soma a janela
  Serial.print(v);                      // envia v ao Monitor Serial
  Serial.print(",");                    // envia o texto ao Monitor Serial
  Serial.println(soma / 5);             // envia soma / 5 ao Monitor Serial e quebra a linha
  delay(200);                           // espera 200 ms
}
