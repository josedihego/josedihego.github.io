// Aula 13 – Nível 1: Piscar 5 vezes no início
// O for no setup pisca o LED 5 vezes e depois para
#define PINO_LED 8                     // LED no pino 8

void setup() {                         // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);           // PINO_LED como saída
  for (int i = 0; i < 5; i++) {        // 5 voltas
    digitalWrite(PINO_LED, HIGH);      // acende/liga PINO_LED
    delay(300);                        // espera 300 ms
    digitalWrite(PINO_LED, LOW);       // apaga/desliga PINO_LED
    delay(300);                        // espera 300 ms
  }
}

void loop() {                          // o loop vazio deixa o LED apagado
}
