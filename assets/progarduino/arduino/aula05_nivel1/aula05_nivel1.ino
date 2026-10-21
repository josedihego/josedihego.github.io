// Aula 5 – Nível 1: Ler um botão
// Botão no pino 2 com o resistor interno de pull-up: solto = 1, apertado = 0
const int PINO_BOTAO = 2;               // pino do botão

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);    // entrada com resistor interno ligado ao 5 V
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  int estado = digitalRead(PINO_BOTAO); // lê 0 (LOW) ou 1 (HIGH)
  Serial.println(estado);               // aperte e veja virar 0
  delay(100);                           // espera 100 ms
}
