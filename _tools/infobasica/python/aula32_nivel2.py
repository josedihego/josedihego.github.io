# Aula 32 – Nível 2: Orçamento de materiais
# teste: 
precos = {"cimento": 38.90, "areia": 120.00, "brita": 135.00}   # material -> preço (R$)
print("Preço do cimento:", precos["cimento"])       # acesso pela chave
precos["cal"] = 22.50                               # chave nova: adiciona ao dicionário
pedido = {"cimento": 10, "areia": 2}                # material -> quantidade
total = 0                                           # acumulador do custo
for material, quantidade in pedido.items():         # items percorre os pares chave-valor
    custo = precos[material] * quantidade           # preço × quantidade
    print(f"{material}: R$ {custo:.2f}")            # custo de cada item
    total = total + custo                           # acumula
print(f"Total do pedido: R$ {total:.2f}")           # custo total
contagem = {}                                       # dicionário vazio para contar letras
for letra in "concreto":                            # percorre cada letra
    contagem[letra] = contagem.get(letra, 0) + 1    # get: valor atual (ou 0) + 1
print(contagem)                                     # {'c': 2, 'o': 2, 'n': 1, ...}
