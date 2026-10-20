# Aula 5 – Nível 2: Área e perímetro
# teste: 
largura = 4.5                                # largura do cômodo em metros (float)
comprimento = 3.2                            # comprimento do cômodo em metros (float)
quantidade_portas = 2                        # número inteiro (int)
nome_comodo = "Sala"                         # texto (str)
area = largura * comprimento                 # área = largura × comprimento
perimetro = 2 * (largura + comprimento)      # perímetro = soma dos quatro lados
print(nome_comodo, "- área:", area, "m²")    # mostra o nome e a área
print("Perímetro:", perimetro, "m")          # mostra o perímetro
print(type(area), type(quantidade_portas))   # type mostra o tipo de cada variável
