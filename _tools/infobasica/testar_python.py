"""Runs the code cell of every Colab notebook with canned keyboard input (Colab and matplotlib stubbed).
Uso: python3 _tools/infobasica/testar_python.py assets/infobasica/python"""
import sys, os, json, types, builtins, io, contextlib, random, tempfile

entradas = {4: [], 5: [], 6: ["100", "15"], 7: ["2", "3725"], 8: ["17", "s"], 9: ["6", "9"], 10: ["8.5"],
            13: [], 14: ["10"] * 7, 15: ["28", "31", "33", "25", "29", "35", "22"], 16: ["1000", "1"], 17: [],
            18: [str(i) for i in range(1, 101)], 19: [], 20: ["1", "2.5", "2", "100", "x", "0"], 21: [], 22: [],
            25: ["Concreto armado"], 26: ["Ana", "Bia", "Caio", "Davi", "Eva"], 27: [], 28: ["O Cortiço"], 29: [],
            30: [], 31: ["200", "17", "13", "5", "11", "9"], 32: [],
            33: ["1", "Ana", "9999", "1", "Ana", "3", "2", "Ana", "4", "Ana", "3", "0"], 34: []}

plt = types.ModuleType("matplotlib.pyplot")
for f in "plot xlabel ylabel title grid show".split():
    setattr(plt, f, lambda *a, **k: None)
mpl = types.ModuleType("matplotlib"); mpl.pyplot = plt
colab = types.ModuleType("google.colab"); colab.files = types.SimpleNamespace(upload=lambda: None)
sys.modules.update({"matplotlib": mpl, "matplotlib.pyplot": plt, "google": types.ModuleType("google"), "google.colab": colab})

pasta = os.path.abspath(sys.argv[1])
os.chdir(tempfile.mkdtemp())
open("notas.csv", "w", encoding="utf-8").write('Nome,Nota\nAna,"7,5"\nBia,9\nCaio,"5,5"\n')
falhas = 0
for nome in sorted(os.listdir(pasta)):
    n = int(nome[4:6])
    codigo = "".join(json.load(open(os.path.join(pasta, nome)))["cells"][1]["source"])
    fila = list(entradas.get(n, []))
    def falso_input(msg=""):
        v = fila.pop(0); print(msg + v); return v
    builtins.input = falso_input
    random.seed(1)
    saida = io.StringIO()
    try:
        with contextlib.redirect_stdout(saida):
            exec(codigo, {})
        linhas = saida.getvalue().splitlines()
        print(f"OK {nome}: {linhas[-1][:70] if linhas else '(sem saída de texto)'}")
    except Exception as e:
        falhas += 1
        print(f"FALHOU {nome}: {e!r}")
print("falhas:", falhas)
sys.exit(1 if falhas else 0)
