# Aula 28 – Nível 2: Busca sequencial
# teste: O Cortiço
livros = ["Dom Casmurro", "Vidas Secas", "O Cortiço", "Iracema"]   # acervo da biblioteca
buscado = input("Título buscado: ")              # o que vamos procurar
posicao = 0                                      # começa no início da lista
encontrado = False                               # ainda não encontramos
while posicao < len(livros) and not encontrado:  # para quando achar ou quando a lista acabar
    if livros[posicao] == buscado:               # é este livro?
        encontrado = True                        # achou: o laço vai parar
    else:                                        # não é este
        posicao = posicao + 1                    # vai para o próximo
if encontrado:                                   # depois do laço, vemos o resultado
    print("Disponível na posição", posicao)      # posição em que achou
else:                                            # percorreu tudo sem achar
    print("Não encontrado")                      # avisa
print("Versão curta:", buscado in livros)        # in faz a mesma busca numa linha
