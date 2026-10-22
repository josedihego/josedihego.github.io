// Aula 7 – Nível 3: Comandos por letra com switch
// pecas: led 8 vermelho
// No Monitor Serial: L liga, D desliga, P pisca 3 vezes
#include <Arduino.h>                            // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINO_LED = 8;                         // pino do LED (com resistor de 220 ohms)

void setup() {                                  // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                    // PINO_LED como saída
  Serial.begin(9600);                           // abre o Monitor Serial a 9600 baud
  Serial.println("Comandos: L, D, P");          // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                   // repete para sempre
  if (Serial.available() > 0) {                 // chegou algo pela serial?
    char comando = Serial.read();               // lê um caractere
    switch (comando) {                          // escolhe pelo caractere
      case 'L': case 'l':                       // aceita maiúscula e minúscula
        digitalWrite(PINO_LED, HIGH);           // acende/liga PINO_LED
        Serial.println("Ligado");               // envia o texto ao Monitor Serial e quebra a linha
        break;                                  // sai do switch/laço
      case 'D': case 'd':                       // D ou d: desliga
        digitalWrite(PINO_LED, LOW);            // apaga/desliga PINO_LED
        Serial.println("Desligado");            // envia o texto ao Monitor Serial e quebra a linha
        break;                                  // sai do switch/laço
      case 'P': case 'p':                       // P ou p: pisca
        for (int i = 0; i < 3; i++) {           // 3 voltas
          digitalWrite(PINO_LED, HIGH); delay(200);   // acende/liga PINO_LED e espera 200 ms
          digitalWrite(PINO_LED, LOW);  delay(200);   // apaga/desliga PINO_LED e espera 200 ms
        }
        Serial.println("Piscou");               // envia o texto ao Monitor Serial e quebra a linha
        break;                                  // sai do switch/laço
      default:                                  // Enter e outros caracteres são ignorados
        break;                                  // sai do switch/laço
    }
  }
}
