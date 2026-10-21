// Aula 32 – Nível 1: Melodia numa matriz
// Cada linha da matriz é {nota, duração}
#define PINO_BUZZER 8                                      // buzzer no pino 8
const int MUSICA[][2] = {{262, 250}, {262, 250}, {294, 500}, {262, 500}, {349, 500}, {330, 1000}};   // cada linha: {nota em Hz, duração em ms}
const int N = sizeof(MUSICA) / sizeof(MUSICA[0]);          // quantidade de linhas

void setup() {                                             // roda uma vez, quando a placa liga
  for (int i = 0; i < N; i++) {                            // percorre os N elementos
    tone(PINO_BUZZER, MUSICA[i][0], MUSICA[i][1] * 0.9);   // coluna 0 = nota, coluna 1 = duração
    delay(MUSICA[i][1]);                                   // espera o tempo calculado (ms)
  }
}

void loop() {                                              // repete para sempre
}
