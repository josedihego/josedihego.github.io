# Aula 8 – Nível 2: Quem pode votar
# teste: 17; s
idade = int(input("Idade: "))                          # lê a idade
resposta = input("Tem título de eleitor? (s/n) ")      # lê s ou n
tem_titulo = resposta == "s"                           # a comparação vira True ou False
voto_facultativo = idade >= 16 and idade < 18          # and: as duas condições precisam ser verdadeiras
pode_votar = tem_titulo and idade >= 16                # combina as duas informações
print("Voto facultativo:", voto_facultativo)           # mostra True ou False
print("Pode votar:", pode_votar)                       # mostra True ou False
print("Não pode votar:", not pode_votar)               # not inverte o resultado
