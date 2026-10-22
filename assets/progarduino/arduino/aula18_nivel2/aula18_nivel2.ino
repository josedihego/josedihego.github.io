// Aula 18 – Nível 2: Primos no Monitor Serial
// Mostra os números primos até 200
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
  for (int n = 2; n <= 200; n++) {      // candidatos de 2 a 200
    bool primo = true;                  // supõe que é primo
    for (int d = 2; d * d <= n; d++) {   // testa divisores até a raiz de n
      if (n % d == 0) { primo = false; break; }   // achou divisor: não é primo
    }
    if (primo) {                        // mostra só os primos
      Serial.print(n);                  // envia n ao Monitor Serial
      Serial.print(" ");                // envia o texto ao Monitor Serial
    }
  }
  Serial.println();                     // quebra a linha
}

void loop() {                           // repete para sempre
}
