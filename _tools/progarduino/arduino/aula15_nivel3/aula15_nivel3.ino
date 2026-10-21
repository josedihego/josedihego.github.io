// Aula 15 – Nível 3: Quanto tempo o botão ficou apertado?
// pecas: botao 2
// Mede em milissegundos quanto tempo o botão ficou apertado
#define PINO_BOTAO 2                                    // botão no pino 2

void setup() {                                          // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);                    // PINO_BOTAO como entrada com pull-up interno
  Serial.begin(9600);                                   // abre o Monitor Serial a 9600 baud
}

void loop() {                                           // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {                 // começou a apertar
    unsigned long inicio = millis();                    // millis: ms desde que a placa ligou
    while (digitalRead(PINO_BOTAO) == LOW) {            // espera soltar
    }
    unsigned long duracao = millis() - inicio;          // tempo apertado em ms
    Serial.print("Apertado por ");                      // envia o texto ao Monitor Serial
    Serial.print(duracao);                              // envia duracao ao Monitor Serial
    Serial.println(" ms");                              // envia o texto ao Monitor Serial e quebra a linha
    delay(30);                                          // ignora o ruído ao soltar
  }
}
