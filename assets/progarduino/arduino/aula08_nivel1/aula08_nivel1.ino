// Aula 8 – Nível 1: Um número em 4 LEDs
// Mostra o número 11 (1011 em binário) nos LEDs dos pinos 5 (bit 3) a 2 (bit 0)
int numero = 11;                                // troque por 0 a 15

void setup() {                                  // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 5; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 5 como saída
  digitalWrite(2, bitRead(numero, 0));          // bitRead pega um bit: peso 1
  digitalWrite(3, bitRead(numero, 1));          // peso 2
  digitalWrite(4, bitRead(numero, 2));          // peso 4
  digitalWrite(5, bitRead(numero, 3));          // peso 8
}

void loop() {                                   // repete para sempre
}
