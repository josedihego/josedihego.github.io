# Aula 33 – Nível 3: Agenda com edição
# teste: 1; Ana; 9999; 1; Ana; 1; Bia; 8888; 2; Ana; 7777; 3; 0
agenda = {}                                          # nome -> telefone
def cadastrar():   # função para a opção 1
    nome = input("Nome: ")                           # lê o nome
    if nome in agenda:                               # não aceita nome repetido
        print("Contato já cadastrado")   # avisa e não cadastra
    else:   # caso contrário
        agenda[nome] = input("Telefone: ")           # guarda
def editar():   # função para a opção 2
    nome = input("Nome a editar: ")                  # lê o nome
    if nome in agenda:                               # só edita se existir
        agenda[nome] = input("Novo telefone: ")      # substitui o valor
    else:   # caso contrário
        print("Não encontrado")   # avisa o usuário
def listar():   # função para a opção 3
    for nome, telefone in sorted(agenda.items()):    # sorted: em ordem alfabética
        print(nome, "-", telefone)   # um contato por linha
while True:                                          # menu
    opcao = input("1-Cadastrar 2-Editar 3-Listar 0-Sair: ")   # lê a opção
    if opcao == "1":   # opção 1
        cadastrar()   # chama a função
    elif opcao == "2":   # opção 2
        editar()   # chama a função
    elif opcao == "3":   # opção 3
        listar()   # chama a função
    elif opcao == "0":   # sair
        break   # encerra o menu
print("Total de contatos:", len(agenda))             # resumo ao sair
