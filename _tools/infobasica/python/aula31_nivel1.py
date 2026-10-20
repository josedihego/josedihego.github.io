# Aula 31 – Nível 1: Variável local
# teste: 
def dobro(numero):            # numero só existe dentro da função
    resultado = numero * 2    # resultado também é local
    return resultado          # devolve o valor
x = 5                         # variável do programa principal
print(dobro(x))               # 10
# print(resultado)            # se tirar o #, dá erro: resultado não existe aqui fora
