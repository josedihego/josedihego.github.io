# Aula 9 – Nível 3: Controle de qualidade
# teste: 50.15
medida = float(input("Medida da peça (mm): "))    # lê a medida
nominal = 50.0                                    # valor de projeto (mm)
tolerancia = 0.2                                  # variação aceita (± mm)
diferenca = abs(medida - nominal)                 # abs tira o sinal: distância até o nominal
if diferenca <= tolerancia:                       # dentro da tolerância?
    print(f"Aprovada (diferença de {diferenca:.2f} mm)")    # mensagem de aprovação
else:                                             # fora da tolerância
    print(f"Reprovada (diferença de {diferenca:.2f} mm)")   # mensagem de reprovação
