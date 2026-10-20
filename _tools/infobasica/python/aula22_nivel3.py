# Aula 22 – Nível 3: Concentração com gráfico
# teste: 
import matplotlib.pyplot as plt                       # biblioteca de gráficos
concentracao = 100.0                                  # concentração inicial (%)
hora = 0                                              # tempo decorrido
horas = [0]                                           # eixo x começa no instante zero
valores = [concentracao]                              # eixo y começa com 100%
while concentracao >= 10:                             # até ficar abaixo de 10%
    concentracao = concentracao * (1 - 0.08)          # perde 8% por hora
    hora = hora + 1                                   # passou uma hora
    horas.append(hora)                                # guarda o ponto
    valores.append(concentracao)   # guarda o valor do eixo y
print(f"Abaixo de 10% após {hora} horas")             # resultado
plt.plot(horas, valores)                              # curva de decaimento
plt.xlabel("Horas")                                   # rótulos
plt.ylabel("Concentração (%)")   # rótulo do eixo y
plt.grid()   # linhas de grade
plt.show()   # mostra o gráfico
