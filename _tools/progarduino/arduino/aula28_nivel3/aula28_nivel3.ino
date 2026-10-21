// Aula 28 – Nível 3: Funções para tocar música
// pecas: buzzer 8; led 9 azul
// tocar(nota, tempos) acende o LED junto com cada nota
#define PINO_BUZZER 8                               // buzzer no pino 8
#define PINO_LED 9                                  // LED no pino 9
#define BATIDA 250                           // duração de um tempo (ms)

void tocar(int frequencia, int tempos) {            // toca uma nota por alguns tempos
  digitalWrite(PINO_LED, HIGH);                     // acende/liga PINO_LED
  tone(PINO_BUZZER, frequencia, tempos * BATIDA * 0.9);   // 90% do tempo soando: separa as notas
  delay(tempos * BATIDA);                           // espera o tempo calculado (ms)
  digitalWrite(PINO_LED, LOW);                      // apaga/desliga PINO_LED
}

void pausa(int tempos) {                            // silêncio por alguns tempos
  delay(tempos * BATIDA);                           // espera o tempo calculado (ms)
}

void setup() {                                      // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                        // PINO_LED como saída
}

void loop() {                                       // repete para sempre
  tocar(330, 1); tocar(330, 1); tocar(330, 2);      // mi mi mi
  tocar(330, 1); tocar(330, 1); tocar(330, 2);      // mi mi mi
  tocar(330, 1); tocar(392, 1); tocar(262, 1); tocar(294, 1); tocar(330, 4);   // mi sol dó ré mi
  pausa(4);                                         // pausa antes de repetir
}
