"""Publishes the course examples from _tools/progarduino/{c,arduino}:
  assets/progarduino/c/aulaNN_nivelK.c
  assets/progarduino/arduino/aulaNN_nivelK/{aulaNN_nivelK.ino, diagram.json}   (diagram.json = circuit for Wokwi)
  assets/progarduino/exemplos-progarduino.zip                                    (everything, by class)
and, with --kit DIR, the same tree in DIR (the exemplos/ folder of the portable kit).
The internal header lines ('// teste:' of the C files, '// pecas:' of the sketches) are not published.
Uso: python3 _tools/progarduino/gerar_exemplos.py <raiz do site> [--kit DIR]"""
import sys, os, glob, json, shutil, zipfile

CORES = {'vermelho': 'red', 'verde': 'green', 'amarelo': 'yellow', 'azul': 'blue', 'branco': 'white'}


def diagrama(pecas):
    """Builds a Wokwi diagram for an Arduino Uno from a parts list such as 'led 8 vermelho; botao 2'."""
    partes = [{'type': 'wokwi-arduino-uno', 'id': 'uno', 'top': 0, 'left': 0, 'attrs': {}}]
    fios = []
    x = -40                                                   # cada peça ocupa uma coluna acima da placa

    def liga(a, b, cor='green'):
        fios.append([a, b, cor, []])

    def gnd(peca_pino):
        liga(peca_pino, 'uno:GND.1', 'black')

    def mais5v(peca_pino):
        liga(peca_pino, 'uno:5V', 'red')

    for i, item in enumerate(p for p in pecas.split(';') if p.strip()):
        tipo, *args = item.split()
        uid = f'{tipo}{i + 1}'
        if tipo == 'led':
            pino, cor = args[0], CORES.get(args[1] if len(args) > 1 else 'vermelho', 'red')
            partes.append({'type': 'wokwi-led', 'id': uid, 'top': -190, 'left': x, 'attrs': {'color': cor}})
            partes.append({'type': 'wokwi-resistor', 'id': 'r' + uid, 'top': -95, 'left': x - 30, 'rotate': 90, 'attrs': {'value': '220'}})
            liga(f'uno:{pino}', f'r{uid}:2')
            liga(f'r{uid}:1', f'{uid}:A')
            gnd(f'{uid}:C')
            x += 60
        elif tipo == 'botao':
            partes.append({'type': 'wokwi-pushbutton', 'id': uid, 'top': -170, 'left': x, 'attrs': {'color': 'green'}})
            liga(f'uno:{args[0]}', f'{uid}:1.l')
            gnd(f'{uid}:2.l')
            x += 100
        elif tipo == 'pot':
            partes.append({'type': 'wokwi-potentiometer', 'id': uid, 'top': -190, 'left': x, 'attrs': {}})
            gnd(f'{uid}:GND')
            liga(f'uno:{args[0]}', f'{uid}:SIG')
            mais5v(f'{uid}:VCC')
            x += 110
        elif tipo == 'ldr':
            partes.append({'type': 'wokwi-photoresistor-sensor', 'id': uid, 'top': -210, 'left': x, 'rotate': 90, 'attrs': {}})
            mais5v(f'{uid}:VCC')
            gnd(f'{uid}:GND')
            liga(f'uno:{args[0]}', f'{uid}:AO')
            x += 110
        elif tipo == 'buzzer':
            partes.append({'type': 'wokwi-buzzer', 'id': uid, 'top': -190, 'left': x, 'attrs': {'volume': '0.1'}})
            gnd(f'{uid}:1')
            liga(f'uno:{args[0]}', f'{uid}:2')
            x += 90
        elif tipo == 'ultrassom':
            partes.append({'type': 'wokwi-hc-sr04', 'id': uid, 'top': -230, 'left': x, 'attrs': {'distance': '40'}})
            mais5v(f'{uid}:VCC')
            liga(f'uno:{args[0]}', f'{uid}:TRIG')
            liga(f'uno:{args[1]}', f'{uid}:ECHO', 'blue')
            gnd(f'{uid}:GND')
            x += 170
        elif tipo == 'servo':
            partes.append({'type': 'wokwi-servo', 'id': uid, 'top': -230, 'left': x, 'attrs': {}})
            gnd(f'{uid}:GND')
            mais5v(f'{uid}:V+')
            liga(f'uno:{args[0]}', f'{uid}:PWM', 'orange')
            x += 170
        elif tipo == 'rgb':
            partes.append({'type': 'wokwi-rgb-led', 'id': uid, 'top': -190, 'left': x, 'attrs': {'common': 'cathode'}})
            for cor, pino in zip('RGB', args):
                liga(f'uno:{pino}', f'{uid}:{cor}')
            gnd(f'{uid}:COM')
            x += 80
        else:
            raise ValueError(f'peça desconhecida: {item}')
    return {'version': 1, 'author': 'José Dihego – josedihego.net/progarduino', 'editor': 'wokwi',
            'parts': partes, 'connections': fios, 'dependencies': {}}


NOMES = {'led': 'LED', 'botao': 'botão', 'pot': 'potenciômetro', 'ldr': 'LDR', 'buzzer': 'buzzer',
         'ultrassom': 'HC-SR04', 'servo': 'servo', 'rgb': 'LED RGB'}


def descrever(pecas):
    """'led 8 vermelho; led 9 verde; botao 2' -> '2 LEDs, botão' (lista curta de peças para a página)."""
    contagem = {}
    for item in (p for p in pecas.split(';') if p.strip()):
        tipo = item.split()[0]
        contagem[tipo] = contagem.get(tipo, 0) + 1
    if not contagem:
        return 'só a placa'
    return ', '.join((f'{n} {NOMES[t]}s' if n > 1 and t == 'led' else f'{n}× {NOMES[t]}' if n > 1 else NOMES[t]) for t, n in contagem.items())


def gerar(raiz, kit=None):
    ferramentas = os.path.join(raiz, '_tools', 'progarduino')
    destino = os.path.join(raiz, 'assets', 'progarduino')
    for sub in ('c', 'arduino'):
        shutil.rmtree(os.path.join(destino, sub), ignore_errors=True)
        os.makedirs(os.path.join(destino, sub))
    arquivos = []                                             # (caminho no kit/zip, conteúdo)
    for fonte in sorted(glob.glob(os.path.join(ferramentas, 'c', '*.c'))):
        nome = os.path.basename(fonte)
        linhas = open(fonte).read().split('\n')
        texto = '\n'.join(linhas[:1] + linhas[2:])            # tira a linha '// teste:'
        open(os.path.join(destino, 'c', nome), 'w').write(texto)
        arquivos.append((f'{nome[:6]}/c/{nome}', texto))
    for pasta in sorted(glob.glob(os.path.join(ferramentas, 'arduino', '*'))):
        nome = os.path.basename(pasta)
        linhas = open(os.path.join(pasta, nome + '.ino')).read().split('\n')
        pecas = linhas[1].split(':', 1)[1].strip()
        texto = '\n'.join(linhas[:1] + linhas[2:])            # tira a linha '// pecas:'
        circuito = json.dumps(diagrama(pecas), indent=2, ensure_ascii=False) + '\n'
        os.makedirs(os.path.join(destino, 'arduino', nome))
        open(os.path.join(destino, 'arduino', nome, nome + '.ino'), 'w').write(texto)
        open(os.path.join(destino, 'arduino', nome, 'diagram.json'), 'w').write(circuito)
        arquivos.append((f'{nome[:6]}/arduino/{nome}/{nome}.ino', texto))
        arquivos.append((f'{nome[:6]}/arduino/{nome}/diagram.json', circuito))
    with zipfile.ZipFile(os.path.join(destino, 'exemplos-progarduino.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for caminho, texto in arquivos:
            z.writestr('exemplos/' + caminho, texto)
    # títulos e peças de cada nível, para a página
    indice = {}
    for fonte in sorted(glob.glob(os.path.join(ferramentas, 'c', '*.c'))):
        nome = os.path.basename(fonte)[:-2]
        indice.setdefault(nome[:6], {'c': [], 'arduino': [], 'pecas': []})['c'].append(open(fonte).readline().split(': ', 1)[1].strip())
    for pasta in sorted(glob.glob(os.path.join(ferramentas, 'arduino', '*'))):
        nome = os.path.basename(pasta)
        primeira, segunda = open(os.path.join(pasta, nome + '.ino')).read().split('\n')[:2]
        indice[nome[:6]]['arduino'].append(primeira.split(': ', 1)[1].strip())
        indice[nome[:6]]['pecas'].append(descrever(segunda.split(':', 1)[1].strip()))
    with open(os.path.join(raiz, '_data', 'progarduino_exemplos.yml'), 'w') as y:
        y.write('# Gerado por _tools/progarduino/gerar_exemplos.py: títulos dos níveis e peças de cada sketch\n')
        for aula, d in indice.items():
            y.write(f'{aula}:\n')
            for chave in ('c', 'arduino', 'pecas'):
                y.write(f'  {chave}:\n' + ''.join('    - ' + json.dumps(t, ensure_ascii=False) + '\n' for t in d[chave]))
    if kit:
        shutil.rmtree(kit, ignore_errors=True)
        for caminho, texto in arquivos:
            os.makedirs(os.path.dirname(os.path.join(kit, caminho)), exist_ok=True)
            open(os.path.join(kit, caminho), 'w').write(texto)
    return len(arquivos)


if __name__ == '__main__':
    kit = sys.argv[sys.argv.index('--kit') + 1] if '--kit' in sys.argv else None
    print(gerar(sys.argv[1], kit), 'arquivos gerados')
