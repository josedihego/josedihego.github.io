// Aula 26 – Nível 3: Mediana × média
// pecas: ldr A0
// Compara média e mediana no Plotter Serial: a mediana ignora picos
const int N = 7;                                      // leituras por bloco (ímpar: tem um elemento do meio)
int v[N];                                             // declara v[N] (int)

void setup() {                                        // roda uma vez, quando a placa liga
  Serial.begin(9600);                                 // abre o Monitor Serial a 9600 baud
  randomSeed(analogRead(A5));                         // pino solto gera ruído: sorteios diferentes a cada vez
}

void loop() {                                         // repete para sempre
  long soma = 0;                                      // long: a soma de muitas leituras passa de 32767
  for (int i = 0; i < N; i++) {                       // percorre os N elementos
    v[i] = analogRead(A0);                            // guarda a leitura na posição i
    if (random(10) == 0) v[i] = 1023;                 // simula um pico de ruído de vez em quando
    soma += v[i];                                     // acumula o elemento
    delay(5);                                         // espera 5 ms
  }
  for (int p = 0; p < N - 1; p++)                     // passadas do bubble sort
    for (int i = 0; i < N - 1 - p; i++)               // compara vizinhos na parte desordenada
      if (v[i] > v[i + 1]) { int aux = v[i]; v[i] = v[i + 1]; v[i + 1] = aux; }   // fora de ordem: troca os vizinhos
  Serial.print("media:");                             // envia o texto ao Monitor Serial
  Serial.print(soma / N);                             // envia soma / N ao Monitor Serial
  Serial.print(" mediana:");                          // rótulo:valor aparece na legenda do Plotter
  Serial.println(v[N / 2]);                           // envia v[N / 2] ao Monitor Serial e quebra a linha
  delay(50);                                          // espera 50 ms
}
