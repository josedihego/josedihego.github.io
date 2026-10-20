# Aula 16 – Nível 3: Média até digitar negativo
# teste: 8; 12; 6; -1
soma = 0                                                # acumulador
quantidade = 0                                          # contador de notas válidas
nota = float(input("Nota (negativo para terminar): "))  # primeira leitura, antes do laço
while nota >= 0:                                        # negativo encerra
    if nota <= 10:                                      # nota válida?
        soma = soma + nota                              # acumula
        quantidade = quantidade + 1                     # conta
    else:                                               # acima de 10
        print("Nota acima de 10 ignorada")              # avisa
    nota = float(input("Nota (negativo para terminar): "))   # lê a próxima no fim do laço
if quantidade > 0:                                      # evita dividir por zero
    print(f"Média de {quantidade} notas: {soma / quantidade:.2f}")   # média só das notas válidas
else:                                                   # nenhuma nota válida
    print("Nenhuma nota válida")   # o usuário terminou sem digitar notas válidas
