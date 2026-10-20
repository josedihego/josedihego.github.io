# Aula 33 – Nível 1: Lista de tarefas
# teste: Estudar; Ler;
tarefas = []                                               # lista vazia
while True:                                                # repete até o break
    tarefa = input("Nova tarefa (em branco para terminar): ")   # lê uma tarefa
    if tarefa == "":                                       # nada digitado?
        break                                              # termina
    tarefas.append(tarefa)                                 # guarda
for numero, tarefa in enumerate(tarefas, start=1):         # enumerate numera a partir de 1
    print(numero, "-", tarefa)   # 1 - Estudar, 2 - Ler ...
