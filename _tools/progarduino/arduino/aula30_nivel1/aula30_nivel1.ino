// Aula 30 – Nível 1: Endereços na memória do Arduino
// pecas: 
// Variáveis têm endereços; no Uno eles cabem em 2 KB de RAM
int tensao = 5;                               // variável comum
int *p = &tensao;                             // p guarda o endereço de tensao

void setup() {                                // roda uma vez, quando a placa liga
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
  Serial.print("Endereço de tensao: 0x");     // envia o texto ao Monitor Serial
  Serial.println((unsigned int)p, HEX);       // endereço em hexadecimal
  Serial.print("*p = ");                      // envia o texto ao Monitor Serial
  Serial.println(*p);                         // envia *p ao Monitor Serial e quebra a linha
  *p = 12;                                    // altera tensao pelo ponteiro
  Serial.print("tensao agora = ");            // envia o texto ao Monitor Serial
  Serial.println(tensao);                     // envia tensao ao Monitor Serial e quebra a linha
}

void loop() {                                 // repete para sempre
}
