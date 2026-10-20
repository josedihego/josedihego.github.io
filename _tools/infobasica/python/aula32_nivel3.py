# Aula 32 – Nível 3: Total vendido por produto
# teste: 
vendas = [("cimento", 38.9), ("areia", 120.0), ("cimento", 77.8),   # cada venda é um par (produto, valor)
          ("brita", 135.0), ("areia", 60.0)]       # lista de pares (produto, valor)
totais = {}                                       # produto -> total vendido
for produto, valor in vendas:                     # separa cada par em duas variáveis
    totais[produto] = totais.get(produto, 0) + valor   # get: total atual (ou 0) + valor
for produto, total in totais.items():             # mostra o resultado
    print(f"{produto}: R$ {total:.2f}")   # total de cada produto
