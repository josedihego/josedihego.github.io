"""Builds the Scratch 3 (.sb3) example projects of the lesson plan."""
import sys, os, json, hashlib, zipfile, itertools

class B:
    """A block; reporters/booleans are used as values, stack blocks are chained with seq()."""
    def __init__(self, p, id): self.p, self.id = p, id

class Projeto:
    def __init__(self, titulo):
        self.titulo = titulo
        self.blocks, self.vars, self.lists = {}, {}, {}
        self.cont = itertools.count()
        self.tops = 0

    def novo_id(self): return f"b{next(self.cont)}"

    def var(self, nome):
        if nome not in self.vars: self.vars[nome] = f"v_{len(self.vars)}"
        return ('var', nome)

    def lista(self, nome):
        if nome not in self.lists: self.lists[nome] = f"l_{len(self.lists)}"
        return nome

    def entrada(self, valor, tipo, pai):
        if isinstance(valor, B):
            self.blocks[valor.id]['parent'] = pai
            return [3, valor.id, [tipo, ""]] if tipo != 'bool' else [2, valor.id]
        if isinstance(valor, tuple) and valor[0] == 'var':
            return [3, [12, valor[1], self.vars[valor[1]]], [tipo, ""]]
        return [1, [tipo, str(valor)]]

    def bloco(self, opcode, num={}, txt={}, boo={}, campos={}, sub={}, mutation=None, shadow=False):
        id = self.novo_id()
        b = {'opcode': opcode, 'next': None, 'parent': None, 'inputs': {}, 'fields': campos,
             'shadow': shadow, 'topLevel': False}
        if mutation: b['mutation'] = mutation
        self.blocks[id] = b
        for k, v in num.items(): b['inputs'][k] = self.entrada(v, 4, id)
        for k, v in txt.items(): b['inputs'][k] = self.entrada(v, 10, id)
        for k, v in boo.items(): b['inputs'][k] = self.entrada(v, 'bool', id)
        for k, pilha in sub.items():
            if pilha:
                primeiro = self.seq(pilha)
                self.blocks[primeiro.id]['parent'] = id
                b['inputs'][k] = [2, primeiro.id]
        return B(self, id)

    def seq(self, blocos):
        for a, b in zip(blocos, blocos[1:]):
            self.blocks[a.id]['next'] = b.id
            self.blocks[b.id]['parent'] = a.id
        return blocos[0]

    def script(self, chapeu, corpo):
        self.seq([chapeu] + corpo)
        h = self.blocks[chapeu.id]
        h.update(topLevel=True, x=40, y=40 + 600 * self.tops)
        self.tops += 1

    # --- blocos usados nos exemplos ---
    def bandeira(self): return self.bloco('event_whenflagclicked')
    def diga(self, msg, segundos=2): return self.bloco('looks_sayforsecs', txt={'MESSAGE': msg}, num={'SECS': segundos})
    def diga_sempre(self, msg): return self.bloco('looks_say', txt={'MESSAGE': msg})
    def pergunte(self, q): return self.bloco('sensing_askandwait', txt={'QUESTION': q})
    def resposta(self): return self.bloco('sensing_answer')
    def mude(self, v, valor): return self.bloco('data_setvariableto', txt={'VALUE': valor}, campos={'VARIABLE': [v[1], self.vars[v[1]]]})
    def adicione(self, v, valor): return self.bloco('data_changevariableby', num={'VALUE': valor}, campos={'VARIABLE': [v[1], self.vars[v[1]]]})
    def op(self, nome, a, b): return self.bloco('operator_' + nome, num={'NUM1': a, 'NUM2': b})
    def junte(self, a, b): return self.bloco('operator_join', txt={'STRING1': a, 'STRING2': b})
    def junte_varios(self, *partes):
        r = partes[-1]
        for p in reversed(partes[:-1]): r = self.junte(p, r)
        return r
    def compara(self, nome, a, b): return self.bloco('operator_' + nome, txt={'OPERAND1': a, 'OPERAND2': b})
    def e(self, a, b): return self.bloco('operator_and', boo={'OPERAND1': a, 'OPERAND2': b})
    def ou(self, a, b): return self.bloco('operator_or', boo={'OPERAND1': a, 'OPERAND2': b})
    def nao(self, a): return self.bloco('operator_not', boo={'OPERAND': a})
    def arredonde(self, a): return self.bloco('operator_round', num={'NUM': a})
    def aleatorio(self, de, ate): return self.bloco('operator_random', num={'FROM': de, 'TO': ate})
    def se(self, cond, entao): return self.bloco('control_if', boo={'CONDITION': cond}, sub={'SUBSTACK': entao})
    def se_senao(self, cond, entao, senao): return self.bloco('control_if_else', boo={'CONDITION': cond}, sub={'SUBSTACK': entao, 'SUBSTACK2': senao})
    def repita(self, vezes, corpo): return self.bloco('control_repeat', num={'TIMES': vezes}, sub={'SUBSTACK': corpo})
    def repita_ate(self, cond, corpo): return self.bloco('control_repeat_until', boo={'CONDITION': cond}, sub={'SUBSTACK': corpo})
    def espere(self, s): return self.bloco('control_wait', num={'DURATION': s})
    def mova(self, passos): return self.bloco('motion_movesteps', num={'STEPS': passos})
    def gire(self, graus): return self.bloco('motion_turnright', num={'DEGREES': graus})
    def va_para(self, x, y): return self.bloco('motion_gotoxy', num={'X': x, 'Y': y})
    def apague_lista(self, l): return self.bloco('data_deletealloflist', campos={'LIST': [l, self.lists[l]]})
    def insira(self, l, item): return self.bloco('data_addtolist', txt={'ITEM': item}, campos={'LIST': [l, self.lists[l]]})
    def item(self, l, indice): return self.bloco('data_itemoflist', num={'INDEX': indice}, campos={'LIST': [l, self.lists[l]]})
    def tamanho(self, l): return self.bloco('data_lengthoflist', campos={'LIST': [l, self.lists[l]]})

    def definir(self, texto, params, corpo):
        """Custom block (Meus Blocos). texto uses %s for each parameter."""
        ids = [f"a_{self.titulo}_{p}" for p in params]
        mut = {'tagName': 'mutation', 'children': [], 'proccode': texto, 'argumentids': json.dumps(ids),
               'argumentnames': json.dumps(params), 'argumentdefaults': json.dumps([""] * len(params)), 'warp': 'false'}
        prot = self.bloco('procedures_prototype', mutation=mut, shadow=True)
        for i, p in zip(ids, params):
            r = self.bloco('argument_reporter_string_number', campos={'VALUE': [p, None]}, shadow=True)
            self.blocks[r.id]['parent'] = prot.id
            self.blocks[prot.id]['inputs'][i] = [1, r.id]
        defin = self.bloco('procedures_definition')
        self.blocks[defin.id]['inputs']['custom_block'] = [1, prot.id]
        self.blocks[prot.id]['parent'] = defin.id
        self.script(defin, corpo)
        return texto, ids

    def parametro(self, nome): return self.bloco('argument_reporter_string_number', campos={'VALUE': [nome, None]})

    def chame(self, assinatura, valores):
        texto, ids = assinatura
        mut = {'tagName': 'mutation', 'children': [], 'proccode': texto, 'argumentids': json.dumps(ids), 'warp': 'false'}
        return self.bloco('procedures_call', txt=dict(zip(ids, valores)), mutation=mut)

    def salvar(self, arquivo, comentario):
        fundo = b'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360"><rect width="480" height="360" fill="#ffffff"/></svg>'
        ator = ('<svg xmlns="http://www.w3.org/2000/svg" width="96" height="100">'
                '<circle cx="48" cy="50" r="44" fill="#4c97ff" stroke="#3373cc" stroke-width="4"/>'
                '<circle cx="34" cy="42" r="7" fill="#fff"/><circle cx="62" cy="42" r="7" fill="#fff"/>'
                '<circle cx="35" cy="43" r="3" fill="#222"/><circle cx="63" cy="43" r="3" fill="#222"/>'
                '<path d="M30 64 Q48 80 66 64" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/></svg>').encode()
        def figurino(dados, nome, cx, cy):
            md5 = hashlib.md5(dados).hexdigest()
            return {'assetId': md5, 'name': nome, 'md5ext': md5 + '.svg', 'dataFormat': 'svg',
                    'rotationCenterX': cx, 'rotationCenterY': cy}, (md5 + '.svg', dados)
        f_fundo, a_fundo = figurino(fundo, 'fundo', 240, 180)
        f_ator, a_ator = figurino(ator, 'robô', 48, 50)
        palco = {'isStage': True, 'name': 'Stage',
                 'variables': {id: [nome, 0] for nome, id in self.vars.items()},
                 'lists': {id: [nome, []] for nome, id in self.lists.items()},
                 'broadcasts': {}, 'blocks': {}, 'comments': {}, 'currentCostume': 0, 'costumes': [f_fundo],
                 'sounds': [], 'volume': 100, 'layerOrder': 0, 'tempo': 60, 'videoTransparency': 50,
                 'videoState': 'on', 'textToSpeechLanguage': None}
        ator_alvo = {'isStage': False, 'name': 'Robô', 'variables': {}, 'lists': {}, 'broadcasts': {},
                     'blocks': self.blocks,
                     'comments': {'c0': {'blockId': None, 'x': 520, 'y': 40, 'width': 320, 'height': 260,
                                         'minimized': False, 'text': comentario}},
                     'currentCostume': 0, 'costumes': [f_ator], 'sounds': [], 'volume': 100, 'layerOrder': 1,
                     'visible': True, 'x': 0, 'y': 0, 'size': 100, 'direction': 90, 'draggable': False,
                     'rotationStyle': 'all around'}
        monitores = [{'id': id, 'mode': 'default', 'opcode': 'data_variable', 'params': {'VARIABLE': nome},
                      'spriteName': None, 'value': 0, 'width': 0, 'height': 0, 'x': 5, 'y': 5 + 27 * i,
                      'visible': nome != 'secreto', 'sliderMin': 0, 'sliderMax': 100, 'isDiscrete': True}
                     for i, (nome, id) in enumerate(self.vars.items())]
        projeto = {'targets': [palco, ator_alvo], 'monitors': monitores, 'extensions': [],
                   'meta': {'semver': '3.0.0', 'vm': '0.2.0', 'agent': 'IFBA – plano de aulas de Informática'}}
        with zipfile.ZipFile(arquivo, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('project.json', json.dumps(projeto, ensure_ascii=False))
            for nome, dados in (a_fundo, a_ator):
                z.writestr(nome, dados)


def aula03(p):
    nome, curso = p.var('nome'), p.var('curso')
    p.script(p.bandeira(), [
        p.va_para(0, 0),
        p.pergunte('Qual é o seu nome?'), p.mude(nome, p.resposta()),
        p.pergunte('Qual é o seu curso?'), p.mude(curso, p.resposta()),
        p.diga(p.junte_varios('Olá, ', nome, '!'), 2),
        p.mova(80), p.gire(15),
        p.diga(p.junte_varios('Que legal estudar ', curso, '!'), 2),
        p.gire(-15), p.mova(-80)])
    return 'Diálogo: o ator pergunta o nome e o curso, guarda as respostas em variáveis e responde usando o bloco "junte".'

def aula04(p):
    p.script(p.bandeira(), [p.diga('Olá, mundo!', 2), p.diga('Curso: Edificações', 2), p.diga('Turma: 1º ano', 2)])
    return 'Primeiro programa: cada bloco "diga" equivale a um print() do Python.'

def aula06(p):
    preco, desconto, valor_desconto, preco_final = p.var('preco'), p.var('desconto'), p.var('valor_desconto'), p.var('preco_final')
    p.script(p.bandeira(), [
        p.pergunte('Preço do produto (R$):'), p.mude(preco, p.resposta()),
        p.pergunte('Desconto (%):'), p.mude(desconto, p.resposta()),
        p.mude(valor_desconto, p.op('divide', p.op('multiply', preco, desconto), 100)),
        p.mude(preco_final, p.op('subtract', preco, valor_desconto)),
        p.diga(p.junte('Preço final: R$ ', p.op('divide', p.arredonde(p.op('multiply', preco_final, 100)), 100)), 3)])
    return 'Entrada e saída: "pergunte" + "resposta" equivalem a input(). Arredondar (×100 ÷100) deixa 2 casas decimais.'

def aula08(p):
    idade, titulo = p.var('idade'), p.var('tem_titulo')
    p.script(p.bandeira(), [
        p.pergunte('Qual é a sua idade?'), p.mude(idade, p.resposta()),
        p.pergunte('Tem título de eleitor? (s/n)'), p.mude(titulo, p.resposta()),
        p.diga(p.junte('Voto facultativo: ', p.e(p.compara('gt', idade, 15), p.compara('lt', idade, 18))), 3),
        p.diga(p.junte('Pode votar: ', p.e(p.compara('equals', titulo, 's'), p.compara('gt', idade, 15))), 3)])
    return 'Expressões lógicas: os blocos hexagonais "e", "ou" e "não" dão verdadeiro (true) ou falso (false). Idade > 15 é o mesmo que idade >= 16.'

def aula09(p):
    n1, n2, media = p.var('nota1'), p.var('nota2'), p.var('media')
    p.script(p.bandeira(), [
        p.pergunte('Nota 1:'), p.mude(n1, p.resposta()),
        p.pergunte('Nota 2:'), p.mude(n2, p.resposta()),
        p.mude(media, p.op('divide', p.op('add', n1, n2), 2)),
        p.se_senao(p.nao(p.compara('lt', media, 7)),
                   [p.diga(p.junte('Aprovado com média ', media), 3)],
                   [p.diga(p.junte('Reprovado com média ', media), 3)])])
    return 'Decisão com "se ... então ... senão". "Não (média < 7)" é o mesmo que média >= 7.'

def aula10(p):
    nota = p.var('nota')
    def conceito(c): return [p.diga('Conceito ' + c, 3)]
    p.script(p.bandeira(), [
        p.pergunte('Nota (0 a 10):'), p.mude(nota, p.resposta()),
        p.se_senao(p.ou(p.compara('lt', nota, 0), p.compara('gt', nota, 10)), [p.diga('Nota inválida', 3)], [
            p.se_senao(p.nao(p.compara('lt', nota, 9)), conceito('A'), [
                p.se_senao(p.nao(p.compara('lt', nota, 7)), conceito('B'), [
                    p.se_senao(p.nao(p.compara('lt', nota, 5)), conceito('C'), conceito('D'))])])])])
    return 'Decisões encadeadas: cada "senão" contém o próximo "se", como o elif do Python.'

def aula13(p):
    numero = p.var('numero')
    p.script(p.bandeira(), [
        p.mude(numero, 10),
        p.repita(10, [p.diga(numero, 1), p.adicione(numero, -1)]),
        p.diga('Lançar!', 2)])
    return 'Repetição: "repita 10 vezes" equivale a for ... in range(10). A variável diminui 1 a cada volta.'

def aula16(p):
    saldo, taxa, objetivo, meses = p.var('saldo'), p.var('taxa'), p.var('objetivo'), p.var('meses')
    p.script(p.bandeira(), [
        p.pergunte('Valor aplicado (R$):'), p.mude(saldo, p.resposta()),
        p.pergunte('Rendimento ao mês (%):'), p.mude(taxa, p.resposta()),
        p.mude(objetivo, p.op('multiply', 2, saldo)), p.mude(meses, 0),
        p.repita_ate(p.nao(p.compara('lt', saldo, objetivo)), [
            p.mude(saldo, p.op('add', saldo, p.op('divide', p.op('multiply', saldo, taxa), 100))),
            p.adicione(meses, 1)]),
        p.diga(p.junte_varios('O valor dobra em ', meses, ' meses'), 4)])
    return '"Repita até que" para quando a condição fica verdadeira; o while do Python repete enquanto a condição é verdadeira.'

def aula17(p):
    caras = p.var('caras')
    p.script(p.bandeira(), [
        p.mude(caras, 0),
        p.repita(1000, [p.se(p.compara('equals', p.aleatorio(0, 1), 1), [p.adicione(caras, 1)])]),
        p.diga(p.junte_varios('Caras em 1000 lançamentos: ', caras), 4)])
    return 'Números aleatórios: 0 = coroa, 1 = cara. O contador "caras" deve ficar perto de 500.'

def aula18(p):
    secreto, palpite, tentativas = p.var('secreto'), p.var('palpite'), p.var('tentativas')
    p.script(p.bandeira(), [
        p.mude(secreto, p.aleatorio(1, 100)), p.mude(tentativas, 0), p.mude(palpite, 0),
        p.repita_ate(p.compara('equals', palpite, secreto), [
            p.pergunte('Seu palpite (1 a 100):'), p.mude(palpite, p.resposta()), p.adicione(tentativas, 1),
            p.se(p.compara('lt', palpite, secreto), [p.diga('O número secreto é MAIOR', 1)]),
            p.se(p.compara('gt', palpite, secreto), [p.diga('O número secreto é MENOR', 1)])]),
        p.diga(p.junte_varios('Acertou em ', tentativas, ' tentativas!'), 4)])
    return 'Jogo de adivinhação: sorteio, repetição até acertar e dicas com "se". Esconda a variável "secreto" do palco antes de jogar!'

def aula26(p):
    nomes = p.lista('nomes')
    contador = p.var('contador')
    p.script(p.bandeira(), [
        p.apague_lista(nomes), p.mude(contador, 1),
        p.repita(5, [p.pergunte(p.junte('Nome do colega ', contador)), p.insira(nomes, p.resposta()), p.adicione(contador, 1)]),
        p.diga(p.junte('Primeiro: ', p.item(nomes, 1)), 2),
        p.diga(p.junte('Último: ', p.item(nomes, 'last')), 2),
        p.diga(p.junte('Quantidade: ', p.tamanho(nomes)), 2)])
    return 'Listas: no Scratch o primeiro item é a posição 1; no Python é a posição 0.'

def aula30(p):
    area = p.var('area')
    ret = p.definir('área do retângulo %s por %s', ['largura', 'comprimento'],
                    [p.mude(area, p.op('multiply', p.parametro('largura'), p.parametro('comprimento')))])
    p.script(p.bandeira(), [
        p.chame(ret, [5, 4]),
        p.diga(p.junte_varios('Área: ', area, ' m²'), 3)])
    return 'Meus Blocos: o bloco criado recebe largura e comprimento (parâmetros) e guarda o resultado na variável "area", já que blocos do Scratch não devolvem valor como o return do Python.'

projetos = {3: aula03, 4: aula04, 6: aula06, 8: aula08, 9: aula09, 10: aula10,
            13: aula13, 16: aula16, 17: aula17, 18: aula18, 26: aula26, 30: aula30}

if __name__ == "__main__":  # uso: python3 _tools/infobasica/gerar_scratch.py <raiz do site>
    site = sys.argv[1]
    destino = os.path.join(site, 'assets/infobasica/scratch')
    os.makedirs(destino, exist_ok=True)
    for n, f in projetos.items():
        p = Projeto(f'aula{n:02d}')
        comentario = f(p)
        p.salvar(os.path.join(destino, f'aula{n:02d}.sb3'), f'Aula {n}. {comentario}')
    print('ok', sorted(projetos))
