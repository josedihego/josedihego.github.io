# Aula 22 – Nível 1: Bactérias que dobram
# teste: 
bacterias = 100                                     # população inicial
for hora in range(1, 11):                           # 10 horas
    bacterias = bacterias * 2                       # a cada hora a população dobra
    print(f"Hora {hora}: {bacterias} bactérias")    # mostra cada passo
