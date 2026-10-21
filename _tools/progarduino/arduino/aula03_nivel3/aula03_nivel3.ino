// Aula 3 – Nível 3: Lei de Ohm pelo Monitor Serial
// pecas: 
// Digite tensão e resistência (ex.: 12 470): a placa calcula corrente e potência
void setup() {                                        // roda uma vez, quando a placa liga
  Serial.begin(9600);                                 // abre o Monitor Serial a 9600 baud
  Serial.println("Digite: tensão(V) resistência(ohms)");   // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                         // repete para sempre
  if (Serial.available() > 0) {                       // chegou algo pela serial?
    float tensao = Serial.parseFloat();               // primeiro número
    float resistencia = Serial.parseFloat();          // segundo número
    while (Serial.available() > 0) Serial.read();     // limpa o Enter
    if (resistencia > 0) {                            // evita divisão por zero
      float corrente = tensao / resistencia;          // I = V / R
      Serial.print("Corrente: ");                     // envia o texto ao Monitor Serial
      Serial.print(corrente * 1000, 2);               // em mA
      Serial.print(" mA   Potência: ");               // envia o texto ao Monitor Serial
      Serial.print(tensao * corrente, 3);             // P = V × I
      Serial.println(" W");                           // envia o texto ao Monitor Serial e quebra a linha
    }
  }
}
