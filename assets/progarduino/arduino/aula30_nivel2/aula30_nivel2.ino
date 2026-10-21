// Aula 30 – Nível 2: Uma leitura, duas respostas
// ler_luz devolve a leitura e a tensão pelos ponteiros
void ler_luz(int *leitura, float *volts) {    // duas saídas por ponteiro
  *leitura = analogRead(A0);                  // grava a leitura na variável de quem chamou
  *volts = *leitura * 5.0 / 1023.0;           // grava a tensão na outra variável
}

void setup() {                                // roda uma vez, quando a placa liga
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
}

void loop() {                                 // repete para sempre
  int bruto;                                  // declara bruto (int)
  float tensao;                               // declara tensao (float)
  ler_luz(&bruto, &tensao);                   // passa os endereços
  Serial.print(bruto);                        // envia bruto ao Monitor Serial
  Serial.print(" = ");                        // envia o texto ao Monitor Serial
  Serial.print(tensao, 2);                    // envia tensao ao Monitor Serial
  Serial.println(" V");                       // envia o texto ao Monitor Serial e quebra a linha
  delay(300);                                 // espera 300 ms
}
