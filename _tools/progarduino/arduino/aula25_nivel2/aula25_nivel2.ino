// Aula 25 – Nível 2: Melodia com vetores
// pecas: buzzer 8
// Dois vetores do mesmo tamanho: notas (Hz) e durações (ms)
#define PINO_BUZZER 8                          // buzzer no pino 8
const int NOTAS[] = {262, 294, 330, 349, 392, 392, 440, 392};   // frequências em Hz (dó, ré, mi...)
const int DURACAO[] = {300, 300, 300, 300, 400, 400, 300, 600};   // duração de cada nota (ms)
const int N = sizeof(NOTAS) / sizeof(NOTAS[0]);   // quantidade de notas

void setup() {                                 // roda uma vez, quando a placa liga
  for (int i = 0; i < N; i++) {                // percorre os N elementos
    tone(PINO_BUZZER, NOTAS[i], DURACAO[i]);   // a mesma posição nos dois vetores
    delay(DURACAO[i] * 1.2);                   // pequena pausa entre as notas
  }
}

void loop() {                                  // repete para sempre
}
