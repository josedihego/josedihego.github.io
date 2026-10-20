# Aula 13 – Nível 2: Faixas e contagem regressiva
# teste: 
for numero in range(1, 11):        # numero vai de 1 até 10 (o 11 não entra)
    print(numero)                  # este bloco repete 10 vezes
for numero in range(0, 101, 5):    # de 0 a 100, de 5 em 5
    print(numero, end=" ")         # end=" " continua na mesma linha
print()                            # quebra a linha
for contagem in range(10, 0, -1):  # passo negativo: conta de 10 até 1
    print(contagem)                # mostra o número atual
print("Lançar!")                   # fora do laço: executa uma vez só
