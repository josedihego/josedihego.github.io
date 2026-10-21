// Aula 21 – Nível 2: Calibração automática
// Nos primeiros 5 s, cubra e descubra o sensor: a placa aprende o mínimo e o máximo
#define PINO_LED 9                               // LED no pino 9
int minimo = 1023, maximo = 0;                   // começam invertidos: a primeira leitura corrige

void setup() {                                   // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                     // PINO_LED como saída
  Serial.begin(9600);                            // abre o Monitor Serial a 9600 baud
  digitalWrite(PINO_LED, HIGH);                  // LED aceso = calibrando
  while (millis() < 5000) {                      // calibra durante os primeiros 5 s
    int v = analogRead(A0);                      // uma leitura
    if (v < minimo) minimo = v;                  // guarda a menor
    if (v > maximo) maximo = v;                  // guarda a maior
  }
  digitalWrite(PINO_LED, LOW);                   // apaga/desliga PINO_LED
  Serial.print("Calibrado: ");                   // envia o texto ao Monitor Serial
  Serial.print(minimo);                          // envia minimo ao Monitor Serial
  Serial.print(" a ");                           // envia o texto ao Monitor Serial
  Serial.println(maximo);                        // envia maximo ao Monitor Serial e quebra a linha
}

void loop() {                                    // repete para sempre
  int brilho = map(analogRead(A0), minimo, maximo, 0, 255);   // faixa calibrada → 0 a 255
  analogWrite(PINO_LED, constrain(brilho, 0, 255));   // mais escuro, mais brilho
  delay(20);                                     // espera 20 ms
}
