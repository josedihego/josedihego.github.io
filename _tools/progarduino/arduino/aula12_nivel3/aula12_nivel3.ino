// Aula 12 – Nível 3: Revisão: binário com PWM
// pecas: led 2 vermelho; led 3 vermelho; led 4 vermelho; led 5 vermelho; pot A0
// Revisão: o potenciômetro escolhe 0 a 15, mostrado em binário nos LEDs
void setup() {                          // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 5; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 5 como saída
}

void loop() {                           // repete para sempre
  int n = map(analogRead(A0), 0, 1023, 0, 15);   // converte a leitura em 0 a 15
  for (int bit = 0; bit < 4; bit++) {   // percorre os 4 bits
    digitalWrite(2 + bit, bitRead(n, bit));   // 2 + bit recebe bitRead(n, bit) (verdadeiro acende, falso apaga)
  }
  delay(50);                            // espera 50 ms
}
