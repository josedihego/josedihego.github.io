// Aula 33 – Nível 1: Um struct para um LED
// pecas: led 8 vermelho
// O struct junta tudo o que descreve um LED que pisca sozinho
struct Led {                                   // tudo o que descreve um LED que pisca sozinho
  int pino;                                    // declara pino (int)
  unsigned long periodo;                       // declara periodo (unsigned long)
  unsigned long ultimo;                        // declara ultimo (unsigned long)
  bool aceso;                                  // declara aceso (bool)
};

Led alerta = {8, 400, 0, false};               // inicializa os campos na ordem

void setup() {                                 // roda uma vez, quando a placa liga
  pinMode(alerta.pino, OUTPUT);                // . acessa um campo
}

void loop() {                                  // repete para sempre
  if (millis() - alerta.ultimo >= alerta.periodo) {   // passou o período deste LED?
    alerta.ultimo = millis();                  // marca a troca
    alerta.aceso = !alerta.aceso;              // inverte
    digitalWrite(alerta.pino, alerta.aceso);   // alerta.pino recebe alerta.aceso (verdadeiro acende, falso apaga)
  }
}
