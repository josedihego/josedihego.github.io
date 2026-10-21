// Aula 29 – Nível 3: Função mediana
// pecas: ldr A0
// mediana(v, n) ordena uma cópia do vetor e devolve o valor do meio
int mediana(const int v[], int n) {           // const: a função promete não alterar v
  int c[15];                                  // cópia: não altera o vetor original
  for (int i = 0; i < n; i++) c[i] = v[i];    // copia o vetor
  for (int p = 0; p < n - 1; p++)             // passadas do bubble sort
    for (int i = 0; i < n - 1 - p; i++)       // compara vizinhos na parte ainda desordenada
      if (c[i] > c[i + 1]) { int a = c[i]; c[i] = c[i + 1]; c[i + 1] = a; }   // fora de ordem: troca na cópia
  return c[n / 2];                            // o elemento do meio da cópia ordenada
}

int leituras[9];                              // declara leituras[9] (int)

void setup() {                                // roda uma vez, quando a placa liga
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
}

void loop() {                                 // repete para sempre
  for (int i = 0; i < 9; i++) {               // 9 leituras
    leituras[i] = analogRead(A0);             // guarda a leitura na posição i
    delay(5);                                 // espera 5 ms
  }
  Serial.println(mediana(leituras, 9));       // envia mediana(leituras ao Monitor Serial e quebra a linha
  delay(100);                                 // espera 100 ms
}
