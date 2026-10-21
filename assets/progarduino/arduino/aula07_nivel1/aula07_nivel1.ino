// Aula 7 – Nível 1: Três faixas, três LEDs
// Potenciômetro baixo = verde, médio = amarelo, alto = vermelho
const int VERDE = 8, AMARELO = 9, VERMELHO = 10;   // pinos dos 3 LEDs

void setup() {                              // roda uma vez, quando a placa liga
  pinMode(VERDE, OUTPUT);                   // VERDE como saída
  pinMode(AMARELO, OUTPUT);                 // AMARELO como saída
  pinMode(VERMELHO, OUTPUT);                // VERMELHO como saída
}

void loop() {                               // repete para sempre
  int leitura = analogRead(A0);             // lê o A0 (0 a 1023)
  digitalWrite(VERDE, LOW);                 // apaga todos antes de decidir
  digitalWrite(AMARELO, LOW);               // apaga/desliga AMARELO
  digitalWrite(VERMELHO, LOW);              // apaga/desliga VERMELHO
  if (leitura < 341) {                      // primeiro terço
    digitalWrite(VERDE, HIGH);              // acende/liga VERDE
  } else if (leitura < 682) {               // segundo terço
    digitalWrite(AMARELO, HIGH);            // acende/liga AMARELO
  } else {                                  // último terço
    digitalWrite(VERMELHO, HIGH);           // acende/liga VERMELHO
  }
}
