# Aula 10 – Nível 1: Ácido, neutro ou básico
# teste: 7
ph = float(input("pH da solução: "))   # lê o pH
if ph < 7:                             # abaixo de 7
    print("Ácido")                     # primeira faixa
elif ph == 7:                          # elif: só é testado se o if acima foi falso
    print("Neutro")                    # exatamente 7
else:                                  # sobrou: acima de 7
    print("Básico")                    # última faixa
