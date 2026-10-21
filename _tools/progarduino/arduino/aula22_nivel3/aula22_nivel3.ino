// Aula 22 – Nível 3: Bomba automática com histerese
// pecas: ultrassom 9 10; led 7 azul; buzzer 8
// LED azul = bomba. Liga abaixo de 30% e desliga acima de 90%; alarme abaixo de 10%
#define TRIG 9                                 // TRIG do HC-SR04 no pino 9
#define ECHO 10                                // ECHO do HC-SR04 no pino 10
#define BOMBA 7                                // bomba (LED azul) no pino 7
#define PINO_BUZZER 8                          // buzzer no pino 8
#define ALTURA 100.0                           // constante ALTURA = 100.0
bool ligada = false;                           // estado da bomba

float nivel() {                                // devolve o nível do tanque em %
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);   // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);   // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);                     // fim do pulso
  float vazio = pulseIn(ECHO, HIGH) * 0.0343 / 2;   // distância do sensor até a água (cm)
  return constrain((ALTURA - vazio) / ALTURA * 100, 0, 100);   // nível em %, limitado a 0..100
}

void setup() {                                 // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                       // TRIG como saída
  pinMode(ECHO, INPUT);                        // ECHO como entrada
  pinMode(BOMBA, OUTPUT);                      // BOMBA como saída
  Serial.begin(9600);                          // abre o Monitor Serial a 9600 baud
}

void loop() {                                  // repete para sempre
  float n = nivel();                           // mede o nível
  if (n < 30) ligada = true;                   // histerese: liga só bem baixo
  else if (n > 90) ligada = false;             // e desliga só bem alto
  digitalWrite(BOMBA, ligada);                 // BOMBA recebe ligada (verdadeiro acende, falso apaga)
  if (n < 10) tone(PINO_BUZZER, 2000, 100);    // alarme de tanque quase vazio
  Serial.print(n, 0);                          // envia n ao Monitor Serial
  Serial.println(ligada ? "%  bomba LIGADA" : "%  bomba desligada");   // envia ligada ? "%  bomba LIGADA" : "%  bomba desligada" ao Monitor Serial e quebra a linha
  delay(500);                                  // espera 500 ms
}
