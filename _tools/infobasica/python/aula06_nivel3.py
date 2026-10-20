# Aula 6 – Nível 3: Conta de energia
# teste: 1200; 1350; 0.85
leitura_anterior = float(input("Leitura anterior (kWh): "))   # número do medidor no mês passado
leitura_atual = float(input("Leitura atual (kWh): "))         # número do medidor hoje
preco_kwh = float(input("Preço do kWh (R$): "))               # tarifa por kWh
taxa_fixa = 12.00                                             # taxa cobrada todo mês (R$)
consumo = leitura_atual - leitura_anterior                    # energia gasta no mês
valor = consumo * preco_kwh + taxa_fixa                       # valor da conta
print(f"Consumo: {consumo:.0f} kWh")                          # :.0f mostra sem casas decimais
print(f"Valor da conta: R$ {valor:.2f}")                      # :.2f mostra 2 casas decimais
