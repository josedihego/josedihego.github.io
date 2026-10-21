// Aula 14 – Nível 3: Mínimo, máximo e média de 50 leituras
// pecas: pot A0
// A cada 50 leituras mostra o mínimo, o máximo e a média
void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  int minimo = 1023, maximo = 0;        // começam invertidos: a primeira leitura corrige
  long soma = 0;                        // long: a soma de muitas leituras passa de 32767
  for (int i = 0; i < 50; i++) {        // 50 leituras
    int v = analogRead(A0);             // uma leitura
    if (v < minimo) minimo = v;         // guarda a menor
    if (v > maximo) maximo = v;         // guarda a maior
    soma += v;                          // acumula
    delay(10);                          // espera 10 ms
  }
  Serial.print("min ");                 // envia o texto ao Monitor Serial
  Serial.print(minimo);                 // envia minimo ao Monitor Serial
  Serial.print("  max ");               // envia o texto ao Monitor Serial
  Serial.print(maximo);                 // envia maximo ao Monitor Serial
  Serial.print("  média ");             // envia o texto ao Monitor Serial
  Serial.println(soma / 50.0, 1);       // envia soma / 50.0 ao Monitor Serial e quebra a linha
}
