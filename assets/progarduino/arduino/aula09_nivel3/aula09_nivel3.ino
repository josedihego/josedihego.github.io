// Aula 9 – Nível 3: Cores com LED RGB
// LED RGB (cátodo comum): mistura vermelho, verde e azul com PWM
#define PINO_R 9                       // vermelho do LED RGB no pino 9
#define PINO_G 10                      // verde do LED RGB no pino 10
#define PINO_B 11                      // azul do LED RGB no pino 11

void cor(int r, int g, int b) {        // acende cada cor com a intensidade pedida (0 a 255)
  analogWrite(PINO_R, r);              // intensidade do vermelho
  analogWrite(PINO_G, g);              // intensidade do verde
  analogWrite(PINO_B, b);              // intensidade do azul
}

void setup() {                         // roda uma vez, quando a placa liga
  pinMode(PINO_R, OUTPUT);             // PINO_R como saída
  pinMode(PINO_G, OUTPUT);             // PINO_G como saída
  pinMode(PINO_B, OUTPUT);             // PINO_B como saída
}

void loop() {                          // repete para sempre
  cor(255, 0, 0);   delay(800);        // vermelho
  cor(0, 255, 0);   delay(800);        // verde
  cor(0, 0, 255);   delay(800);        // azul
  cor(255, 120, 0); delay(800);        // laranja
  cor(128, 0, 128); delay(800);        // roxo
}
