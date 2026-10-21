// Aula 13 – Nível 3: Vai e volta (efeito scanner)
// A luz vai e volta; o potenciômetro controla a velocidade
void setup() {                                           // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 6; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 6 como saída
}

void acende(int pino) {                         // pisca um LED pelo tempo do potenciômetro
  int espera = map(analogRead(A0), 0, 1023, 30, 300);    // potenciômetro escolhe 30 a 300 ms
  digitalWrite(pino, HIGH);                              // acende/liga pino
  delay(espera);                                         // espera o tempo calculado (ms)
  digitalWrite(pino, LOW);                               // apaga/desliga pino
}

void loop() {                                            // repete para sempre
  for (int pino = 2; pino <= 6; pino++) acende(pino);    // ida
  for (int pino = 5; pino >= 3; pino--) acende(pino);    // volta, sem repetir as pontas
}
