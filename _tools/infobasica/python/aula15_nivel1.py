# Aula 15 – Nível 1: Contar os pares
# teste: 
pares = 0                           # contador começa em zero
for numero in range(1, 51):         # de 1 a 50
    if numero % 2 == 0:             # é par?
        pares = pares + 1           # conta mais um
print("Pares entre 1 e 50:", pares) # 25
