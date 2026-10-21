// Aula 26 – Nível 2: Filtro de mediana
// Ordena 5 leituras e pega a do meio: elimina picos de ruído
int v[5];                                             // declara v[5] (int)

void setup() {                                        // roda uma vez, quando a placa liga
  Serial.begin(9600);                                 // abre o Monitor Serial a 9600 baud
}

void loop() {                                         // repete para sempre
  for (int i = 0; i < 5; i++) {                       // 5 voltas
    v[i] = analogRead(A0);                            // guarda a leitura na posição i
    delay(10);                                        // espera 10 ms
  }
  for (int p = 0; p < 4; p++) {                       // bubble sort
    for (int i = 0; i < 4 - p; i++) {                 // compara vizinhos na parte desordenada
      if (v[i] > v[i + 1]) { int aux = v[i]; v[i] = v[i + 1]; v[i + 1] = aux; }   // fora de ordem: troca os vizinhos
    }
  }
  Serial.println(v[2]);                               // mediana: o elemento do meio
  delay(100);                                         // espera 100 ms
}
