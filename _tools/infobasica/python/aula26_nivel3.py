# Aula 26 – Nível 3: Nome do mês
# teste: 3
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",   # a lista pode continuar na linha de baixo
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]   # 12 meses
numero = int(input("Número do mês (1 a 12): "))   # lê o número
if 1 <= numero <= 12:                             # número válido?
    print(meses[numero - 1])                      # a lista começa no índice 0, por isso - 1
else:   # número fora da faixa
    print("Mês inválido")                         # fora da faixa
