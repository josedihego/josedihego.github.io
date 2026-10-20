# Aula 34 – Nível 3: Gravar um CSV e baixar
# teste: 
import csv                                            # biblioteca para CSV
import matplotlib.pyplot as plt                       # biblioteca de gráficos
from google.colab import files                        # para baixar o arquivo no Colab
consumo = [12, 14, 13, 15, 18, 20, 21, 19, 16, 14, 13, 12]   # m³ de água por mês
with open("trimestres.csv", "w", newline="", encoding="utf-8") as arquivo:   # cria o arquivo de resultados
    escritor = csv.writer(arquivo)                    # escritor de linhas CSV
    escritor.writerow(["Trimestre", "Consumo medio"]) # cabeçalho
    for t in range(4):                                # 4 trimestres
        tres_meses = consumo[t * 3:t * 3 + 3]         # fatia com 3 meses
        escritor.writerow([t + 1, round(sum(tres_meses) / 3, 1)])   # média do trimestre
files.download("trimestres.csv")                      # baixa o arquivo para abrir no Planilhas
plt.bar(range(1, 13), consumo)                        # gráfico de barras mês a mês
plt.xlabel("Mês")   # rótulo do eixo x
plt.ylabel("Consumo (m³)")   # rótulo do eixo y
plt.show()   # mostra o gráfico
