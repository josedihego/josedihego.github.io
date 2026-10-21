"""Compiles every C example with -Wall -Wextra (any warning counts as a failure), runs it with the
inputs of its '// teste:' line (values separated by ';', or '1..100') and lists lines without a comment.
Uso: python3 _tools/progarduino/testar_c.py [gcc]   (padrão: gcc do sistema; use o do kit para testá-lo)"""
import sys, os, glob, subprocess, tempfile

GCC = sys.argv[1] if len(sys.argv) > 1 else 'gcc'
pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c')
saida = tempfile.mkdtemp()
falhas = sem_comentario = 0

def precisa_comentario(linha):
    s = linha.strip()
    return s and '//' not in s and s not in ('{', '}', '};', '} else {') and not s.startswith('#include')

for fonte in sorted(glob.glob(os.path.join(pasta, '*.c'))):
    nome = os.path.basename(fonte)[:-2]
    linhas = open(fonte).read().split('\n')
    teste = linhas[1].split(':', 1)[1].strip()
    entrada = '\n'.join(str(i) for i in range(1, 101)) if teste == '1..100' else '\n'.join(v.strip() for v in teste.split(';')) if teste else ''
    exe = os.path.join(saida, nome)
    c = subprocess.run([GCC, '-Wall', '-Wextra', '-std=c17', fonte, '-o', exe, '-lm'], capture_output=True, text=True)
    if c.returncode != 0 or c.stderr.strip():
        falhas += 1
        print(f'COMPILAÇÃO {nome}:\n{c.stderr.strip()[:600]}')
        continue
    try:
        r = subprocess.run([exe], input=entrada + '\n', capture_output=True, text=True, timeout=20, cwd=saida)
        ultima = (r.stdout.strip().splitlines() or ['(sem saída)'])[-1]
        estado = 'OK' if r.returncode == 0 else f'SAIU COM {r.returncode}'
        if r.returncode != 0: falhas += 1
        print(f'{estado} {nome}: {ultima[:80]}')
    except subprocess.TimeoutExpired:
        falhas += 1
        print(f'TEMPO ESGOTADO {nome}')
    for l in linhas[2:]:
        if precisa_comentario(l):
            sem_comentario += 1
print('falhas:', falhas, '| linhas sem comentário:', sem_comentario)
sys.exit(1 if falhas else 0)
