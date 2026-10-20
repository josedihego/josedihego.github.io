# Aula 19 – Nível 3: MDC pelo algoritmo de Euclides
# teste: 48; 36
numero1 = int(input("Primeiro número: "))   # lê os dois números
numero2 = int(input("Segundo número: "))   # segundo número
a = numero1                                 # cópias para não perder os originais
b = numero2   # cópia do segundo número
while b != 0:                               # repete até o resto ser zero
    resto = a % b                           # resto da divisão
    a = b                                   # o divisor vira dividendo
    b = resto                               # o resto vira divisor
print(f"MDC({numero1}, {numero2}) = {a}")   # o último divisor é o MDC
