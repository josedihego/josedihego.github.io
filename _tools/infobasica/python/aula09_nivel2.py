# Aula 9 – Nível 2: Aprovado ou reprovado
# teste: 6; 9
nota1 = float(input("Nota 1: "))    # lê a primeira nota
nota2 = float(input("Nota 2: "))    # lê a segunda nota
media = (nota1 + nota2) / 2         # parênteses: soma antes de dividir
print(f"Média: {media:.1f}")        # mostra a média com 1 casa decimal
if media >= 7:                      # se a condição for verdadeira...
    print("Aprovado")               # ...executa este bloco (repare no recuo)
else:                               # senão...
    print("Reprovado")              # ...executa este outro bloco
