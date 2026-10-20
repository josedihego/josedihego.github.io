# Aula 7 – Nível 2: Círculo e tempo
# teste: 2; 3725
import math                                          # biblioteca com funções matemáticas
raio = float(input("Raio da circunferência (m): "))  # lê o raio
area = math.pi * raio ** 2                           # área = π·r² (** é potência)
comprimento = 2 * math.pi * raio                     # comprimento = 2·π·r
print(f"Área: {area:.2f} m²")                        # mostra a área com 2 casas
print(f"Comprimento: {comprimento:.2f} m")           # mostra o comprimento
total_segundos = int(input("Duração em segundos: ")) # lê um número inteiro
horas = total_segundos // 3600                       # // divisão inteira: horas completas
resto = total_segundos % 3600                        # % resto da divisão: segundos que sobraram
minutos = resto // 60                                # minutos completos no que sobrou
segundos = resto % 60                                # segundos finais
print(f"{horas} h {minutos} min {segundos} s")       # mostra no formato h min s
