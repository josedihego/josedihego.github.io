# Aula 18 – Nível 1: Um palpite só
# teste: 5
import random                                      # para sortear
secreto = random.randint(1, 10)                    # número secreto de 1 a 10
palpite = int(input("Adivinhe (1 a 10): "))        # um único palpite
if palpite == secreto:                             # acertou?
    print("Acertou!")   # palpite igual ao número secreto
else:                                              # errou
    print("Errou! O número era", secreto)          # revela o número
