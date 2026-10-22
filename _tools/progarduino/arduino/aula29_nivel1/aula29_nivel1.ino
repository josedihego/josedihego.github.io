// Aula 29 – Nível 1: Função media(vetor, n)
// pecas: pot A0
// Passa o vetor de leituras para uma função
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
float media(int v[], int n) {           // média de um vetor de leituras
  long soma = 0;                        // long: a soma de muitas leituras passa de 32767
  for (int i = 0; i < n; i++) soma += v[i];   // soma todas as leituras
  return (float)soma / n;               // (float) evita a divisão inteira
}

int leituras[8];                        // declara leituras[8] (int)

void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  for (int i = 0; i < 8; i++) {         // 8 leituras
    leituras[i] = analogRead(A0);       // guarda a leitura na posição i
    delay(20);                          // espera 20 ms
  }
  Serial.println(media(leituras, 8), 1);   // envia media(leituras ao Monitor Serial e quebra a linha
}
