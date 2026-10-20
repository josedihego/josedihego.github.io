# Aula 16 – Nível 2: Quando o dinheiro dobra
# teste: 1000; 1
saldo = float(input("Valor aplicado (R$): "))   # valor inicial
taxa = float(input("Rendimento ao mês (%): "))  # taxa mensal (maior que zero)
objetivo = 2 * saldo                            # queremos dobrar o valor
meses = 0                                       # contador de meses
while saldo < objetivo:                         # repete ENQUANTO ainda não dobrou
    saldo = saldo + saldo * taxa / 100          # aplica o rendimento do mês
    meses = meses + 1                           # passou mais um mês
print(f"Dobra em {meses} meses (saldo: R$ {saldo:.2f})")  # mostra o resultado
