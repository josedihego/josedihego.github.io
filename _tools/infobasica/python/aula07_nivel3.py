# Aula 7 – Nível 3: Caixa d'água cilíndrica
# teste: 1.2; 1; 20
import math                                            # biblioteca com math.pi
diametro = float(input("Diâmetro da caixa (m): "))     # medida de lado a lado
altura = float(input("Altura da caixa (m): "))         # altura útil
vazao = float(input("Vazão da torneira (L/min): "))    # litros por minuto
raio = diametro / 2                                    # o raio é metade do diâmetro
volume_m3 = math.pi * raio ** 2 * altura               # volume do cilindro = π·r²·h
volume_litros = volume_m3 * 1000                       # 1 m³ = 1000 litros
total_minutos = round(volume_litros / vazao)           # round arredonda para inteiro
horas = total_minutos // 60                            # horas completas
minutos = total_minutos % 60                           # minutos que sobram
print(f"Volume: {volume_m3:.2f} m³ = {volume_litros:.0f} litros")   # mostra o volume
print(f"Tempo para encher: {horas} h {minutos} min")                 # mostra o tempo
