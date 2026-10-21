// Aula 4 – Nível 3: Porcentagem com map e o perigo do int
// map converte faixas; a conta com int perde as casas decimais
void setup() {                                      // roda uma vez, quando a placa liga
  Serial.begin(9600);                               // abre o Monitor Serial a 9600 baud
}

void loop() {                                       // repete para sempre
  int leitura = analogRead(A0);                     // 0 a 1023
  int porcento = map(leitura, 0, 1023, 0, 100);     // regra de três inteira: 0 a 100
  int errado = leitura / 1023 * 100;                // divisão inteira: quase sempre 0!
  float certo = leitura / 1023.0 * 100;             // com 1023.0 a conta é decimal
  Serial.print(porcento);                           // envia porcento ao Monitor Serial
  Serial.print("%  (int: ");                        // envia o texto ao Monitor Serial
  Serial.print(errado);                             // envia errado ao Monitor Serial
  Serial.print("  float: ");                        // envia o texto ao Monitor Serial
  Serial.print(certo, 1);                           // envia certo ao Monitor Serial
  Serial.println(")");                              // envia o texto ao Monitor Serial e quebra a linha
  delay(300);                                       // espera 300 ms
}
