# Aula 10 – Nível 3: Classificador de multas
# teste: 75; 60
velocidade = float(input("Velocidade medida (km/h): "))   # lê a velocidade
limite = float(input("Limite da via (km/h): "))           # lê o limite
excesso = (velocidade - limite) / limite * 100            # percentual acima do limite
if excesso <= 0:                                          # dentro do limite
    print("Sem multa")   # velocidade dentro do limite
elif excesso <= 20:                                       # até 20% acima
    print("Multa leve")   # até 20% acima
elif excesso <= 50:                                       # até 50% acima
    print("Multa grave")   # entre 20% e 50% acima
else:                                                     # mais de 50% acima
    print("Multa gravíssima")   # mais de 50% acima
print(f"Excesso: {max(excesso, 0):.0f}%")                 # max(...) evita mostrar excesso negativo
