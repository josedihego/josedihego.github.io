# Aula 30 – Nível 3: Área útil da sala
# teste: 
import math                                        # para usar math.pi
def area_retangulo(largura, comprimento):          # def cria a função; os parâmetros vêm entre parênteses
    return largura * comprimento                   # return devolve o resultado
def area_circulo(raio):                            # outra função, com um parâmetro
    return math.pi * raio ** 2                     # área do círculo
def area_util(largura, comprimento, raio_coluna):  # função que usa as outras duas
    return area_retangulo(largura, comprimento) - area_circulo(raio_coluna)  # sala menos a coluna
area = area_util(5, 4, 0.3)                        # chama a função passando os valores
print(f"Área útil da sala: {area:.2f} m²")         # mostra o resultado
