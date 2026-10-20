# Aula 20 – Nível 3: Caixa eletrônico
# teste: 2; 100; 3; 150; 3; 30; 1; 0
saldo = 0.0                                              # dinheiro na conta
operacoes = 0                                            # contador de operações feitas
while True:                                              # laço principal do menu
    opcao = input("1-Saldo 2-Depositar 3-Sacar 0-Sair: ")   # lê a opção
    if opcao == "1":                                     # consultar
        print(f"Saldo: R$ {saldo:.2f}")   # mostra o saldo atual
    elif opcao == "2":                                   # depositar
        valor = float(input("Valor do depósito: "))   # lê o valor a depositar
        saldo = saldo + valor                            # aumenta o saldo
        operacoes = operacoes + 1                        # conta a operação
    elif opcao == "3":                                   # sacar
        valor = float(input("Valor do saque: "))   # lê o valor a sacar
        if valor <= saldo:                               # só saca se tiver saldo
            saldo = saldo - valor   # diminui o saldo
            operacoes = operacoes + 1   # conta a operação
        else:   # caso contrário
            print("Saldo insuficiente")   # não deixa o saldo ficar negativo
    elif opcao == "0":                                   # sair
        break                                            # encerra o laço
    else:   # caso contrário
        print("Opção inválida")   # qualquer outra tecla
print("Operações realizadas:", operacoes)                # resumo ao sair
