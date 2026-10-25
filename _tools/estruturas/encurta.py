"""Moves the trailing comment of lines longer than 88 characters to its own line above, with the same
indentation (only for '// ' comments outside strings). Prints the lines it could not fix.
Uso: python3 _tools/estruturas/encurta.py arquivos.c"""
import sys, re

for f in sys.argv[1:]:
    saida = []
    for i, l in enumerate(open(f).read().split('\n'), 1):
        m = re.match(r'^(\s*)(.*?\S)\s+(// .*)$', l)
        if len(l) > 88 and m and m.group(2).count('"') % 2 == 0 and not l.lstrip().startswith('//'):
            saida += [m.group(1) + m.group(3), m.group(1) + m.group(2)]
        else:
            saida.append(l)
    open(f, 'w').write('\n'.join(saida))
    for i, l in enumerate(saida, 1):
        if len(l) > 88:
            print(f, i, l)
