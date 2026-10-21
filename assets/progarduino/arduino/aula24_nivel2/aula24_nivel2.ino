// Aula 24 – Nível 2: Revisão: contador de toques com limite
// Revisão: depois de 5 toques o LED acende e a contagem recomeça
#define PINO_BOTAO 2                    // botão no pino 2
#define PINO_LED 8                      // LED no pino 8
int toques = 0;                         // contador de toques
int anterior = HIGH;                    // estado na volta anterior (começa solto)

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);    // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);            // PINO_LED como saída
}

void loop() {                           // repete para sempre
  int atual = digitalRead(PINO_BOTAO);   // estado agora
  if (anterior == HIGH && atual == LOW) {   // acabou de apertar
    toques++;                           // conta mais um toque
    delay(30);                          // espera 30 ms
    if (toques == 5) {                  // chegou a 5 toques
      digitalWrite(PINO_LED, HIGH);     // acende/liga PINO_LED
      delay(1000);                      // espera 1000 ms
      digitalWrite(PINO_LED, LOW);      // apaga/desliga PINO_LED
      toques = 0;                       // recomeça a contagem
    }
  }
  anterior = atual;                     // guarda o estado para a próxima volta
}
