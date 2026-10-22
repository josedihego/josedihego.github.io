// Aula 36 – Nível 1: Revisão: maior leitura com função
// Revisão: função que devolve a posição da maior leitura
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
int posicao_maior(int v[], int n) {     // devolve a posição, não o valor
  int p = 0;                            // supõe que o maior está na posição 0
  for (int i = 1; i < n; i++) if (v[i] > v[p]) p = i;   // guarda a posição do maior
  return p;                             // devolve a posição
}

int v[6];                               // declara v[6] (int)

void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  for (int i = 0; i < 6; i++) { v[i] = analogRead(A0); delay(100); }   // 6 leituras espaçadas
  Serial.print("Maior na posição ");    // envia o texto ao Monitor Serial
  Serial.println(posicao_maior(v, 6));   // envia posicao_maior(v ao Monitor Serial e quebra a linha
}
