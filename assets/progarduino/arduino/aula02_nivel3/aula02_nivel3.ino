// Aula 2 – Nível 3: Tipos no Arduino e estouro do int
// No Arduino Uno o int tem só 2 bytes: passa de 32767 e volta para -32768
int pequeno = 32760;                          // perto do limite
long grande = 32760;                          // long tem 4 bytes

void setup() {                                // roda uma vez, quando a placa liga
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
  Serial.print("sizeof(int) = ");             // envia o texto ao Monitor Serial
  Serial.println(sizeof(int));                // 2 no Uno (4 no computador)
  Serial.print("sizeof(long) = ");            // envia o texto ao Monitor Serial
  Serial.println(sizeof(long));               // 4
}

void loop() {                                 // repete para sempre
  Serial.print("int: ");                      // envia o texto ao Monitor Serial
  Serial.print(pequeno);                      // envia pequeno ao Monitor Serial
  Serial.print("   long: ");                  // envia o texto ao Monitor Serial
  Serial.println(grande);                     // envia grande ao Monitor Serial e quebra a linha
  pequeno = pequeno + 1;                      // vai estourar em 32767 + 1
  grande = grande + 1;                        // continua crescendo
  delay(300);                                 // espera 300 ms
}
