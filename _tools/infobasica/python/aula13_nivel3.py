# Aula 13 – Nível 3: Tabuada
# teste: 7
numero = int(input("Tabuada do: "))                         # lê o número
for multiplicador in range(1, 11):                          # de 1 a 10
    resultado = numero * multiplicador                      # calcula a linha da tabuada
    print(f"{numero} x {multiplicador} = {resultado}")      # mostra no formato 7 x 3 = 21
