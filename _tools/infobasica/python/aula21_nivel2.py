# Aula 21 – Nível 2: Queda livre
# teste: 
import matplotlib.pyplot as plt         # biblioteca de gráficos (já vem no Colab)
gravidade = 9.81                        # aceleração da gravidade (m/s²)
tempos = []                             # valores do eixo x
distancias = []                         # valores do eixo y
for passo in range(31):                 # 31 instantes: de 0,0 s até 3,0 s
    tempo = passo * 0.1                 # cada passo vale 0,1 s
    distancia = gravidade * tempo ** 2 / 2   # distância percorrida em queda livre
    tempos.append(tempo)                # guarda o ponto do eixo x
    distancias.append(distancia)        # guarda o ponto do eixo y
plt.plot(tempos, distancias)            # desenha a curva
plt.xlabel("Tempo (s)")                 # rótulo do eixo x
plt.ylabel("Distância (m)")             # rótulo do eixo y
plt.title("Queda livre")                # título do gráfico
plt.grid()                              # linhas de grade
plt.show()                              # mostra o gráfico
