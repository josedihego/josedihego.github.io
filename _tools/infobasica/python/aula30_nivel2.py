# Aula 30 – Nível 2: Função que devolve valor
# teste: 
def celsius_para_fahrenheit(celsius):   # recebe a temperatura em °C
    return celsius * 9 / 5 + 32         # return devolve o resultado para quem chamou
for c in range(0, 101, 20):             # 0, 20, 40, 60, 80, 100
    f = celsius_para_fahrenheit(c)      # guarda o valor devolvido
    print(c, "°C =", f, "°F")           # mostra a tabela
