# Aula 10 – Nível 2: Conceito A, B, C ou D
# teste: 8.5
nota = float(input("Nota (0 a 10): "))  # lê a nota
if nota < 0 or nota > 10:               # primeiro, descarta valores inválidos
    print("Nota inválida")              # avisa o usuário
elif nota >= 9:                         # elif = "senão, se": só é testado se o anterior for falso
    print("Conceito A")                 # nota entre 9 e 10
elif nota >= 7:                         # aqui já sabemos que a nota é menor que 9
    print("Conceito B")                 # nota entre 7 e 9
elif nota >= 5:                         # e aqui, que é menor que 7
    print("Conceito C")                 # nota entre 5 e 7
else:                                   # nenhuma condição acima foi verdadeira
    print("Conceito D")                 # nota abaixo de 5
