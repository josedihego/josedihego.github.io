# Aula 20 – Nível 2: Conversor com menu
# teste: 1; 2.5; 2; 100; x; 0
while True:                                  # laço principal: repete até encontrar um break
    print("1 - metros para centímetros")     # mostra o menu
    print("2 - °C para °F")                  # segunda opção
    print("0 - sair")                        # opção de saída
    opcao = input("Escolha: ")               # lê a opção como texto
    if opcao == "1":                         # primeira opção
        metros = float(input("Metros: "))    # lê o valor em metros
        print(metros * 100, "cm")            # converte e mostra
    elif opcao == "2":                       # segunda opção
        celsius = float(input("°C: "))       # lê a temperatura
        print(celsius * 9 / 5 + 32, "°F")    # fórmula de conversão
    elif opcao == "0":                       # usuário quer sair
        print("Até logo!")                   # mensagem final
        break                                # sai do laço e o programa termina
    else:                                    # qualquer outra coisa digitada
        print("Opção inválida")              # avisa e o menu aparece de novo
