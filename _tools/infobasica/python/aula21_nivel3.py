# Aula 21 – Nível 3: Queda livre na Terra e na Lua
# teste: 
import matplotlib.pyplot as plt                    # biblioteca de gráficos
tempos = []                                        # eixo x
terra = []                                         # distâncias na Terra
lua = []                                           # distâncias na Lua
for passo in range(31):                            # de 0,0 s a 3,0 s
    tempo = passo * 0.1                            # cada passo vale 0,1 s
    tempos.append(tempo)                           # guarda o tempo
    terra.append(9.81 * tempo ** 2 / 2)            # g da Terra = 9,81 m/s²
    lua.append(1.62 * tempo ** 2 / 2)              # g da Lua = 1,62 m/s²
plt.plot(tempos, terra, label="Terra")             # primeira curva
plt.plot(tempos, lua, label="Lua")                 # segunda curva
plt.xlabel("Tempo (s)")                            # rótulo do eixo x
plt.ylabel("Distância (m)")                        # rótulo do eixo y
plt.legend()                                       # legenda com os nomes das curvas
plt.grid()                                         # linhas de grade
plt.show()                                         # mostra o gráfico
