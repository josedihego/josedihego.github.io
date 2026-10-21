// Aula 8 – Nível 3: Do Monitor Serial para os LEDs
// Digite 0 a 15: o valor aparece em binário, usando os operadores >> e &
void setup() {                                          // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 5; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 5 como saída
  Serial.begin(9600);                                   // abre o Monitor Serial a 9600 baud
  Serial.println("Digite um número de 0 a 15:");        // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                           // repete para sempre
  if (Serial.available() > 0) {                         // chegou algo pela serial?
    int n = Serial.parseInt();                          // lê o número digitado
    while (Serial.available() > 0) Serial.read();       // limpa o Enter
    n = n & 0x0F;                                       // & 0000 1111 guarda só os 4 bits mais baixos
    for (int bit = 0; bit < 4; bit++) {                 // percorre os 4 bits
      digitalWrite(2 + bit, (n >> bit) & 1);            // desloca e isola um bit
    }
    Serial.print(n);                                    // envia n ao Monitor Serial
    Serial.print(" = ");                                // envia o texto ao Monitor Serial
    Serial.println(n, BIN);                             // BIN imprime em binário
  }
}
