// Aula 12 – Nível 1: Revisão: tensão no Serial
// Revisão: tensão do A0 com 3 casas decimais
void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  Serial.println(analogRead(A0) * 5.0 / 1023.0, 3);   // envia analogRead(A0) * 5.0 / 1023.0 ao Monitor Serial e quebra a linha
  delay(250);                           // espera 250 ms
}
