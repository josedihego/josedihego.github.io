# Aula 27 – Nível 2: Chuva no ano
# teste: 
meses = ["jan", "fev", "mar", "abr", "mai", "jun",   # nomes dos meses (continua abaixo)
         "jul", "ago", "set", "out", "nov", "dez"]   # nomes dos meses
chuva = [320, 290, 360, 410, 380, 250,   # chuva de cada mês em mm (continua abaixo)
         190, 120, 80, 95, 140, 230]                 # chuva de cada mês em mm (exemplo)
total = 0                                            # acumulador
maior = chuva[0]                                     # começa supondo que janeiro é o maior
posicao_maior = 0                                    # e guarda a posição dele
for indice in range(len(chuva)):                     # percorre todas as posições
    total = total + chuva[indice]                    # soma a chuva do mês
    if chuva[indice] > maior:                        # achou um mês mais chuvoso?
        maior = chuva[indice]                        # guarda o novo maior
        posicao_maior = indice                       # e a posição dele
print("Total anual:", total, "mm")                   # soma do ano
print("Média mensal:", total / len(chuva), "mm")     # média
print("Mais chuvoso:", meses[posicao_maior])         # usa a posição para achar o nome do mês
print("Conferindo:", sum(chuva), max(chuva))         # funções prontas do Python
