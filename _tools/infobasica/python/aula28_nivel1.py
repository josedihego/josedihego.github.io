# Aula 28 – Nível 1: Está na lista?
# teste: maçã
frutas = ["banana", "maçã", "manga", "caju"]   # lista de frutas
fruta = input("Fruta: ")                       # o que procurar
if fruta in frutas:                            # in: está na lista?
    print("Tem", fruta)   # encontrou
else:   # caso contrário
    print("Não tem", fruta)   # não encontrou
