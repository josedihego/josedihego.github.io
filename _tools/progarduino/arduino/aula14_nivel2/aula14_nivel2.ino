// Aula 14 – Nível 2: Média móvel (LDR suavizado)
// pecas: ldr A0
// Média das últimas 8 leituras: cada nova leitura substitui a mais antiga
const int N = 8;                                 // tamanho da janela da média
int leituras[N];                                 // vetor guarda as últimas leituras
int posicao = 0;                                 // onde entra a próxima
long soma = 0;                                   // soma do vetor

void setup() {                                   // roda uma vez, quando a placa liga
  Serial.begin(9600);                            // abre o Monitor Serial a 9600 baud
  for (int i = 0; i < N; i++) leituras[i] = 0;   // começa zerado
}

void loop() {                                    // repete para sempre
  int nova = analogRead(A0);                     // leitura mais recente
  soma = soma - leituras[posicao] + nova;        // tira a antiga e soma a nova
  leituras[posicao] = nova;                      // guarda no lugar da mais antiga
  posicao = (posicao + 1) % N;                   // avança e volta ao início depois do fim
  Serial.print(nova);                            // abra o Plotter Serial: bruto × suave
  Serial.print(" ");                             // envia o texto ao Monitor Serial
  Serial.println(soma / N);                      // envia soma / N ao Monitor Serial e quebra a linha
  delay(50);                                     // espera 50 ms
}
