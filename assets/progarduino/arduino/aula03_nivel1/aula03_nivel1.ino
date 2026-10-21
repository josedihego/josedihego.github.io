// Aula 3 – Nível 1: Eco de números
// Digite um número no Monitor Serial: a placa responde com o dobro
void setup() {                                // roda uma vez, quando a placa liga
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
  Serial.println("Digite um número:");        // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                 // repete para sempre
  if (Serial.available() > 0) {               // chegou algo pela serial?
    int numero = Serial.parseInt();           // lê um inteiro do texto recebido
    Serial.print("O dobro é ");               // envia o texto ao Monitor Serial
    Serial.println(numero * 2);               // envia numero * 2 ao Monitor Serial e quebra a linha
    while (Serial.available() > 0) Serial.read();   // descarta o resto da linha (Enter)
  }
}
