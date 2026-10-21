// Aula 31 – Nível 2: Percorrer um vetor com ponteiro
// pecas: 
// O ponteiro avança de elemento em elemento
int leituras[] = {512, 498, 530, 505};         // vetor de exemplo

void setup() {                                 // roda uma vez, quando a placa liga
  Serial.begin(9600);                          // abre o Monitor Serial a 9600 baud
  int *p = leituras;                           // aponta para o primeiro
  for (int i = 0; i < 4; i++) {                // percorre os 4 elementos
    Serial.print(*p);                          // valor apontado
    Serial.print(" em 0x");                    // envia o texto ao Monitor Serial
    Serial.println((unsigned int)p, HEX);      // endereços de 2 em 2 bytes
    p++;                                       // próximo int
  }
}

void loop() {                                  // repete para sempre
}
