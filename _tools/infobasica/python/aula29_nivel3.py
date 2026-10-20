# Aula 29 – Nível 3: Compreensão de listas
# teste: 
palavras = ["tijolo", "cal", "argamassa", "areia", "concreto"]   # lista de palavras
longas = [p for p in palavras if len(p) > 5]           # só as com mais de 5 letras
print("Longas:", longas)   # ['tijolo', 'argamassa', 'concreto']
medidas_mm = [50.8, 25.4, 101.6, 12.7]                 # medidas em milímetros
em_polegadas = [round(m / 25.4, 2) for m in medidas_mm]   # 1 polegada = 25,4 mm
print("Em polegadas:", em_polegadas)                   # [2.0, 1.0, 4.0, 0.5]
