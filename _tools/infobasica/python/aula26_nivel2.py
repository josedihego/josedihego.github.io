# Aula 26 – Nível 2: Lista de colegas
# teste: Ana; Bia; Caio; Davi; Eva
nomes = []                                         # lista vazia
for posicao in range(5):                           # repete 5 vezes
    nome = input(f"Nome do colega {posicao + 1}: ")  # lê um nome
    nomes.append(nome)                             # append coloca no fim da lista
print("Lista:", nomes)                             # mostra a lista inteira
print("Primeiro:", nomes[0])                       # índice 0 = primeiro elemento
print("Último:", nomes[-1])                        # índice -1 = último elemento
print("Quantidade:", len(nomes))                   # len: número de elementos
for indice in range(len(nomes) - 1, -1, -1):       # índices de trás para frente
    print(nomes[indice])                           # mostra em ordem inversa
