# Aula 31 – Nível 2: Leitura com validação
# teste: 200; 17; 13; 5; 11; 9
def ler_numero(mensagem, minimo=0, maximo=100):   # valores padrão: usados quando não informados
    while True:                                   # repete até receber um valor válido
        valor = int(input(mensagem))              # lê o número (variável local da função)
        if minimo <= valor <= maximo:             # está dentro da faixa?
            return valor                          # sim: devolve o valor e sai da função
        print(f"Digite um valor entre {minimo} e {maximo}")   # não: avisa e repete
idade = ler_numero("Idade: ", 0, 120)             # a mesma função serve para vários usos
mes = ler_numero("Mês: ", 1, 12)                  # outra faixa
nota = ler_numero("Nota inteira: ", maximo=10)    # usa o mínimo padrão (0)
print(idade, mes, nota)                           # mostra os valores lidos
