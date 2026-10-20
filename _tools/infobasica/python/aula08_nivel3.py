# Aula 8 – Nível 3: Ano bissexto
# teste: 2024
ano = int(input("Ano: "))                                       # lê o ano
divisivel_4 = ano % 4 == 0                                      # True se o resto da divisão por 4 for zero
divisivel_100 = ano % 100 == 0                                  # True se for divisível por 100
divisivel_400 = ano % 400 == 0                                  # True se for divisível por 400
bissexto = (divisivel_4 and not divisivel_100) or divisivel_400  # regra completa do calendário
print("Bissexto:", bissexto)                                    # mostra True ou False
