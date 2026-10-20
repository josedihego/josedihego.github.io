# Aula 25 – Nível 3: E-mail e palíndromo
# teste: Ana; Souza; Arara
nome = input("Nome: ").strip().lower()             # strip tira espaços das pontas; lower deixa minúsculo
sobrenome = input("Sobrenome: ").strip().lower()   # o mesmo para o sobrenome
email = nome + "." + sobrenome + "@escola.br"      # + junta textos
print("E-mail:", email)                            # ana.souza@escola.br
palavra = input("Palavra: ").lower()               # lê outra palavra
invertida = palavra[::-1]                          # fatia com passo -1: o texto de trás para frente
if palavra == invertida:                           # igual lida dos dois lados?
    print(palavra, "é um palíndromo")   # ex.: arara
else:   # caso contrário
    print(palavra, "não é um palíndromo")   # ex.: casa
