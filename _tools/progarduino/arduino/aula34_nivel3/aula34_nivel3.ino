// Aula 34 – Nível 3: Estação com comandos e struct
// pecas: ldr A0; pot A1; led 9 vermelho; buzzer 7
// Comandos: LIMITE n (temperatura de alarme), INTERVALO ms, STATUS
#include <Arduino.h>                            // funções do Arduino (pinMode, digitalWrite, delay...)
#define LED_QUENTE 9                            // LED de alarme de calor no pino 9
#define PINO_BUZZER 7                           // buzzer no pino 7

struct Config {                                 // configuração ajustável por comando
  float limite;                                 // declara limite (float)
  unsigned long intervalo;                      // declara intervalo (unsigned long)
};

Config cfg = {35.0, 1000};                      // limite 35 °C, uma medição por segundo
unsigned long ultimo = 0;                       // instante da última medição

void comandos() {                               // trata os comandos do Monitor Serial
  if (Serial.available() == 0) return;          // nada chegou: sai da função
  String linha = Serial.readStringUntil('\n');   // lê a linha até o Enter
  linha.trim();                                 // tira espaços e \r das pontas
  linha.toUpperCase();                          // aceita maiúsculas e minúsculas
  if (linha.startsWith("LIMITE ")) cfg.limite = linha.substring(7).toFloat();   // LIMITE n: novo limite de temperatura
  else if (linha.startsWith("INTERVALO ")) cfg.intervalo = linha.substring(10).toInt();   // INTERVALO ms: novo intervalo
  Serial.print("# limite="); Serial.print(cfg.limite, 1);   // envia o texto ao Monitor Serial
  Serial.print(" intervalo="); Serial.println(cfg.intervalo);   // envia o texto ao Monitor Serial
}

void setup() {                                  // roda uma vez, quando a placa liga
  pinMode(LED_QUENTE, OUTPUT);                  // LED_QUENTE como saída
  Serial.begin(9600);                           // abre o Monitor Serial a 9600 baud
  Serial.println("segundos,luz,temperatura");   // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                   // repete para sempre
  comandos();                                   // atende os comandos sem esperar a medição
  if (millis() - ultimo >= cfg.intervalo) {     // mede sem travar a leitura de comandos
    ultimo = millis();                          // marca o instante deste evento
    float temperatura = analogRead(A1) * 50.0 / 1023;   // potenciômetro simula 0 a 50 °C
    bool quente = temperatura > cfg.limite;     // compara com o limite configurado
    digitalWrite(LED_QUENTE, quente);           // LED_QUENTE recebe quente (verdadeiro acende, falso apaga)
    if (quente) tone(PINO_BUZZER, 1200, 100);   // bipe de alarme
    Serial.print(millis() / 1000); Serial.print(",");   // envia millis() / 1000); Serial.print(" ao Monitor Serial
    Serial.print(analogRead(A0));  Serial.print(",");   // envia analogRead(A0));  Serial.print(" ao Monitor Serial
    Serial.println(temperatura, 1);             // envia temperatura ao Monitor Serial e quebra a linha
  }
}
