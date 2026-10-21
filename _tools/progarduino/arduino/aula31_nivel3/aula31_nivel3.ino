// Aula 31 – Nível 3: Memória livre
// pecas: 
// Mostra quanta RAM sobra; um vetor grande local consome memória enquanto a função roda
extern int __heap_start, *__brkval;            // símbolos do sistema AVR

int memoria_livre() {                          // bytes livres entre o heap e a pilha
  int topo;                                    // variável na pilha: marca o topo
  return (int)&topo - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);   // topo da pilha − fim do heap
}

void usa_vetor() {                             // função com um vetor local grande
  int grande[200];                             // 400 bytes na pilha
  for (int i = 0; i < 200; i++) grande[i] = i;   // usa o vetor (o compilador não pode descartá-lo)
  Serial.print(F("Dentro da função: "));       // envia o texto ao Monitor Serial
  Serial.println(memoria_livre());             // envia memoria_livre() ao Monitor Serial e quebra a linha
  Serial.println(grande[199]);                 // envia grande[199] ao Monitor Serial e quebra a linha
}

void setup() {                                 // roda uma vez, quando a placa liga
  Serial.begin(9600);                          // abre o Monitor Serial a 9600 baud
  Serial.print(F("Livre no início: "));        // envia o texto ao Monitor Serial
  Serial.println(memoria_livre());             // envia memoria_livre() ao Monitor Serial e quebra a linha
  usa_vetor();                                 // chama: a memória livre diminui lá dentro
  Serial.print(F("Depois: "));                 // envia o texto ao Monitor Serial
  Serial.println(memoria_livre());             // envia memoria_livre() ao Monitor Serial e quebra a linha
}

void loop() {                                  // repete para sempre
}
