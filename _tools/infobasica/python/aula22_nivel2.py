# Aula 22 – Nível 2: Resfriamento de uma peça
# teste: 
temperatura = 200                     # temperatura inicial da peça (°C)
ambiente = 25                         # temperatura do ambiente (°C)
minuto = 0                            # tempo decorrido
while temperatura >= 40:              # repete até a peça ficar abaixo de 40 °C
    temperatura = temperatura - 0.1 * (temperatura - ambiente)  # perde 10% da diferença a cada minuto
    minuto = minuto + 1               # passou um minuto
    print(f"{minuto} min: {temperatura:.1f} °C")   # mostra cada passo da simulação
print(f"Abaixo de 40 °C em {minuto} minutos")      # resultado final
