// Aula 27 – Nível 2: Comandos LIGA e DESLIGA
// Controle por texto: LIGA, DESLIGA, ESTADO
#include <Arduino.h>                                // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 8                                  // LED no pino 8
bool aceso = false;                                 // estado do LED

void setup() {                                      // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                        // PINO_LED como saída
  Serial.begin(9600);                               // abre o Monitor Serial a 9600 baud
  Serial.println("Comandos: LIGA, DESLIGA, ESTADO");   // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                       // repete para sempre
  if (Serial.available() > 0) {                     // chegou algo pela serial?
    String cmd = Serial.readStringUntil('\n');      // lê o comando até o Enter
    cmd.trim();                                     // tira espaços e \r
    cmd.toUpperCase();                              // aceita liga, Liga, LIGA...
    if (cmd == "LIGA") aceso = true;                // comando LIGA
    else if (cmd == "DESLIGA") aceso = false;       // comando DESLIGA
    else if (cmd != "ESTADO") { Serial.println("Comando desconhecido"); return; }   // ESTADO só mostra; o resto é erro
    digitalWrite(PINO_LED, aceso);                  // PINO_LED recebe aceso (verdadeiro acende, falso apaga)
    Serial.println(aceso ? "LED aceso" : "LED apagado");   // envia aceso ? "LED aceso" : "LED apagado" ao Monitor Serial e quebra a linha
  }
}
