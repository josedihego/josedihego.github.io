# Aula 31 – Nível 3: Jogo refatorado em funções
# teste: 1..100
import random                                     # para sortear
def ler_palpite():                                # cada tarefa vira uma função
    return int(input("Seu palpite (1 a 100): "))  # lê e devolve o palpite
def dar_dica(palpite, secreto):                   # decide a mensagem
    if palpite < secreto:   # palpite baixo?
        return "MAIOR"                            # o secreto é maior
    if palpite > secreto:   # palpite alto?
        return "MENOR"                            # o secreto é menor
    return "ACERTOU"                              # nem maior nem menor
def jogar_partida():                              # uma partida inteira
    secreto = random.randint(1, 100)              # variável local da partida
    tentativas = 0   # contador da partida
    dica = ""   # ainda não há dica
    while dica != "ACERTOU":                      # repete até acertar
        palpite = ler_palpite()                   # usa a primeira função
        tentativas = tentativas + 1   # conta a tentativa
        dica = dar_dica(palpite, secreto)         # usa a segunda função
        print(dica)   # mostra MAIOR, MENOR ou ACERTOU
    return tentativas                             # devolve quantas tentativas
total = jogar_partida()                           # o programa principal fica curto
print("Tentativas:", total)   # resultado da partida
