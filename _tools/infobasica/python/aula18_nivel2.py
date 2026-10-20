# Aula 18 – Nível 2: Adivinhação com dicas
# teste: 1..100
import random                                         # para sortear o número secreto
secreto = random.randint(1, 100)                      # número que o jogador deve adivinhar
tentativas = 0                                        # contador de tentativas
palpite = 0                                           # começa com um valor que nunca é o secreto
while palpite != secreto:                             # repete até acertar
    palpite = int(input("Seu palpite (1 a 100): "))   # lê o palpite
    tentativas = tentativas + 1                       # conta a tentativa
    if palpite < secreto:                             # palpite abaixo do secreto
        print("O número secreto é MAIOR")             # dá a dica
    elif palpite > secreto:                           # palpite acima do secreto
        print("O número secreto é MENOR")             # dá a dica
print(f"Acertou em {tentativas} tentativas!")         # fora do laço: o jogo acabou
