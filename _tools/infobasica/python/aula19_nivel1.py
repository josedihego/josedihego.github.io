# Aula 19 – Nível 1: Múltiplos de 3 ou de 7
# teste: 
for numero in range(1, 101):                # percorre de 1 a 100
    if numero % 3 == 0 or numero % 7 == 0:  # resto zero = divisível
        print(numero, end=" ")              # end=" " continua na mesma linha
print()                                     # quebra a linha no final
