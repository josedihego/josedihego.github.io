// Aula 33 – Nível 3: Struct de estatísticas
// pecas: pot A0
// Um struct acumula mínimo, máximo e média de uma série de leituras
struct Estatistica {                           // acumula uma série de leituras
  int minimo, maximo;                          // extremos
  long soma;                                   // declara soma (long)
  int n;                                       // declara n (int)
};

void zerar(Estatistica *e) {                   // ponteiro para struct: -> acessa o campo
  e->minimo = 1023; e->maximo = 0; e->soma = 0; e->n = 0;   // valores iniciais
}

void registrar(Estatistica *e, int valor) {    // inclui uma leitura nas estatísticas
  if (valor < e->minimo) e->minimo = valor;    // novo mínimo
  if (valor > e->maximo) e->maximo = valor;    // novo máximo
  e->soma += valor;                            // acumula
  e->n++;                                      // conta a leitura
}

Estatistica est;                               // variável do tipo struct

void setup() {                                 // roda uma vez, quando a placa liga
  Serial.begin(9600);                          // abre o Monitor Serial a 9600 baud
  zerar(&est);                                 // prepara para um novo bloco de leituras
}

void loop() {                                  // repete para sempre
  registrar(&est, analogRead(A0));             // registra uma leitura
  if (est.n == 100) {                          // a cada 100 leituras, relatório
    Serial.print("min "); Serial.print(est.minimo);   // envia o texto ao Monitor Serial
    Serial.print(" max "); Serial.print(est.maximo);   // envia o texto ao Monitor Serial
    Serial.print(" média "); Serial.println(est.soma / est.n);   // envia o texto ao Monitor Serial
    zerar(&est);                               // prepara para um novo bloco de leituras
  }
  delay(10);                                   // espera 10 ms
}
