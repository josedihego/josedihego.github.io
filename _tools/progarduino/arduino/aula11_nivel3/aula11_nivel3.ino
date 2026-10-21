// Aula 11 – Nível 3: Simulado: semáforo de nível
// pecas: pot A0; led 8 verde; led 9 amarelo; led 10 vermelho
// Simulado: nível de 0 a 100% no Serial e no semáforo (até 50 verde, até 80 amarelo, acima vermelho)
#define VERDE 8                         // LED verde no pino 8
#define AMARELO 9                       // LED amarelo no pino 9
#define VERMELHO 10                     // LED vermelho no pino 10

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(VERDE, OUTPUT);               // VERDE como saída
  pinMode(AMARELO, OUTPUT);             // AMARELO como saída
  pinMode(VERMELHO, OUTPUT);            // VERMELHO como saída
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  int nivel = map(analogRead(A0), 0, 1023, 0, 100);   // converte a leitura em 0 a 100%
  Serial.print(nivel);                  // envia nivel ao Monitor Serial
  Serial.println("%");                  // envia o texto ao Monitor Serial e quebra a linha
  digitalWrite(VERDE, nivel <= 50);     // VERDE recebe nivel <= 50 (verdadeiro acende, falso apaga)
  digitalWrite(AMARELO, nivel > 50 && nivel <= 80);   // AMARELO recebe nivel > 50 && nivel <= 80 (verdadeiro acende, falso apaga)
  digitalWrite(VERMELHO, nivel > 80);   // VERMELHO recebe nivel > 80 (verdadeiro acende, falso apaga)
  delay(200);                           // espera 200 ms
}
