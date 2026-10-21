// Aula 22 – Nível 2: Nível do tanque na barra de LEDs
// Cada LED representa 20% do tanque
#define TRIG 9                                         // TRIG do HC-SR04 no pino 9
#define ECHO 10                                        // ECHO do HC-SR04 no pino 10
#define ALTURA 100.0                                   // constante ALTURA = 100.0

float nivel() {                                        // devolve o nível em %
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);      // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);     // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);                             // fim do pulso
  float vazio = pulseIn(ECHO, HIGH) * 0.0343 / 2;      // distância do sensor até a água (cm)
  return constrain((ALTURA - vazio) / ALTURA * 100, 0, 100);   // nível em %, limitado a 0..100
}

void setup() {                                         // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                               // TRIG como saída
  pinMode(ECHO, INPUT);                                // ECHO como entrada
  for (int p = 2; p <= 6; p++) pinMode(p, OUTPUT);     // pinos 2 a 6 como saída
}

void loop() {                                          // repete para sempre
  float n = nivel();                                   // mede o nível
  for (int i = 0; i < 5; i++) {                        // 5 voltas
    digitalWrite(2 + i, n >= (i + 1) * 20 - 10);       // acende a partir do meio de cada faixa
  }
  delay(300);                                          // espera 300 ms
}
