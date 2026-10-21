// Aula 20 – Nível 3: Sensor de estacionamento
// pecas: ultrassom 9 10; buzzer 8
// Bipes mais rápidos quanto mais perto; abaixo de 10 cm, som contínuo
#define TRIG 9                                        // TRIG do HC-SR04 no pino 9
#define ECHO 10                                       // ECHO do HC-SR04 no pino 10
#define PINO_BUZZER 8                                 // buzzer no pino 8

float medir() {                                       // devolve a distância em cm
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);     // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);    // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);                            // fim do pulso
  return pulseIn(ECHO, HIGH, 30000) * 0.0343 / 2;     // 30 ms de limite: sem eco devolve 0
}

void setup() {                                        // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                              // TRIG como saída
  pinMode(ECHO, INPUT);                               // ECHO como entrada
}

void loop() {                                         // repete para sempre
  float cm = medir();                                 // distância atual
  if (cm > 0 && cm < 10) {                            // muito perto
    tone(PINO_BUZZER, 1500);                          // som contínuo
    delay(100);                                       // espera 100 ms
  } else if (cm > 0 && cm < 60) {                     // pausa proporcional à distância
    tone(PINO_BUZZER, 1500, 60);                      // bipe curto de 60 ms
    delay(cm * 10);                                   // espera o tempo calculado (ms)
  } else {
    noTone(PINO_BUZZER);                              // silêncio
    delay(100);                                       // espera 100 ms
  }
}
