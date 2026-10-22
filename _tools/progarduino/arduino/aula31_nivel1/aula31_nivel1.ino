// Aula 31 – Nível 1: Quanto ocupa cada tipo
// pecas: 
// sizeof no Arduino e a macro F(), que guarda textos na memória de programa (flash)
#include <Arduino.h>                                                // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                                      // roda uma vez, quando a placa liga
  Serial.begin(9600);                                               // abre o Monitor Serial a 9600 baud
  Serial.print(F("int: "));       Serial.println(sizeof(int));      // envia o texto ao Monitor Serial
  Serial.print(F("long: "));      Serial.println(sizeof(long));     // envia o texto ao Monitor Serial
  Serial.print(F("float: "));     Serial.println(sizeof(float));    // envia o texto ao Monitor Serial
  Serial.print(F("double: "));    Serial.println(sizeof(double));   // no Uno, double = float (4 bytes)
  Serial.print(F("ponteiro: "));  Serial.println(sizeof(int *));    // endereços de 2 bytes
}

void loop() {                                                       // repete para sempre
}
