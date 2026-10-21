// Aula 16 – Nível 1: Contar toques
// Conta quantas vezes o botão foi apertado (detecta a mudança de solto para apertado)
#define PINO_BOTAO 2                          // botão no pino 2
int toques = 0;                               // contador de toques
int anterior = HIGH;                          // estado na volta anterior do loop

void setup() {                                // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);          // PINO_BOTAO como entrada com pull-up interno
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
}

void loop() {                                 // repete para sempre
  int atual = digitalRead(PINO_BOTAO);        // estado agora
  if (anterior == HIGH && atual == LOW) {     // borda de descida: acabou de apertar
    toques++;                                 // conta mais um toque
    Serial.println(toques);                   // envia toques ao Monitor Serial e quebra a linha
  }
  anterior = atual;                           // guarda para a próxima volta
}
