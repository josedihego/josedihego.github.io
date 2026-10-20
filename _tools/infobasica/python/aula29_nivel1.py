# Aula 29 – Nível 1: Só os pares
# teste: 
numeros = [3, 8, 12, 5, 20, 7]     # lista original
pares = []                         # lista nova, vazia
for numero in numeros:             # percorre a original
    if numero % 2 == 0:            # é par?
        pares.append(numero)       # guarda na nova
print(pares)                       # [8, 12, 20]
