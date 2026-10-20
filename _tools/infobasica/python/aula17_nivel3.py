# Aula 17 – Nível 3: Soma 7 com dois dados
# teste: 
import random                                       # biblioteca de números aleatórios
lancamentos = 10000                                 # quantas vezes jogar os dois dados
setes = 0                                           # contador de somas iguais a 7
for vez in range(lancamentos):                      # repete 10000 vezes
    dado1 = random.randint(1, 6)                    # primeiro dado
    dado2 = random.randint(1, 6)                    # segundo dado
    if dado1 + dado2 == 7:                          # a soma deu 7?
        setes = setes + 1                           # conta
percentual = setes / lancamentos * 100              # percentual de setes
print(f"Soma 7 em {percentual:.1f}% dos lançamentos (teoria: 16,7%)")   # compara com a teoria
