# Aula 6 – Nível 2: Preço com desconto
# teste: 100; 15
preco = float(input("Preço do produto (R$): "))   # lê o texto digitado e converte para decimal
desconto = float(input("Desconto (%): "))         # lê o percentual de desconto
valor_desconto = preco * desconto / 100           # calcula quanto será descontado
preco_final = preco - valor_desconto              # tira o desconto do preço
print(f"Desconto: R$ {valor_desconto:.2f}")       # f-string: {variável:.2f} mostra 2 casas decimais
print(f"Preço final: R$ {preco_final:.2f}")       # mostra o resultado formatado
