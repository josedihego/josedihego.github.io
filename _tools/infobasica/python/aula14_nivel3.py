# Aula 14 – Nível 3: Soma e fatorial de N
# teste: 6
n = int(input("N: "))                     # lê N
soma = 0                                  # acumulador de soma começa em 0
fatorial = 1                              # acumulador de produto começa em 1, não em 0
for numero in range(1, n + 1):            # de 1 até N (por isso n + 1)
    soma = soma + numero                  # soma o número
    fatorial = fatorial * numero          # multiplica o número
print("Soma:", soma, "| pela fórmula:", n * (n + 1) // 2)   # as duas devem ser iguais
print(f"{n}! =", fatorial)                # N fatorial
