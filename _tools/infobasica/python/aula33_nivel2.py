# Aula 33 – Nível 2: Agenda de contatos
# teste: 1; Ana; 9999; 1; Ana; 3; 2; Ana; 4; Ana; 3; 0
agenda = {}                                     # nome -> telefone
def cadastrar():                                # uma função para cada operação
    nome = input("Nome: ")                      # lê o nome
    if nome in agenda:                          # nome repetido?
        print("Contato já cadastrado")          # não cadastra de novo
    else:                                       # nome novo
        agenda[nome] = input("Telefone: ")      # guarda o telefone
def buscar():                                   # procura um contato
    nome = input("Nome buscado: ")              # lê o nome
    print(agenda.get(nome, "Não encontrado"))   # get devolve o padrão se não achar
def listar():                                   # mostra todos os contatos
    for nome, telefone in agenda.items():       # percorre a agenda
        print(nome, "-", telefone)              # um contato por linha
def remover():                                  # apaga um contato
    nome = input("Nome a remover: ")            # lê o nome
    if nome in agenda:                          # só remove se existir
        del agenda[nome]                        # del apaga a chave
while True:                                     # laço principal do menu
    opcao = input("1-Cadastrar 2-Buscar 3-Listar 4-Remover 0-Sair: ")   # lê a opção
    if opcao == "1":                            # chama a função de cada opção
        cadastrar()   # chama a função da opção
    elif opcao == "2":   # opção 2
        buscar()   # chama a função da opção
    elif opcao == "3":   # opção 3
        listar()   # chama a função da opção
    elif opcao == "4":   # opção 4
        remover()   # chama a função da opção
    elif opcao == "0":                          # sair
        break                                   # encerra o programa
