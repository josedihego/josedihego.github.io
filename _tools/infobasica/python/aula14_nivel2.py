# Aula 14 – Nível 2: Gastos da semana
# teste: 10; 12; 8; 15; 9; 20; 11
total = 0                                              # acumulador começa em zero, antes do laço
for dia in range(1, 8):                                # repete para os 7 dias da semana
    gasto = float(input(f"Gasto do dia {dia}: R$ "))   # lê o gasto de um dia
    total = total + gasto                              # soma o gasto ao que já foi acumulado
media = total / 7                                      # média = total ÷ número de dias
print(f"Total da semana: R$ {total:.2f}")              # mostra o total
print(f"Média diária: R$ {media:.2f}")                 # mostra a média
