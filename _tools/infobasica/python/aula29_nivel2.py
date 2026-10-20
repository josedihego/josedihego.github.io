# Aula 29 – Nível 2: Peças fora da tolerância
# teste: 
medidas = [50.1, 49.7, 50.3, 49.9, 50.0, 50.25, 49.85]   # medidas das peças (mm)
nominal = 50.0                                           # valor de projeto (mm)
tolerancia = 0.2                                         # variação aceita (± mm)
fora = []                                                # lista das peças reprovadas
for medida in medidas:                                   # percorre cada medida
    if abs(medida - nominal) > tolerancia:               # abs: distância até o valor nominal
        fora.append(medida)                              # reprovada: guarda na lista
print("Fora da tolerância:", fora)                       # resultado do filtro
dentro = [m for m in medidas if abs(m - nominal) <= tolerancia]  # o filtro inverso numa linha
print("Dentro da tolerância:", dentro)                   # peças aprovadas
celsius = [20, 25, 30]                                   # transformar: cada elemento vira outro
fahrenheit = [c * 9 / 5 + 32 for c in celsius]           # converte todos de uma vez
print("Em °F:", fahrenheit)                              # [68.0, 77.0, 86.0]
