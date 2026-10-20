# Aula 32 – Nível 1: Dicionário de capitais
# teste: 
capitais = {"BA": "Salvador", "PE": "Recife", "SP": "São Paulo"}   # chave: valor
print(capitais["BA"])                         # acesso pela chave: Salvador
capitais["MG"] = "Belo Horizonte"             # chave nova: acrescenta
print(len(capitais))                          # 4 pares
for sigla, capital in capitais.items():       # items: percorre os pares
    print(sigla, "→", capital)   # BA → Salvador ...
