// Aula 27 – Nível 1: Ler uma linha do Monitor Serial
// Lê uma linha inteira (até o Enter) e responde
void setup() {                                      // roda uma vez, quando a placa liga
  Serial.begin(9600);                               // abre o Monitor Serial a 9600 baud
  Serial.println("Escreva seu nome:");              // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                       // repete para sempre
  if (Serial.available() > 0) {                     // chegou algo pela serial?
    String nome = Serial.readStringUntil('\n');     // lê até o Enter
    nome.trim();                                    // tira espaços e \r das pontas
    Serial.print("Olá, ");                          // envia o texto ao Monitor Serial
    Serial.print(nome);                             // envia nome ao Monitor Serial
    Serial.print("! Seu nome tem ");                // envia o texto ao Monitor Serial
    Serial.print(nome.length());                    // envia nome.length() ao Monitor Serial
    Serial.println(" letras.");                     // envia o texto ao Monitor Serial e quebra a linha
  }
}
