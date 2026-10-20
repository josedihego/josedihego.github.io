# Aula 15 – Nível 2: Maior, menor e dias quentes
# teste: 28; 31; 33; 25; 29; 35; 22
maior = -1000                                                # valor bem baixo: qualquer temperatura será maior
menor = 1000                                                 # valor bem alto: qualquer temperatura será menor
dias_quentes = 0                                             # contador começa em zero
for dia in range(1, 8):                                      # repete para 7 dias
    temperatura = float(input(f"Temperatura do dia {dia}: "))  # lê a temperatura do dia
    if temperatura > maior:                                  # encontrou um valor maior?
        maior = temperatura                                  # guarda o novo maior
    if temperatura < menor:                                  # encontrou um valor menor?
        menor = temperatura                                  # guarda o novo menor
    if temperatura > 30:                                     # foi um dia quente?
        dias_quentes = dias_quentes + 1                      # contador: soma 1
print("Maior:", maior, "| Menor:", menor)                    # mostra os extremos
print("Dias acima de 30 °C:", dias_quentes)                  # mostra a contagem
