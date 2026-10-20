# Aula 19 – Nível 2: Fibonacci com break
# teste: 
anterior = 0                    # primeiro termo
atual = 1                       # segundo termo
for posicao in range(20):       # no máximo 20 termos
    print(anterior, end=" ")    # mostra o termo
    proximo = anterior + atual  # cada termo é a soma dos dois anteriores
    anterior = atual            # avança uma posição
    atual = proximo             # avança uma posição
    if anterior > 1000:         # passou de 1000?
        break                   # break sai do laço na hora
print()                         # quebra a linha
