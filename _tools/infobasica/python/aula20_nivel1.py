# Aula 20 – Nível 1: Menu de uma escolha
# teste: 1
print("1 - Bom dia")                  # opções do menu
print("2 - Boa noite")   # segunda opção
opcao = input("Escolha: ")            # lê a opção como texto
if opcao == "1":                      # compara com o texto "1"
    print("Bom dia! ☀️")   # resposta da opção 1
elif opcao == "2":   # senão, se escolheu 2
    print("Boa noite! 🌙")   # resposta da opção 2
else:                                 # qualquer outra coisa
    print("Opção inválida")   # avisa o usuário
