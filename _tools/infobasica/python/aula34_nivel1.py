# Aula 34 – Nível 1: Criar e ler um CSV
# teste: 
import csv                                                  # biblioteca para CSV
with open("exemplo.csv", "w", encoding="utf-8") as arquivo: # "w": cria o arquivo para escrever
    arquivo.write("Nome,Nota\nAna,8\nBia,6.5\n")            # \n quebra a linha
with open("exemplo.csv", encoding="utf-8") as arquivo:      # abre para ler
    for linha in csv.reader(arquivo):                       # cada linha vira uma lista
        print(linha)                                        # ['Nome', 'Nota'], ['Ana', '8'], ...
