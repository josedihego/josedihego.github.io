// Aula 26 – Nível 1: Maior de 10 leituras
// A cada segundo: 10 leituras guardadas num vetor e a maior delas
int v[10];                              // declara v[10] (int)

void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  for (int i = 0; i < 10; i++) {        // 10 voltas
    v[i] = analogRead(A0);              // guarda a leitura na posição i
    delay(50);                          // espera 50 ms
  }
  int maior = v[0];                     // começa supondo que a primeira é a maior
  for (int i = 1; i < 10; i++) if (v[i] > maior) maior = v[i];   // procura a maior
  Serial.print("Maior: ");              // envia o texto ao Monitor Serial
  Serial.println(maior);                // envia maior ao Monitor Serial e quebra a linha
  delay(500);                           // espera 500 ms
}
