# Aula 34 – Nível 2: Notas de um CSV
# teste: 
import csv                                      # biblioteca para ler arquivos CSV
from google.colab import files                  # ferramenta do Colab para enviar arquivos
files.upload()                                  # abre a janela: escolha o notas.csv baixado do Planilhas
notas = []                                      # lista das notas
with open("notas.csv", encoding="utf-8") as arquivo:   # abre o arquivo enviado
    leitor = csv.reader(arquivo)                # leitor de linhas do CSV
    next(leitor)                                # pula o cabeçalho (Nome, Nota)
    for linha in leitor:                        # cada linha vira uma lista: [nome, nota]
        nota = float(linha[1].replace(",", "."))   # troca "7,5" por "7.5" e converte
        notas.append(nota)                      # guarda a nota
print("Média:", sum(notas) / len(notas))        # média da turma
print("Maior:", max(notas), "| Menor:", min(notas))   # extremos
