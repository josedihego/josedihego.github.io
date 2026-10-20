# Aula 17 – Nível 2: Mil lançamentos de moeda
# teste: 
import random                                  # biblioteca de números aleatórios
lancamentos = 1000                             # quantas vezes a moeda será lançada
caras = 0                                      # contador de caras
for vez in range(lancamentos):                 # repete 1000 vezes
    moeda = random.randint(0, 1)               # sorteia 0 (coroa) ou 1 (cara)
    if moeda == 1:                             # saiu cara?
        caras = caras + 1                      # conta mais uma cara
percentual = caras / lancamentos * 100         # percentual de caras
print(f"Caras: {caras} ({percentual:.1f}%)")   # deve ficar perto de 50%
