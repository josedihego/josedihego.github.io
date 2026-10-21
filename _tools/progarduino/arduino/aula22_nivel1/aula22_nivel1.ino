// Aula 22 – Nível 1: Nível do tanque em %
// pecas: ultrassom 9 10
// Sensor no alto de um tanque de 100 cm: quanto mais perto a água, mais cheio
#define TRIG 9                                        // TRIG do HC-SR04 no pino 9
#define ECHO 10                                       // ECHO do HC-SR04 no pino 10
#define ALTURA 100.0                                  // altura do tanque em cm

void setup() {                                        // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                              // TRIG como saída
  pinMode(ECHO, INPUT);                               // ECHO como entrada
  Serial.begin(9600);                                 // abre o Monitor Serial a 9600 baud
}

void loop() {                                         // repete para sempre
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);     // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);    // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);                            // fim do pulso
  float vazio = pulseIn(ECHO, HIGH) * 0.0343 / 2;     // distância até a água
  float nivel = constrain((ALTURA - vazio) / ALTURA * 100, 0, 100);   // nível em %, limitado a 0..100
  Serial.print("Nível: ");                            // envia o texto ao Monitor Serial
  Serial.print(nivel, 0);                             // envia nivel ao Monitor Serial
  Serial.println("%");                                // envia o texto ao Monitor Serial e quebra a linha
  delay(500);                                         // espera 500 ms
}
