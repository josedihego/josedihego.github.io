"""Runs every example in _tools/infobasica/python with the inputs from its '# teste:' line
(values separated by ';', or '1..100'). Colab and matplotlib are stubbed.
Uso: python3 _tools/infobasica/testar_python.py _tools/infobasica/python"""
import sys, os, glob, types, builtins, io, contextlib, random, tempfile

plt = types.ModuleType("matplotlib.pyplot")
for f in "plot bar xlabel ylabel title grid legend show".split():
    setattr(plt, f, lambda *a, **k: None)
mpl = types.ModuleType("matplotlib"); mpl.pyplot = plt
colab = types.ModuleType("google.colab")
colab.files = types.SimpleNamespace(upload=lambda: None, download=lambda nome: None)
sys.modules.update({"matplotlib": mpl, "matplotlib.pyplot": plt, "google": types.ModuleType("google"), "google.colab": colab})

pasta = os.path.abspath(sys.argv[1])
os.chdir(tempfile.mkdtemp())
open("notas.csv", "w", encoding="utf-8").write('Nome,Nota\nAna,"7,5"\nBia,9\nCaio,"5,5"\n')
falhas = sem_comentario = 0
for fonte in sorted(glob.glob(os.path.join(pasta, '*.py'))):
    linhas = open(fonte).read().split('\n')
    teste = linhas[1].split(':', 1)[1].strip()
    fila = [str(i) for i in range(1, 101)] if teste == '1..100' else ([v.strip() for v in teste.split(';')] if teste else [])
    codigo = '\n'.join(linhas[2:])
    def falso_input(msg=""):
        v = fila.pop(0); print(msg + v); return v
    builtins.input = falso_input
    random.seed(1)
    saida = io.StringIO()
    nome = os.path.basename(fonte)
    try:
        with contextlib.redirect_stdout(saida):
            exec(codigo, {})
        ultima = saida.getvalue().splitlines()
        print(f"OK {nome}: {ultima[-1][:60] if ultima else '(sem texto: só gráfico)'}")
    except Exception as e:
        falhas += 1
        print(f"FALHOU {nome}: {e!r}")
    for l in linhas[2:]:
        if l.strip() and '#' not in l:
            sem_comentario += 1
            print(f"   sem comentário: {nome}: {l.strip()}")
print("falhas:", falhas, "| linhas sem comentário:", sem_comentario)
sys.exit(1 if falhas else 0)
