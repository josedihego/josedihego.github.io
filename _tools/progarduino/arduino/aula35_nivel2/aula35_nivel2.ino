// Aula 35 – Nível 2: Simulado: função de média com mediana
// pecas: ldr A0
// Simulado: função que devolve a média das 5 leituras sem a maior e a menor
int media_aparada(int v[], int n) {     // média sem o maior e o menor
  int mn = v[0], mx = v[0];             // extremos começam no primeiro elemento
  long soma = 0;                        // long: a soma de muitas leituras passa de 32767
  for (int i = 0; i < n; i++) {         // percorre os n elementos (i de 0 a n-1)
    soma += v[i];                       // acumula o elemento
    if (v[i] < mn) mn = v[i];           // novo menor
    if (v[i] > mx) mx = v[i];           // novo maior
  }
  return (soma - mn - mx) / (n - 2);    // tira os extremos da soma e da contagem
}

int v[5];                               // declara v[5] (int)

void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  for (int i = 0; i < 5; i++) { v[i] = analogRead(A0); delay(10); }   // 5 leituras espaçadas
  Serial.println(media_aparada(v, 5));   // envia media_aparada(v ao Monitor Serial e quebra a linha
  delay(200);                           // espera 200 ms
}
