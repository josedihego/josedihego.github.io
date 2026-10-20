# Aula 15 – Nível 3: Notas da turma
# teste: 4; 8; 5.5; 9; 6
quantidade = int(input("Quantos estudantes? "))        # tamanho da turma
soma = 0                                               # acumulador das notas
aprovados = 0                                          # contador de aprovados
maior = -1                                             # menor que qualquer nota possível
for estudante in range(1, quantidade + 1):             # repete para cada estudante
    nota = float(input(f"Nota do estudante {estudante}: "))   # lê a nota
    soma = soma + nota                                 # acumula
    if nota >= 7:                                      # aprovado?
        aprovados = aprovados + 1                      # conta
    if nota > maior:                                   # nota maior que a maior até agora?
        maior = nota                                   # guarda
media = soma / quantidade                              # média da turma
percentual = aprovados / quantidade * 100              # percentual de aprovados
print(f"Média: {media:.2f} | Maior: {maior} | Aprovados: {percentual:.0f}%")   # resumo
