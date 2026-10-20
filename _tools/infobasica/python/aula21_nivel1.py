# Aula 21 – Nível 1: Gráfico de uma reta
# teste: 
import matplotlib.pyplot as plt    # biblioteca de gráficos (já vem no Colab)
valores_x = []                     # pontos do eixo x
valores_y = []                     # pontos do eixo y
for x in range(-10, 11):           # x de -10 a 10
    valores_x.append(x)            # guarda o x
    valores_y.append(2 * x + 1)    # guarda y = 2x + 1
plt.plot(valores_x, valores_y)     # desenha a reta
plt.grid()                         # linhas de grade
plt.show()                         # mostra o gráfico
