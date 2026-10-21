// Aula 16 – Nível 2: Contar toques sem repique
// Debounce: só aceita um novo toque 50 ms depois do anterior
#define PINO_BOTAO 2                              // botão no pino 2
int toques = 0;                                   // contador de toques
int anterior = HIGH;                              // estado na volta anterior (começa solto)
unsigned long ultimo = 0;                         // instante do último toque aceito

void setup() {                                    // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);              // PINO_BOTAO como entrada com pull-up interno
  Serial.begin(9600);                             // abre o Monitor Serial a 9600 baud
}

void loop() {                                     // repete para sempre
  int atual = digitalRead(PINO_BOTAO);            // estado agora
  if (anterior == HIGH && atual == LOW && millis() - ultimo > 50) {   // apertou agora e já passaram 50 ms
    toques++;                                     // conta mais um toque
    ultimo = millis();                            // marca o instante deste evento
    Serial.print("Toques: ");                     // envia o texto ao Monitor Serial
    Serial.println(toques);                       // envia toques ao Monitor Serial e quebra a linha
  }
  anterior = atual;                               // guarda o estado para a próxima volta
}
