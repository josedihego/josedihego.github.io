# Aula 18 – Nível 3: No máximo 7 tentativas
# teste: 50; 25; 12; 6; 3; 2; 1
import random                                         # para sortear
secreto = random.randint(1, 100)                      # número secreto
limite = 7                                            # tentativas permitidas
acertou = False                                       # ainda não acertou
for tentativa in range(1, limite + 1):                # no máximo 7 voltas
    palpite = int(input(f"Tentativa {tentativa}/{limite}: "))   # lê o palpite
    if palpite == secreto:                            # acertou?
        acertou = True                                # marca
        break                                         # sai do laço antes do fim
    elif palpite < secreto:                           # palpite baixo
        print("O número secreto é MAIOR")   # dica para subir
    else:                                             # palpite alto
        print("O número secreto é MENOR")   # dica para descer
if acertou:                                           # depois do laço, o resultado
    print(f"Acertou na tentativa {tentativa}!")   # tentativa guarda a volta em que o laço parou
else:   # caso contrário
    print("Acabaram as tentativas. O número era", secreto)   # revela o número secreto
