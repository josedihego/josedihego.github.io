// Aula 10 – Nível 3: Termômetro simulado com alarme
// pecas: pot A0; led 8 verde; led 9 amarelo; led 10 vermelho; buzzer 7
// O potenciômetro simula um sensor de 0 a 100 °C: verde, amarelo ou vermelho com alarme
#define VERDE 8                                           // LED verde no pino 8
#define AMARELO 9                                         // LED amarelo no pino 9
#define VERMELHO 10                                       // LED vermelho no pino 10
#define PINO_BUZZER 7                                     // buzzer no pino 7

void setup() {                                            // roda uma vez, quando a placa liga
  pinMode(VERDE, OUTPUT);                                 // VERDE como saída
  pinMode(AMARELO, OUTPUT);                               // AMARELO como saída
  pinMode(VERMELHO, OUTPUT);                              // VERMELHO como saída
  Serial.begin(9600);                                     // abre o Monitor Serial a 9600 baud
}

void loop() {                                             // repete para sempre
  float temperatura = analogRead(A0) * 100.0 / 1023.0;   // 0 a 100 °C
  Serial.print(temperatura, 1);                           // envia temperatura ao Monitor Serial
  Serial.println(" °C");                                  // envia o texto ao Monitor Serial e quebra a linha
  digitalWrite(VERDE, temperatura < 40);                  // cada LED recebe o resultado de uma comparação
  digitalWrite(AMARELO, temperatura >= 40 && temperatura < 70);   // AMARELO recebe temperatura >= 40 && temperatura < 70 (verdadeiro acende, falso apaga)
  digitalWrite(VERMELHO, temperatura >= 70);              // VERMELHO recebe temperatura >= 70 (verdadeiro acende, falso apaga)
  if (temperatura >= 70) {                                // faixa de alarme
    tone(PINO_BUZZER, 1000, 100);                         // bip curto enquanto estiver quente
  }
  delay(300);                                             // espera 300 ms
}
