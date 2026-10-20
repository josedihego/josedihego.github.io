# Aula 28 – Nível 3: Sigla, nome e contagem
# teste: ba
siglas = ["BA", "PE", "SP", "RJ", "MG"]                                       # lista de siglas
nomes = ["Bahia", "Pernambuco", "São Paulo", "Rio de Janeiro", "Minas Gerais"]   # na mesma ordem
sigla = input("Sigla: ").upper()                    # upper: aceita "ba" ou "BA"
if sigla in siglas:                                 # a sigla existe?
    posicao = siglas.index(sigla)                   # index devolve a posição
    print(nomes[posicao])                           # mesma posição na outra lista
else:   # sigla fora da lista
    print("Sigla não encontrada")   # avisa o usuário
palavras = ["areia", "cimento", "areia", "brita", "areia"]   # lista com repetições
print("areia aparece", palavras.count("areia"), "vezes")     # count conta as ocorrências
