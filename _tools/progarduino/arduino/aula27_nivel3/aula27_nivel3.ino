// Aula 27 – Nível 3: Comando com parâmetro
// pecas: led 8 vermelho; buzzer 7
// PISCA 5, BIP 880, BRILHO? -> separa o comando do número
#define PINO_LED 8                                      // LED no pino 8
#define PINO_BUZZER 7                                   // buzzer no pino 7

void setup() {                                          // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                            // PINO_LED como saída
  Serial.begin(9600);                                   // abre o Monitor Serial a 9600 baud
  Serial.println("Comandos: PISCA n, BIP freq");        // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                           // repete para sempre
  if (Serial.available() > 0) {                         // chegou algo pela serial?
    String linha = Serial.readStringUntil('\n');        // lê a linha até o Enter
    linha.trim();                                       // tira espaços e \r das pontas
    linha.toUpperCase();                                // aceita maiúsculas e minúsculas
    int espaco = linha.indexOf(' ');                    // posição do espaço
    String cmd = espaco < 0 ? linha : linha.substring(0, espaco);   // texto antes do espaço
    int valor = espaco < 0 ? 0 : linha.substring(espaco + 1).toInt();   // texto depois do espaço vira número
    if (cmd == "PISCA") {                               // comando PISCA n
      for (int i = 0; i < valor; i++) {                 // pisca 'valor' vezes
        digitalWrite(PINO_LED, HIGH); delay(200);       // acende/liga PINO_LED e espera 200 ms
        digitalWrite(PINO_LED, LOW);  delay(200);       // apaga/desliga PINO_LED e espera 200 ms
      }
      Serial.println("ok");                             // envia o texto ao Monitor Serial e quebra a linha
    } else if (cmd == "BIP") {                          // comando BIP frequência
      tone(PINO_BUZZER, valor, 300);                    // toca a frequência pedida por 300 ms
      Serial.println("ok");                             // envia o texto ao Monitor Serial e quebra a linha
    } else {
      Serial.println("Comando desconhecido");           // envia o texto ao Monitor Serial e quebra a linha
    }
  }
}
