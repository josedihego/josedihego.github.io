# Aula 27 – Nível 3: Acima da média e os 3 maiores
# teste: 
chuva = [320, 290, 360, 410, 380, 250, 190, 120, 80, 95, 140, 230]   # chuva mensal (mm)
media = sum(chuva) / len(chuva)                     # média anual
acima = 0                                           # contador
for valor in chuva:                                 # percorre os valores
    if valor > media:                               # acima da média?
        acima = acima + 1                           # conta
print(f"Média: {media:.1f} mm | Meses acima: {acima}")   # resultado
tres_maiores = sorted(chuva, reverse=True)[0:3]     # ordena do maior para o menor e pega 3
print("Três maiores:", tres_maiores)   # [410, 380, 360]
