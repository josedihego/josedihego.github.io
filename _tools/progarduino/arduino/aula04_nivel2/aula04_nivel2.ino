// Aula 4 – Nível 2: Leitura em volts
// pecas: pot A0
// Converte a leitura do A0 em tensão (0 a 5 V)
void setup() {                                      // roda uma vez, quando a placa liga
  Serial.begin(9600);                               // abre o Monitor Serial a 9600 baud
}

void loop() {                                       // repete para sempre
  int leitura = analogRead(A0);                     // 0 a 1023
  float tensao = leitura * 5.0 / 1023.0;            // 5.0 e 1023.0 garantem conta com decimais
  Serial.print("Leitura: ");                        // envia o texto ao Monitor Serial
  Serial.print(leitura);                            // envia leitura ao Monitor Serial
  Serial.print("   Tensão: ");                      // envia o texto ao Monitor Serial
  Serial.print(tensao, 2);                          // envia tensao ao Monitor Serial
  Serial.println(" V");                             // envia o texto ao Monitor Serial e quebra a linha
  delay(200);                                       // espera 200 ms
}
