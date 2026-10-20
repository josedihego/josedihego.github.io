# Aula 5 – Nível 3: Trocar valores e converter tipos
# teste: 
copo_a = "suco"                         # conteúdo do copo A
copo_b = "água"                         # conteúdo do copo B
auxiliar = copo_a                       # guarda o conteúdo de A num terceiro copo
copo_a = copo_b                         # A recebe o conteúdo de B
copo_b = auxiliar                       # B recebe o que estava guardado
print("Copo A:", copo_a)                # agora tem água
print("Copo B:", copo_b)                # agora tem suco
preco_texto = "12.50"                   # um número guardado como texto
preco = float(preco_texto)              # float converte o texto em número decimal
print(type(preco_texto), type(preco))   # str e float
print("Dobro:", preco * 2)              # só dá para calcular depois de converter
