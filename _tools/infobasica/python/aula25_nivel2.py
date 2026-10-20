# Aula 25 – Nível 2: Contar vogais
# teste: Concreto armado
frase = input("Digite uma frase: ")        # lê o texto
print("Caracteres:", len(frase))           # len: tamanho do texto
print("Maiúsculas:", frase.upper())        # upper: tudo em maiúsculas
print("Três primeiras:", frase[0:3])       # fatia: posições 0, 1 e 2
vogais = 0                                 # contador de vogais
for letra in frase.lower():                # percorre cada letra, já em minúsculas
    if letra in "aeiouáéíóúâêôãõ":         # in: a letra está neste texto?
        vogais = vogais + 1                # conta mais uma vogal
print("Vogais:", vogais)                   # mostra o total
