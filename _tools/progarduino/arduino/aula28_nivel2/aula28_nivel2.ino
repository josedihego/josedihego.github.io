// Aula 28 – Nível 2: Função que mede a distância
// pecas: ultrassom 9 10
// A função esconde os detalhes do sensor e devolve centímetros
#define TRIG 9                               // TRIG do HC-SR04 no pino 9
#define ECHO 10                              // ECHO do HC-SR04 no pino 10

float distancia_cm() {                       // devolve um float
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);   // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);   // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);                   // fim do pulso
  return pulseIn(ECHO, HIGH, 30000) * 0.0343 / 2;   // eco → cm (sem eco em 30 ms devolve 0)
}

void setup() {                               // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                     // TRIG como saída
  pinMode(ECHO, INPUT);                      // ECHO como entrada
  Serial.begin(9600);                        // abre o Monitor Serial a 9600 baud
}

void loop() {                                // repete para sempre
  Serial.println(distancia_cm(), 1);         // o loop fica curto e fácil de ler
  delay(300);                                // espera 300 ms
}
