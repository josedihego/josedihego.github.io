"""Bloco 3 – Dicionários: hash e árvores (aulas 19 a 27)."""

AULA_19 = dict(
    n=19, bloco=3, tema='Tabelas hash com encadeamento', curto='Hash com encadeamento',
    cormen='seções 11.1 e 11.2',
    objetivos=['Explicar endereçamento direto e por que ele não escala',
               'Resolver colisões por encadeamento',
               'Analisar a busca em função do fator de carga $\\alpha = n/m$',
               'Medir $\\alpha$ e $1 + \\alpha/2$ elementos examinados por busca'],
    roteiro=['Dicionários, endereçamento direto, hash, colisões e o teorema 11.1/11.2',
             'Frequência de palavras com uma tabela hash em C',
             'Custo de busca com e sem sucesso para $\\alpha$ de 0,25 a 4',
             'Bancos de dados, compiladores, redes e cache distribuído'],
    teoria=[
        dict(titulo='Dicionários e endereçamento direto', fig='11.1', altura=0.55,
             legenda='tabela de endereçamento direto: a chave é o próprio índice.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Dicionário}: \Nome{Insert}, \Nome{Search}, \Nome{Delete}.
\item Se as chaves vêm de um universo pequeno $U = \{0, \dots, m-1\}$, use um vetor: $T[k]$ guarda a chave $k$.
\item Tudo em $O(1)$ no pior caso.
\item Problema: o universo costuma ser enorme (CPFs, URLs, palavras) e o conjunto $K$ de chaves usadas, pequeno. Memória $|U|$ é inviável.
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Funções hash e colisões', fig='11.2', altura=0.55,
             legenda='$h$ leva o universo $U$ para $m$ posições; $k_2$ e $k_5$ colidem.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Uma \textbf{função hash} $h: U \to \{0, \dots, m-1\}$ diz onde guardar cada chave.
\item Memória $\Theta(|K|)$ em vez de $\Theta(|U|)$.
\item Como $|U| > m$, \textbf{colisões} são inevitáveis (princípio da casa dos pombos).
\item Duas soluções: encadeamento (hoje) e endereçamento aberto (aula 21).
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Encadeamento', fig='11.3', altura=0.55,
             legenda='cada posição guarda uma lista com as chaves que caíram nela.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \Nome{Insert}($T, x$): insere na cabeça da lista $T[h(x.\mathit{chave})]$: $O(1)$.
\item \Nome{Search}($T, k$): percorre a lista $T[h(k)]$.
\item \Nome{Delete}($T, x$): $O(1)$ com listas duplamente ligadas.
\item Pior caso: todas as chaves na mesma lista, $\Theta(n)$.
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Análise: o fator de carga',
             texto=r'''\textbf{Hash uniforme simples:} cada chave cai em qualquer das $m$ posições com a mesma probabilidade, independentemente das outras. Seja $\alpha = n/m$ o \textbf{fator de carga}.
\begin{itemize}\setlength{\itemsep}{6pt}
\item \textbf{Teorema 11.1} (sem sucesso): a busca examina em média $\alpha$ elementos; tempo $\Theta(1 + \alpha)$.
\item \textbf{Teorema 11.2} (com sucesso): examina em média $1 + \frac{\alpha}{2} - \frac{\alpha}{2n}$ elementos.
\item Se $m$ cresce junto com $n$ ($n = O(m)$), então $\alpha = O(1)$ e \textbf{todas as operações são $O(1)$ em média}.
\end{itemize}''',
             rodape=r'Na prática: dobre $m$ (e reinsira tudo) quando $\alpha$ passar de um limite, como no vetor dinâmico da aula 16: custo amortizado $O(1)$.'),
    ],
    pratica=dict(
        resumo=['Hash de strings: polinômio em base 31, resto por $m = 101$ (primo)', 'Listas na cabeça; busca antes de inserir para contar repetições',
                'Ao fim: palavras, posições usadas e a maior lista'],
        arquivos=[('aula19_hash_encadeamento.c', 'Frequência de palavras com hash')]),
    experimento=dict(
        programa='aula19_experimento.c', titulo='O fator de carga decide',
        pergunta='Quantos elementos uma busca examina, com e sem sucesso, em função do fator de carga α?',
        resumo=['Hipótese: $\\alpha$ (sem sucesso) e $1 + \\alpha/2$ (com sucesso)', '$m = 65.536$, $\\alpha$ de 0,25 a 4',
                'Chaves aleatórias de 32 bits (hash uniforme)'],
        hipotese=r'''Com hash uniforme simples, uma busca \textbf{sem sucesso} percorre uma lista inteira: em média $\alpha$ elementos.
Uma busca \textbf{com sucesso} pela $i$-ésima chave inserida examina ela mesma mais as inseridas depois na mesma lista: em média $1 + \alpha/2$.''',
        metodo=['$m = 2^{16}$ posições, $n = \\alpha m$ chaves aleatórias', '$\\alpha = 0{,}25, 0{,}5, \\dots, 4$',
                'Com sucesso: busca de todas as $n$ chaves', 'Sem sucesso: 200.000 chaves sorteadas'],
        graficos=[
            dict(titulo='Elementos examinados por busca', x='alfa', xlabel='fator de carga $\\alpha$', ylabel='elementos examinados',
                 series=[dict(col='sem_sucesso', rotulo='sem sucesso'), dict(col='com_sucesso', rotulo='com sucesso')],
                 teoria=[dict(col='sem_sucesso', f='n', rotulo='$\\alpha$', ajustar=False, tolerancia=0.02),
                         dict(col='com_sucesso', f='1 + n/2', rotulo='$1 + \\alpha/2$', ajustar=False, tolerancia=0.02)],
                 leitura=r'As duas retas se cruzam em $\alpha = 2$: acima disso, procurar algo que não existe custa mais que achar.'),
        ],
        conclusao=r'''Os teoremas 11.1 e 11.2 se confirmam com desvio menor que 1\%: $\alpha$ elementos sem sucesso, $1 + \alpha/2$ com sucesso.
O custo depende de $\alpha$, \textbf{não de $n$}: com $\alpha$ fixo, uma tabela com um bilhão de chaves busca tão rápido quanto uma com mil.'''),
    conexoes=[
        ('\\faDatabase', 'Bancos de dados', 'Índices hash respondem \\texttt{WHERE id = ?} em $O(1)$; o \\emph{hash join} monta uma tabela hash com a menor relação e varre a maior.'),
        ('\\faCogs', 'Compiladores e linguagens', 'A tabela de símbolos guarda identificadores numa tabela hash; dicionários do Python, objetos do JavaScript e \\texttt{HashMap} do Java também.'),
        ('\\faServer', 'Cache distribuído', 'Memcached e Redis distribuem chaves entre servidores com hash; o \\emph{hashing consistente} minimiza as chaves movidas quando um servidor entra ou sai.'),
        ('\\faNetworkWired', 'Redes', 'Switches mantêm a tabela de endereços MAC em hash; roteadores e firewalls classificam fluxos (5-tupla) por hash para decidir em nanossegundos.'),
    ],
    exercicios=['(11.1-1) Como achar o máximo numa tabela de endereçamento direto? Qual o custo?',
                '(11.2-2) Insira 5, 28, 19, 15, 20, 33, 12, 17, 10 com $h(k) = k \\bmod 9$ e encadeamento.',
                '(11.2-3) E se as listas forem mantidas ordenadas? O que muda em cada operação?',
                'Rode \\texttt{aula19\\_hash\\_encadeamento.c} com um livro inteiro (Domínio Público) e analise a maior lista.',
                'Implemente o redimensionamento: dobre $m$ quando $\\alpha > 1$ e meça o custo amortizado.'],
    leitura='Cormen et al., seções 11.1 e 11.2.',
)

AULA_20 = dict(
    n=20, bloco=3, tema='Funções hash e hashing universal', curto='Funções hash',
    cormen='seção 11.3',
    objetivos=['Construir funções hash pelos métodos da divisão e da multiplicação',
               'Reconhecer escolhas ruins de $m$ (potências de 2 com chaves estruturadas)',
               'Definir hashing universal e o que ele garante',
               'Medir o efeito da função hash em chaves com padrão'],
    roteiro=['O que é uma boa função hash; divisão, multiplicação, família universal',
             'Quantas posições cada função usa com chaves múltiplas de 64',
             'Quatro funções, chaves com padrão, fator de carga 1',
             'Segurança, sistemas distribuídos, big data e criptografia'],
    teoria=[
        dict(titulo='O que é uma boa função hash',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Ideal: \textbf{hash uniforme simples}, cada chave igualmente provável em cada posição, independente das demais.
\item Na prática não conhecemos a distribuição das chaves, e elas têm \textbf{padrões}: endereços alinhados, IDs sequenciais, nomes com mesmo prefixo.
\item Interpretar chaves como números naturais: uma string vira $\sum c_i\,b^i$ (base $b$).
\item Uma boa função usa \textbf{todos os bits} da chave e espalha padrões regulares.
\end{itemize}'''),
        dict(titulo='Método da divisão',
             texto=r'''\[h(k) = k \bmod m\]
\begin{itemize}\setlength{\itemsep}{5pt}
\item Rápido: uma divisão.
\item \textbf{Evite $m = 2^p$}: $h(k)$ seria só os $p$ bits menos significativos. Chaves múltiplas de 64 cairiam em apenas $m/64$ posições.
\item Escolha $m$ \textbf{primo} longe de potências de 2. Exemplo: $n = 2000$ strings, até 3 por lista: $m = 701$.
\item Chaves em progressão aritmética $s, 2s, 3s, \dots$ com $m$ primo (e $s$ não múltiplo de $m$) ocupam \textbf{todas} as posições.
\end{itemize}'''),
        dict(titulo='Método da multiplicação',
             texto=r'''\[h(k) = \lfloor m\,(kA \bmod 1)\rfloor, \qquad 0 < A < 1\]
\begin{itemize}\setlength{\itemsep}{5pt}
\item O valor de $m$ não é crítico: pode ser $2^p$.
\item Implementação com palavras de $w$ bits: $s = \lfloor A \cdot 2^w\rfloor$; $h(k)$ = os $p$ bits mais altos de $(k\,s) \bmod 2^w$. Uma multiplicação e um deslocamento.
\item Knuth sugere $A \approx (\sqrt5 - 1)/2 = 0{,}618\dots$ (razão áurea): \emph{hashing de Fibonacci}.
\end{itemize}''',
             rodape=r'Em C, com \texttt{unsigned} de 32 bits: \texttt{(k * 2654435769u) >> (32 - p)}.'),
        dict(titulo='Hashing universal',
             texto=r'''Qualquer função fixa tem um conjunto de $n$ chaves que cai todo na mesma posição. Um adversário pode escolhê-lo.

\medskip\textbf{Solução:} sortear a função, no início da execução, de uma família $\mathcal H$.
\begin{itemize}\setlength{\itemsep}{4pt}
\item $\mathcal H$ é \textbf{universal} se, para $k \ne l$, no máximo $|\mathcal H|/m$ funções fazem $h(k) = h(l)$: probabilidade de colisão $\le 1/m$.
\item \textbf{Teorema 11.3:} com encadeamento, a lista esperada de uma chave tem tamanho $\le 1 + \alpha$, para \textbf{qualquer} conjunto de chaves.
\item Família do livro: $h_{ab}(k) = ((ak + b) \bmod p) \bmod m$, $p$ primo maior que as chaves, $a \in [1, p-1]$, $b \in [0, p-1]$.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Chaves $s, 2s, \\dots, ms$ (padrão comum)', 'Divisão por $m$, divisão por um primo, multiplicação',
                'Conta quantas posições cada função ocupa'],
        arquivos=[('aula20_funcoes_hash.c', 'Comparando funções hash')]),
    experimento=dict(
        programa='aula20_experimento.c', titulo='Chaves com padrão',
        pergunta='Com chaves múltiplas de 64 e fator de carga 1, quanto custa uma busca com cada função hash?',
        resumo=['Chaves $64, 128, \\dots, 64m$ e $n = m$ (fator de carga 1)', 'Divisão por $2^p$, divisão por primo, multiplicação, universal',
                'Universal: média sobre muitas funções sorteadas'],
        hipotese=r'''Com $m = 2^p$, o método da divisão só vê os bits baixos: múltiplos de 64 caem em $m/64$ posições, listas de 64, custo médio $(64+1)/2 = 32{,}5$.
Com $m$ primo, a progressão ocupa todas as posições: custo 1. O hashing universal garante em média no máximo $1 + \alpha/2 = 1{,}5$, para \textbf{qualquer} conjunto de chaves.''',
        metodo=['$m = 2^{10}, \\dots, 2^{18}$ e $n = m$ chaves $64i$', 'Custo médio de busca com sucesso: $\\sum L(L+1)/2 \\,/\\, n$',
                'Primo: o menor primo maior que $m$', 'Universal: média de $2^{26}/n$ funções $h_{ab}$ sorteadas'],
        graficos=[
            dict(titulo='Custo médio de busca com sucesso', ylabel='elementos examinados', escala='log',
                 series=[dict(col='div_pot2', rotulo='divisão por $2^p$'), dict(col='multiplicacao', rotulo='multiplicação'),
                         dict(col='universal', rotulo='universal (média)'), dict(col='div_primo', rotulo='divisão por primo')],
                 teoria=[dict(col='universal', f='1.5', rotulo='$1 + \\alpha/2$', ajustar=False, tolerancia=0.08),
                         dict(col='div_pot2', f='32.5', rotulo='$65/2$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Divisão por $2^p$: 32,5 em todos os tamanhos. Primo: 1 (perfeito). Universal: 1,5 em média. Multiplicação: entre 1 e 2, conforme $m$.'),
        ],
        conclusao=r'''A escolha da função muda o custo em mais de \textbf{30 vezes} com as mesmas chaves: dividir por potência de 2 dá exatamente 32,5; dividir por um primo dá 1.
O hashing universal fica em 1,5 em média, como garante o teorema, \textbf{sem depender} das chaves. Uma função isolada sorteada, porém, pode ter azar: a garantia é sobre a média da família.'''),
    conexoes=[
        ('\\faUserSecret', 'Segurança', 'Em 2011, ataques de \\emph{hash flooding} derrubaram servidores web enviando parâmetros que colidiam; Python, Ruby e Java passaram a sortear a função (SipHash).'),
        ('\\faServer', 'Sistemas distribuídos', 'Hashing consistente (Dynamo, Cassandra) e \\emph{rendezvous hashing} decidem qual servidor guarda cada chave; uma função ruim desequilibra o cluster.'),
        ('\\faChartBar', 'Big data', 'Contagem aproximada (HyperLogLog), filtros de Bloom e \\emph{count-min sketch} dependem de funções hash independentes e bem espalhadas.'),
        ('\\faKey', 'Criptografia', 'Hashes criptográficos (SHA-256) vão além: resistência a colisões e a pré-imagem. Senhas, assinaturas e blockchain dependem disso.'),
    ],
    exercicios=['(11.3-1) Busca numa lista de strings longas com hash armazenado: como usar o hash para acelerar?',
                '(11.3-3) Mostre que, com $m = 2^p - 1$ e strings em base $2^p$, permutar caracteres não muda o hash.',
                '(11.3-4) Calcule as posições de 61, 62, 63, 64, 65 com $m = 1000$ e $A = (\\sqrt5 - 1)/2$.',
                'Rode \\texttt{aula20\\_funcoes\\_hash.c} com passos 1, 10, 64 e 1000. Qual função é robusta?',
                'Meça o custo de \\textbf{uma} função universal sorteada várias vezes: qual a pior que você encontra?'],
    leitura='Cormen et al., seção 11.3.',
)

AULA_21 = dict(
    n=21, bloco=3, tema='Endereçamento aberto', curto='Endereçamento aberto',
    cormen='seção 11.4',
    objetivos=['Guardar todas as chaves no próprio vetor, sem listas',
               'Comparar sondagem linear, quadrática e hash duplo',
               'Explicar por que a remoção exige marcas',
               'Medir as sondagens e confrontar com $1/(1-\\alpha)$ e com a fórmula de Knuth'],
    roteiro=['Sequência de sondagem, hash duplo, teoremas 11.6 e 11.8',
             'Hash duplo com remoção por marca em C',
             'Sondagens: linear contra duplo, de $\\alpha = 0{,}05$ a $0{,}9$',
             'Hardware, sistemas embarcados, linguagens e bancos de dados'],
    teoria=[
        dict(titulo='Sem listas: sondar a própria tabela',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Todas as chaves ficam no vetor $T[0..m-1]$: $\alpha = n/m \le 1$.
\item Para inserir $k$, testa-se a \textbf{sequência de sondagem} $h(k, 0), h(k, 1), \dots$ até achar uma posição vazia.
\item A busca segue a mesma sequência até achar $k$ ou uma posição \textbf{vazia}.
\item \textbf{Linear:} $h(k, i) = (h'(k) + i) \bmod m$. Simples, amigável ao cache, mas forma \textbf{aglomerados}.
\item \textbf{Quadrática:} $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \bmod m$.
\item \textbf{Hash duplo:} $h(k, i) = (h_1(k) + i\,h_2(k)) \bmod m$, com $h_2(k)$ primo com $m$ para visitar todas as posições.
\end{itemize}'''),
        dict(titulo='Hash duplo', fig='11.5', altura=0.5,
             legenda='inserção de 14 com $h_1(k) = k \\bmod 13$ e $h_2(k) = 1 + (k \\bmod 11)$: sondagens 1, 5 e 9.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item $h_1$ escolhe o início; $h_2$, o \textbf{passo}.
\item Chaves com o mesmo início seguem caminhos diferentes: os aglomerados somem.
\item $m$ primo e $h_2(k) \in [1, m-1]$, ou $m = 2^p$ e $h_2(k)$ ímpar.
\item $\Theta(m^2)$ sequências diferentes, contra $\Theta(m)$ da linear.
\end{itemize}''', largura_texto=0.46),
        dict(titulo='Quantas sondagens?',
             texto=r'''Com \textbf{hash uniforme} (cada sequência de sondagem igualmente provável):
\begin{itemize}\setlength{\itemsep}{6pt}
\item \textbf{Teorema 11.6} (sem sucesso): no máximo $\dfrac{1}{1 - \alpha}$ sondagens. Com $\alpha = 0{,}9$: 10.
\item \textbf{Teorema 11.8} (com sucesso): no máximo $\dfrac{1}{\alpha}\ln\dfrac{1}{1 - \alpha}$. Com $\alpha = 0{,}9$: 2,56.
\item \textbf{Sondagem linear} (Knuth): $\frac12\big(1 + \frac{1}{(1-\alpha)^2}\big)$ sem sucesso e $\frac12\big(1 + \frac{1}{1-\alpha}\big)$ com sucesso. Com $\alpha = 0{,}9$: 50,5 e 5,5.
\end{itemize}''',
             rodape=r'\textbf{Remoção:} não se pode esvaziar a posição (a busca pararia antes da hora). Usa-se uma marca \textsc{removida}, que a busca pula e a inserção reaproveita.'),
    ],
    pratica=dict(
        resumo=['Tabela de 13 posições, como na Figura 11.5', '$h_2(k) = 1 + (k \\bmod 11)$: nunca zero, primo com 13',
                'Marca \\texttt{REMOVIDA} para a remoção'],
        arquivos=[('aula21_enderecamento_aberto.c', 'Hash duplo em C')]),
    experimento=dict(
        programa='aula21_experimento.c', titulo='Linear contra hash duplo',
        pergunta='Quantas sondagens fazem a sondagem linear e o hash duplo, com e sem sucesso, para α de 0,05 a 0,9?',
        resumo=['$m = 2^{20}$ posições, chaves aleatórias', 'Hash duplo com passo ímpar (primo com $2^{20}$)',
                'Teoremas 11.6 e 11.8 e as fórmulas de Knuth para a linear'],
        hipotese=r'''O hash duplo se comporta quase como hash uniforme: $1/(1-\alpha)$ sondagens sem sucesso e $\frac1\alpha\ln\frac1{1-\alpha}$ com sucesso.
A sondagem linear sofre com aglomerados: $\frac12(1 + 1/(1-\alpha)^2)$ sem sucesso, \textbf{muito pior} quando a tabela enche.''',
        metodo=['$m = 2^{20}$; $n = \\alpha m$ chaves de 64 bits sorteadas', '$\\alpha$ de 0,05 a 0,90',
                'Com sucesso: busca de todas as chaves; sem sucesso: 200.000 sorteadas', 'Mesmas chaves para as duas estratégias'],
        graficos=[
            dict(titulo='Busca sem sucesso', x='alfa', xlabel='fator de carga $\\alpha$', ylabel='sondagens', escala='logy',
                 series=[dict(col='linear_sem', rotulo='linear'), dict(col='duplo_sem', rotulo='hash duplo')],
                 teoria=[dict(col='duplo_sem', f='1/(1-n)', rotulo='$\\frac{1}{1-\\alpha}$', ajustar=False, tolerancia=0.03),
                         dict(col='linear_sem', f='0.5*(1 + 1/(1-n)**2)', rotulo='$\\frac12(1+\\frac{1}{(1-\\alpha)^2})$', ajustar=False, tolerancia=0.06)],
                 leitura=r'Com 90\% de ocupação: 10 sondagens no hash duplo, 50 na linear.'),
            dict(titulo='Busca com sucesso', x='alfa', xlabel='fator de carga $\\alpha$', ylabel='sondagens',
                 series=[dict(col='linear_com', rotulo='linear'), dict(col='duplo_com', rotulo='hash duplo')],
                 teoria=[dict(col='duplo_com', f='(1/n)*log(1/(1-n))', rotulo='$\\frac1\\alpha\\ln\\frac{1}{1-\\alpha}$', ajustar=False, tolerancia=0.03),
                         dict(col='linear_com', f='0.5*(1 + 1/(1-n))', rotulo='$\\frac12(1+\\frac{1}{1-\\alpha})$', ajustar=False, tolerancia=0.04)],
                 leitura=r'Com sucesso é mais barato: a chave foi inserida quando a tabela estava mais vazia.'),
        ],
        conclusao=r'''As quatro fórmulas se confirmam com desvios de poucos por cento. Até $\alpha \approx 0{,}5$, linear e duplo empatam; acima disso, os \textbf{aglomerados} da linear explodem o custo.
Regra prática: endereçamento aberto com $\alpha \le 0{,}7$; acima disso, redimensione.''',
        extra=r'A linear ainda é muito usada: suas sondagens são vizinhas na memória e aproveitam o cache (aula 17). Meça o \textbf{tempo}, não só as sondagens.'),
    conexoes=[
        ('\\faMicrochip', 'Hardware', 'Caches de CPU são tabelas hash em hardware: o endereço escolhe o conjunto, e cada conjunto tem poucas ``posições'' (associatividade).'),
        ('\\faRust', 'Linguagens', 'O \\texttt{HashMap} do Rust (SwissTable), o \\texttt{dict} do Python e o \\texttt{absl::flat\\_hash\\_map} do C++ usam endereçamento aberto pela localidade de memória.'),
        ('\\faMicrochip', 'Sistemas embarcados', 'Sem \\texttt{malloc} nem listas: uma tabela de tamanho fixo com endereçamento aberto cabe em memória estática, ideal para microcontroladores.'),
        ('\\faDatabase', 'Bancos de dados', 'Agregações (\\texttt{GROUP BY}) e \\emph{joins} em memória usam tabelas com sondagem linear vetorizada (SIMD) em sistemas analíticos.'),
    ],
    exercicios=['(11.4-1) Insira 10, 22, 31, 4, 15, 28, 17, 88, 59 com $m = 11$: linear, quadrática ($c_1 = 1$, $c_2 = 3$) e duplo.',
                '(11.4-2) Escreva \\Nome{Hash-Delete} com a marca \\textsc{removida} e ajuste \\Nome{Hash-Insert}.',
                '(11.4-3) Calcule as sondagens esperadas para $\\alpha = 3/4$ e $\\alpha = 7/8$.',
                'Acrescente a sondagem quadrática ao experimento. Onde ela fica entre linear e duplo?',
                'Meça o \\textbf{tempo} de busca da linear e do duplo para $\\alpha = 0{,}5$. Quem vence? Por quê?'],
    leitura='Cormen et al., seção 11.4.',
)

AULA_22 = dict(
    n=22, bloco=3, tema='Árvores binárias de busca: percursos e consultas', curto='Árvores binárias de busca',
    cormen='seções 12.1 e 12.2',
    objetivos=['Enunciar a propriedade de árvore binária de busca',
               'Percorrer em ordem, pré-ordem e pós-ordem',
               'Buscar, achar mínimo, máximo, sucessor e predecessor em $O(h)$',
               'Medir o custo médio de busca em árvores aleatórias: $\\approx 1{,}39\\lg n$'],
    roteiro=['Propriedade, percursos, consultas e o papel da altura',
             'ABB em C: inserção, percurso, busca, mínimo, máximo e sucessor',
             'Custo médio de busca contra $2(1 + 1/n)H_n - 3$',
             'Sistemas de arquivos, compiladores, bancos de dados e geometria'],
    teoria=[
        dict(titulo='A propriedade de árvore binária de busca', fig='12.1', altura=0.52,
             legenda='duas ABBs com as mesmas chaves: (a) altura 2; (b) altura 4, menos eficiente.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Cada nó $x$ tem \textit{chave}, \textit{esq}, \textit{dir} e \textit{pai}.
\item \textbf{Propriedade:} se $y$ está na subárvore esquerda de $x$, $y.\mathit{chave} \le x.\mathit{chave}$; se está na direita, $y.\mathit{chave} \ge x.\mathit{chave}$.
\item As operações custam $O(h)$, onde $h$ é a \textbf{altura}.
\item $h$ vai de $\lfloor\lg n\rfloor$ (árvore cheia) a $n - 1$ (uma corrente).
\end{itemize}''', largura_texto=0.46),
        dict(titulo='Percurso em ordem', nome='Inorder-Tree-Walk($x$)',
             pseudo=r'''\If{$x \ne \textsc{nil}$}
\State \Nome{Inorder-Tree-Walk}($x.\mathit{esq}$)
\State imprima $x.\mathit{chave}$
\State \Nome{Inorder-Tree-Walk}($x.\mathit{dir}$)
\EndIf''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Imprime as chaves \textbf{em ordem}: consequência direta da propriedade.
\item \textbf{Teorema 12.1:} $\Theta(n)$ para $n$ nós.
\item Pré-ordem: raiz antes das subárvores (copiar a árvore).
\item Pós-ordem: raiz depois (liberar a memória, avaliar expressões).
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Busca, mínimo, máximo e sucessor', fig='12.2', altura=0.58,
             legenda='busca por 13: $15 \\to 6 \\to 7 \\to 13$. Mínimo: sempre à esquerda (2). Sucessor de 13: 15.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \Nome{Tree-Search}: desce à esquerda ou à direita conforme a chave: $O(h)$.
\item \Nome{Tree-Minimum}: sempre à esquerda. \Nome{Tree-Maximum}: sempre à direita.
\item \Nome{Tree-Successor}($x$): se há subárvore direita, o mínimo dela; senão, suba até chegar por um filho esquerdo.
\item \textbf{Teorema 12.2:} todas $O(h)$.
\end{itemize}''', largura_texto=0.46),
    ],
    pratica=dict(
        resumo=['Nós com ponteiro para o pai (necessário para o sucessor)', 'Percurso em ordem recursivo; busca iterativa',
                'Teste com as chaves da Figura 12.2'],
        arquivos=[('aula22_abb.c', 'Árvore binária de busca em C')]),
    experimento=dict(
        programa='aula22_experimento.c', titulo='Quanto custa buscar numa árvore aleatória?',
        pergunta='Numa ABB construída com chaves em ordem aleatória, quantos nós uma busca com sucesso visita em média?',
        resumo=['Hipótese: $2(1 + 1/n)H_n - 3 \\approx 1{,}39\\lg n$', '$n = 2^{10}$ a $2^{21}$, média de várias árvores',
                'Custo de buscar uma chave = sua profundidade + 1'],
        hipotese=r'''Inserir chaves em ordem aleatória equivale a montar a árvore de recursão do quicksort: cada chave é comparada com seus ancestrais.
O custo médio de uma busca com sucesso é
\[2\Big(1 + \frac1n\Big)H_n - 3 \approx 2\ln n \approx 1{,}39\lg n.\]''',
        metodo=['Chaves de 32 bits sorteadas (xorshift)', 'Profundidade de cada nó registrada na inserção',
                '$n = 2^{10}, \\dots, 2^{21}$', 'Média de 10 árvores (3 para $n > 2^{17}$)'],
        graficos=[
            dict(titulo='Nós visitados por busca', ylabel='nós visitados (média)', escala='logx',
                 series=[dict(col='busca_media', rotulo='medido')],
                 teoria=[dict(col='busca_media', f='2*(1+1/n)*(log(n)+0.5772156649) - 3', rotulo='$2(1+\\frac1n)H_n - 3$', ajustar=False, tolerancia=0.03)],
                 leitura=r'Com $n$ em escala logarítmica, o custo é uma reta: cresce como $\lg n$, cerca de 1,39 nó a cada vez que $n$ dobra.'),
        ],
        conclusao=r'''O custo médio segue $2(1 + 1/n)H_n - 3$ com desvio abaixo de 1\%: para dois milhões de chaves, 27 nós por busca.
Uma árvore aleatória é só 39\% mais funda (em média) que uma perfeitamente balanceada. O perigo está nas entradas \textbf{não} aleatórias (próxima aula).'''),
    conexoes=[
        ('\\faFolderOpen', 'Sistemas de arquivos', 'Diretórios são árvores; ext4 e Btrfs indexam nomes em árvores de busca para achar um arquivo entre milhões sem varrer todos.'),
        ('\\faCogs', 'Compiladores', 'Árvores sintáticas são percorridas em pós-ordem para gerar código e avaliar expressões; o percurso em ordem imprime a expressão infixa.'),
        ('\\faDatabase', 'Bancos de dados', 'Consultas por intervalo (\\texttt{BETWEEN}) usam o sucessor: acha-se o início e anda-se em ordem. Hash não faz isso; árvores fazem.'),
        ('\\faMapMarked', 'Geometria computacional', 'Árvores k-d e de intervalos generalizam a ABB para pontos no plano: ``quais restaurantes estão neste retângulo do mapa?''.'),
    ],
    exercicios=['(12.1-1) Desenhe ABBs de alturas 2, 3, 4, 5 e 6 com as chaves $\\{1, 4, 5, 10, 16, 17, 21\\}$.',
                '(12.1-3) Escreva o percurso em ordem não recursivo, com uma pilha.',
                '(12.2-1) Quais sequências de busca por 363 são impossíveis numa ABB? Por quê?',
                '(12.2-3) Escreva \\Nome{Tree-Predecessor}.',
                'Altere o experimento para medir a busca \\textbf{sem} sucesso. A fórmula muda?'],
    leitura='Cormen et al., seções 12.1 e 12.2.',
)

AULA_23 = dict(
    n=23, bloco=3, tema='Inserção, remoção e altura das árvores de busca', curto='Inserção e remoção em ABB',
    cormen='seções 12.3 e 12.4',
    objetivos=['Inserir mantendo a propriedade de ABB',
               'Remover nos três casos com \\Nome{Transplant}',
               'Entender por que a altura esperada de uma ABB aleatória é $O(\\lg n)$',
               'Medir a altura de árvores aleatórias e o desastre da entrada ordenada'],
    roteiro=['\\Nome{Tree-Insert}, \\Nome{Tree-Delete} e a altura esperada (teorema 12.4)',
             'Inserção e remoção em C',
             'Altura média de árvores aleatórias; chaves em ordem',
             'Bancos de dados, editores, jogos e redes'],
    teoria=[
        dict(titulo='Inserção', nome='Tree-Insert($T, z$)',
             pseudo=r'''\State $y \atrib \textsc{nil}$;\quad $x \atrib T.\mathit{raiz}$
\While{$x \ne \textsc{nil}$}
\State $y \atrib x$ \Comment{$y$ segue $x$ um passo atrás}
\If{$z.\mathit{chave} < x.\mathit{chave}$} \State $x \atrib x.\mathit{esq}$
\Else \State $x \atrib x.\mathit{dir}$ \EndIf
\EndWhile
\State $z.\mathit{pai} \atrib y$
\If{$y = \textsc{nil}$} \State $T.\mathit{raiz} \atrib z$ \Comment{árvore vazia}
\ElsIf{$z.\mathit{chave} < y.\mathit{chave}$} \State $y.\mathit{esq} \atrib z$
\Else \State $y.\mathit{dir} \atrib z$ \EndIf''',
             fig='12.3', legenda='inserção de 13: desce até uma posição vazia e vira folha.',
             texto=r'''Desce como numa busca e pendura $z$ como \textbf{folha}. Custo $O(h)$.''', largura_texto=0.30),
        dict(titulo='Remoção: os três casos', fig='12.4', altura=0.5,
             legenda='(a) sem filho esquerdo; (b) sem filho direito; (c) sucessor é o filho direito; (d) sucessor mais abaixo.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Sem filhos ou um filho:} o filho (ou \textsc{nil}) toma o lugar de $z$.
\item \textbf{Dois filhos:} o \textbf{sucessor} $y$ (mínimo da subárvore direita, que não tem filho esquerdo) toma o lugar de $z$.
\item \Nome{Transplant}($T, u, v$) põe a subárvore $v$ no lugar de $u$.
\item Custo $O(h)$.
\end{itemize}''', largura_texto=0.40),
        dict(titulo='Qual a altura de uma árvore aleatória?',
             texto=r'''Inserindo $n$ chaves distintas em ordem \textbf{aleatória} (todas as $n!$ ordens igualmente prováveis):
\begin{itemize}\setlength{\itemsep}{6pt}
\item \textbf{Teorema 12.4:} a altura esperada é $O(\lg n)$.
\item Ideia da prova: com $Y_n = 2^{h}$ e a raiz escolhida ao acaso, $E[Y_n] \le \frac{4}{n}\sum_{i} E[Y_i] = O(n^3)$; pela desigualdade de Jensen, $E[h] \le 3\lg n + O(1)$.
\item Resultado exato (Reed, 2003): $E[h] \approx 4{,}311\ln n - 1{,}953\ln\ln n \approx 2{,}99\lg n$.
\item Mas a entrada real raramente é aleatória: chaves \textbf{em ordem} geram uma corrente de altura $n - 1$.
\end{itemize}''',
             rodape=r'Solução: árvores que se reequilibram sozinhas, garantindo $h = O(\lg n)$ para \textbf{qualquer} ordem de inserção (aulas 24 e 25).'),
    ],
    pratica=dict(
        resumo=['\\texttt{transplanta}: o coração da remoção', 'Os quatro casos de \\Nome{Tree-Delete}, como no livro',
                'Entrada: chaves e comandos \\texttt{r k}'],
        arquivos=[('aula23_abb_remocao.c', 'Inserção e remoção em ABB')]),
    experimento=dict(
        programa='aula23_experimento.c', titulo='Altura: ordem aleatória contra ordem crescente',
        pergunta='Qual a altura de uma ABB com chaves aleatórias? E com chaves em ordem crescente?',
        resumo=['Aleatória: altura entre $\\lg n$ e $3\\lg n$ (teorema 12.4)', 'Ordenada: exatamente $n - 1$',
                '$n$ até $2^{21}$, média de 10 árvores'],
        hipotese=r'''Com chaves aleatórias, a altura deve ficar entre o mínimo possível, $\lg n$, e o limite da prova, $3\lg n$, aproximando-se de $\approx 2{,}99\lg n$ bem devagar.
Com chaves em ordem crescente, cada chave vira filho direito da anterior: altura exatamente $n - 1$.''',
        metodo=['Altura registrada durante as inserções', 'Aleatória: $n = 2^{10}, \\dots, 2^{21}$, média de 10 árvores',
                'Ordenada: $n$ de 500 a 8.000', 'Verificação dos limites em todos os pontos'],
        graficos=[
            dict(titulo='Altura de árvores aleatórias', ylabel='altura (média)', escala='logx',
                 series=[dict(col='altura_media', rotulo='medido')],
                 teoria=[dict(col='altura_media', f='3*log2(n)', rotulo='$3\\lg n$', limite='superior'),
                         dict(col='altura_media', f='log2(n)', rotulo='$\\lg n$', limite='inferior')],
                 leitura=r'A razão altura$/\lg n$ sobe devagar (2,2 para 2,6) rumo ao valor assintótico 2,99.'),
            dict(titulo='Chaves em ordem: uma corrente', tabela=1, ylabel='altura',
                 series=[dict(col='ordenada', rotulo='medido')],
                 teoria=[dict(col='ordenada', f='n-1', rotulo='$n-1$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Altura $n - 1$: a árvore é uma lista ligada, e todas as operações viram $\Theta(n)$.'),
        ],
        conclusao=r'''Com chaves aleatórias, a altura fica sempre entre $\lg n$ e $3\lg n$: para dois milhões de chaves, cerca de 54 níveis.
Com chaves em ordem, exatamente $n - 1$: dois milhões de níveis. \textbf{A mesma estrutura, com a mesma quantidade de dados, fica 40.000 vezes mais funda} só pela ordem de chegada.'''),
    conexoes=[
        ('\\faDatabase', 'Bancos de dados', 'Chaves autoincrementadas chegam \\emph{em ordem}: é exatamente o pior caso de uma ABB comum. Por isso bancos usam árvores balanceadas (B-trees).'),
        ('\\faEdit', 'Editores e cordas', 'Editores de texto grandes guardam o documento numa árvore de trechos (\\emph{rope}); inserir e remover no meio custa $O(h)$.'),
        ('\\faGamepad', 'Jogos', 'Placares (\\emph{leaderboards}) mantêm jogadores ordenados por pontuação com inserção e remoção constantes; a altura define a latência.'),
        ('\\faNetworkWired', 'Redes', 'Tabelas de roteamento e de temporizadores de conexões TCP mudam o tempo todo: remoções e inserções eficientes são essenciais.'),
    ],
    exercicios=['(12.3-1) Escreva \\Nome{Tree-Insert} recursivo.',
                '(12.3-3) Ordene $n$ números inserindo-os numa ABB e percorrendo em ordem. Pior e melhor caso?',
                '(12.3-4) A remoção é ``comutativa''? Remover $x$ e depois $y$ dá a mesma árvore que $y$ e depois $x$?',
                'Mostre que existe ABB aleatória com altura média maior que a esperada, e explique por que isso não contradiz o teorema.',
                'Altere o experimento: insira as chaves quase em ordem (1\\% trocadas). Qual a altura?'],
    leitura='Cormen et al., seções 12.3 e 12.4.',
)

AULA_24 = dict(
    n=24, bloco=3, tema='Árvores AVL', curto='Árvores AVL',
    cormen='problema 13-3 e seção 13.2 (rotações)',
    objetivos=['Definir o fator de balanceamento AVL',
               'Aplicar rotações simples e duplas',
               'Provar que a altura de uma AVL é $O(\\lg n)$ (árvores de Fibonacci)',
               'Medir a altura com chaves em ordem e o número de rotações por inserção'],
    roteiro=['Balanceamento, rotações, os quatro casos, altura máxima',
             'AVL em C com altura em cada nó',
             'Altura com chaves em ordem e aleatórias; rotações por inserção',
             'Bancos em memória, sistemas de tempo real, linguagens e roteamento'],
    teoria=[
        dict(titulo='Balanceamento de altura',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item Adelson-Velsky e Landis (1962): a primeira árvore de busca autobalanceada.
\item Cada nó guarda sua \textbf{altura} $h(x)$ (folha: 0; \textsc{nil}: $-1$).
\item \textbf{Propriedade AVL:} em todo nó, as alturas das subárvores esquerda e direita diferem de no máximo 1.
\item Fator de balanceamento: $b(x) = h(x.\mathit{esq}) - h(x.\mathit{dir}) \in \{-1, 0, 1\}$.
\item Depois de inserir, sobe-se pelo caminho atualizando alturas; onde $|b| = 2$, \textbf{rotaciona}.
\end{itemize}'''),
        dict(titulo='Rotações', fig='13.2', altura=0.45,
             legenda='rotação à esquerda em $x$ e à direita em $y$: mudam a forma e preservam a ordem $\\alpha < x < \\beta < y < \\gamma$.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Uma rotação troca a posição de pai e filho mexendo em $O(1)$ ponteiros.
\item A propriedade de ABB se mantém.
\item Uma subárvore sobe um nível, outra desce.
\end{itemize}''', largura_texto=0.36),
        dict(titulo='Os quatro casos',
             texto=r'''Seja $x$ o nó mais baixo desbalanceado após inserir:
\medskip\renewcommand{\arraystretch}{1.4}\begin{tabular}{lll}\toprule \textbf{Caso} & \textbf{Situação} & \textbf{Correção}\\\midrule
esquerda-esquerda & $b(x) = 2$, inserção na subárvore esq. do filho esq. & rotação à direita em $x$\\
direita-direita & $b(x) = -2$, na subárvore dir. do filho dir. & rotação à esquerda em $x$\\
esquerda-direita & $b(x) = 2$, na subárvore dir. do filho esq. & esquerda no filho, direita em $x$\\
direita-esquerda & $b(x) = -2$, na subárvore esq. do filho dir. & direita no filho, esquerda em $x$\\\bottomrule\end{tabular}

\medskip Exemplos (slides antigos): inserir 7, 9, 11 (DD); 10, 6, 2 (EE); 9, 4, 7 (ED); 15, 20, 18 (DE).''',
             rodape=r'Na inserção, \textbf{uma} rotação (simples ou dupla) restaura todo o caminho: a subárvore volta à altura que tinha antes.'),
        dict(titulo='Por que a altura é $O(\\lg n)$',
             texto=r'''Seja $N_h$ o \textbf{menor} número de nós de uma AVL de altura $h$ (problema 13-3a). A árvore mais magra tem uma subárvore de altura $h-1$ e outra de altura $h-2$:
\[N_h = N_{h-1} + N_{h-2} + 1, \qquad N_0 = 1,\; N_1 = 2\]
Então $N_h = F_{h+3} - 1$ (Fibonacci), e $F_k \approx \varphi^k/\sqrt5$ com $\varphi = 1{,}618\dots$:
\[n \ge N_h \approx \varphi^{h} \quad\Longrightarrow\quad h \le \log_\varphi n \approx 1{,}44\lg(n + 2) - 0{,}328\]''',
             rodape=r'AVL é mais rigidamente balanceada que a rubro-negra ($1{,}44\lg n$ contra $2\lg n$): buscas um pouco mais rápidas, inserções e remoções com mais rotações.'),
    ],
    pratica=dict(
        resumo=['Altura guardada em cada nó; \\texttt{balanceia} na volta da recursão', 'Rotação dupla = duas rotações simples',
                'Testes: os quatro casos dos slides antigos'],
        arquivos=[('aula24_avl.c', 'Árvore AVL em C')]),
    experimento=dict(
        programa='aula24_experimento.c', titulo='AVL contra a ordem de chegada',
        pergunta='Qual a altura de uma AVL com chaves em ordem e com chaves aleatórias? Quantas rotações custa cada inserção?',
        resumo=['Chaves em ordem: a ABB comum teria altura $n - 1$', 'Limite: $1{,}44\\lg(n+2) - 0{,}328$',
                'Rotações por inserção, chaves aleatórias'],
        hipotese=r'''Com chaves em ordem, a AVL deve ficar \textbf{perfeitamente} balanceada: altura $\lg n$ (para $n = 2^k$).
Com chaves aleatórias, a altura deve respeitar $1{,}44\lg(n+2) - 0{,}328$. E as rotações por inserção devem ser \textbf{constantes}, independentes de $n$.''',
        metodo=['$n = 2^{10}, \\dots, 2^{21}$', 'Verificação da propriedade AVL em todos os nós (aborta se falhar)',
                'Contador de rotações simples (dupla conta 2)', 'Mesmo código para os dois tipos de entrada'],
        graficos=[
            dict(titulo='Altura da AVL', ylabel='altura', escala='logx',
                 series=[dict(col='avl_aleatoria', rotulo='chaves aleatórias'), dict(col='avl_ordenada', rotulo='chaves em ordem')],
                 teoria=[dict(col='avl_ordenada', f='log2(n)', rotulo='$\\lg n$', ajustar=False, tolerancia=0.0001),
                         dict(col='avl_aleatoria', f='1.44*log2(n+2) - 0.328', rotulo='$1{,}44\\lg(n+2)-0{,}328$', limite='superior')],
                 leitura=r'Em ordem: exatamente $\lg n$, uma árvore perfeita. Aleatórias: cerca de $\lg n + 3$, bem abaixo do limite.'),
            dict(titulo='Rotações por inserção', ylabel='rotações por inserção', escala='logx', opcoes='ymin=0,ymax=1',
                 series=[dict(col='rotacoes', rotulo='chaves aleatórias')],
                 teoria=[dict(col='rotacoes', f='1', rotulo='constante', tolerancia=0.05)],
                 leitura=r'Cerca de 0,7 rotação por inserção, de mil a dois milhões de chaves: custo constante.'),
        ],
        conclusao=r'''Com chaves em ordem, a AVL tem altura \textbf{exatamente} $\lg n$, contra $n - 1$ da ABB comum (21 níveis contra dois milhões).
Com chaves aleatórias, fica abaixo de $1{,}44\lg n$, e o reequilíbrio custa só $\approx 0{,}7$ rotação por inserção.'''),
    conexoes=[
        ('\\faDatabase', 'Bancos em memória', 'Bancos e caches em memória que priorizam leituras usam árvores AVL ou parecidas: a altura menor que a da rubro-negra acelera buscas.'),
        ('\\faClock', 'Tempo real', 'Garantia de $O(\\lg n)$ no pior caso, sem amortização: adequada a sistemas que não podem ter picos de latência.'),
        ('\\faCode', 'Linguagens funcionais', 'Conjuntos e mapas imutáveis (\\texttt{Data.Map} em Haskell, \\texttt{Set} em OCaml) usam árvores balanceadas por tamanho ou altura, parentes da AVL.'),
        ('\\faRoute', 'Roteamento', 'Tabelas de prefixos e estruturas de intervalos em roteadores usam árvores balanceadas para manter a busca curta mesmo sob atualizações constantes.'),
    ],
    exercicios=['Insira 1, 2, \\dots, 15 numa AVL vazia e desenhe a árvore após cada rotação.',
                '(13-3a) Prove que uma AVL com $n$ nós tem altura $O(\\lg n)$ ($N_h \\ge F_h$).',
                '(13-3b) Escreva \\Nome{Balance}($x$) para $|h(x.\\mathit{esq}) - h(x.\\mathit{dir})| \\le 2$.',
                '(13-3d) Mostre que a inserção faz $O(1)$ rotações.',
                'Implemente a remoção numa AVL. Ainda basta uma rotação? Meça.'],
    leitura='Cormen et al., problema 13-3 e seção 13.2; slides antigos de AVL.',
)

AULA_25 = dict(
    n=25, bloco=3, tema='Árvores rubro-negras', curto='Árvores rubro-negras',
    cormen='seções 13.1 a 13.3',
    objetivos=['Enunciar as cinco propriedades rubro-negras',
               'Provar que a altura é no máximo $2\\lg(n+1)$',
               'Executar \\Nome{RB-Insert-Fixup} nos três casos',
               'Medir altura e rotações e conferir as propriedades a cada experimento'],
    roteiro=['Propriedades, altura negra, lema 13.1, inserção e conserto',
             'Rubro-negra em C, como no livro, com sentinela',
             'Altura em ordem e aleatória; rotações por inserção',
             'Linux, bibliotecas padrão, memória virtual e redes'],
    teoria=[
        dict(titulo='As cinco propriedades', fig='13.1', altura=0.48,
             legenda='(a) árvore rubro-negra com folhas \\textsc{nil}; (b) com uma sentinela $T.\\mathit{nil}$; (c) sem desenhar as folhas.',
             texto=r'''\begin{enumerate}\setlength{\itemsep}{3pt}
\item Todo nó é vermelho ou preto.
\item A raiz é preta.
\item Toda folha (\textsc{nil}) é preta.
\item Um nó vermelho tem os dois filhos pretos.
\item Todo caminho de um nó até as folhas abaixo dele tem o mesmo número de nós pretos: a \textbf{altura negra} $bh(x)$.
\end{enumerate}''', largura_texto=0.42),
        dict(titulo='Lema 13.1: altura $\\le 2\\lg(n+1)$',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item A subárvore de $x$ tem pelo menos $2^{bh(x)} - 1$ nós internos (indução na altura).
\item Pela propriedade 4, pelo menos metade dos nós de qualquer caminho da raiz a uma folha é preta: $bh(\mathit{raiz}) \ge h/2$.
\item Logo $n \ge 2^{h/2} - 1$, ou seja, $h \le 2\lg(n + 1)$.
\end{itemize}
\medskip O caminho mais longo tem no máximo o \textbf{dobro} do mais curto: um balanceamento mais frouxo que o da AVL, mas mais barato de manter.''',
             rodape=r'Busca, mínimo, máximo, sucessor e predecessor: $O(\lg n)$ sem mudança alguma, porque uma rubro-negra é uma ABB.'),
        dict(titulo='Inserção: o conserto', fig='13.4', altura=0.48,
             legenda='\\Nome{RB-Insert-Fixup} após inserir 4: caso 1 (recolorir), caso 2 (girar o pai) e caso 3 (recolorir e girar o avô).',
             texto=r'''Insere-se $z$ \textbf{vermelho}, como numa ABB. Só a propriedade 4 (ou a 2) pode quebrar. Enquanto o pai de $z$ for vermelho:
\begin{enumerate}\setlength{\itemsep}{3pt}
\item \textbf{Tio vermelho:} pinta pai e tio de preto, avô de vermelho, sobe $z$ dois níveis.
\item \textbf{Tio preto, $z$ filho ``de dentro'':} rotação no pai: vira o caso 3.
\item \textbf{Tio preto, $z$ filho ``de fora'':} recolore e gira o avô. Fim.
\end{enumerate}
No máximo \textbf{2 rotações} por inserção.''', largura_texto=0.48),
    ],
    pratica=dict(
        resumo=['Sentinela \\texttt{nil} preta: folhas e pai da raiz', 'Rotações e \\Nome{RB-Insert-Fixup} linha a linha do livro',
                'Teste com as chaves da Figura 13.4'],
        arquivos=[('aula25_rubro_negra.c', 'Árvore rubro-negra em C')]),
    experimento=dict(
        programa='aula25_experimento.c', titulo='Altura garantida e conserto barato',
        pergunta='A altura de uma rubro-negra respeita 2 lg(n+1)? Quantas rotações custa uma inserção?',
        resumo=['Propriedades conferidas em toda árvore (aborta se falhar)', 'Chaves em ordem e aleatórias, $n$ até $2^{21}$',
                'Rotações por inserção'],
        hipotese=r'''Pelo lema 13.1, a altura fica abaixo de $2\lg(n+1)$ em \textbf{qualquer} ordem de inserção.
Cada inserção faz no máximo 2 rotações; em média, bem menos, e o número deve ser \textbf{constante}, independente de $n$.''',
        metodo=['$n = 2^{10}, \\dots, 2^{21}$', 'Conferência: altura negra igual em todos os caminhos e nenhum vermelho com filho vermelho',
                'Chaves em ordem crescente e chaves aleatórias', 'Contador de rotações'],
        graficos=[
            dict(titulo='Altura da rubro-negra', ylabel='altura', escala='logx',
                 series=[dict(col='altura_ordenada', rotulo='chaves em ordem'), dict(col='altura_aleatoria', rotulo='chaves aleatórias')],
                 teoria=[dict(col='altura_ordenada', f='2*log2(n+1)', rotulo='$2\\lg(n+1)$', limite='superior'),
                         dict(col='altura_aleatoria', f='2*log2(n+1)', rotulo='$2\\lg(n+1)$', limite='superior')],
                 leitura=r'Em ordem, a altura fica perto do limite ($2\lg n - 3$); com chaves aleatórias, perto de $\lg n + 4$.'),
            dict(titulo='Rotações por inserção', ylabel='rotações por inserção', escala='logx', opcoes='ymin=0,ymax=1',
                 series=[dict(col='rotacoes', rotulo='chaves aleatórias')],
                 teoria=[dict(col='rotacoes', f='1', rotulo='constante', tolerancia=0.05)],
                 leitura=r'Cerca de 0,58 rotação por inserção, menos que a AVL (0,7).'),
        ],
        conclusao=r'''As propriedades valeram em todas as árvores, e a altura ficou sempre abaixo de $2\lg(n + 1)$, mesmo com chaves em ordem.
O conserto custa $\approx 0{,}58$ rotação por inserção: menos que a AVL, ao preço de árvores um pouco mais altas. É o equilíbrio que levou as bibliotecas padrão a escolher a rubro-negra.'''),
    conexoes=[
        ('\\faLinux', 'Kernel Linux', 'O escalonador CFS ordenava processos numa rubro-negra pelo tempo de CPU usado; a memória virtual guarda as áreas mapeadas de cada processo numa delas.'),
        ('\\faCode', 'Bibliotecas padrão', '\\texttt{std::map} e \\texttt{std::set} do C++ e \\texttt{TreeMap} do Java são rubro-negras; o \\texttt{HashMap} do Java vira rubro-negra quando uma lista fica longa.'),
        ('\\faNetworkWired', 'Redes', 'Temporizadores de alta resolução e tabelas de conexões usam rubro-negras para inserções e remoções frequentes com pior caso garantido.'),
        ('\\faCodeBranch', 'Estruturas persistentes', 'Rubro-negras funcionais (Okasaki) são a base de mapas imutáveis em Scala e Clojure: versões antigas continuam válidas a custo $O(\\lg n)$.'),
    ],
    exercicios=['(13.1-1) Desenhe a ABB completa de altura 3 com as chaves $1..15$ e pinte-a com alturas negras 2, 3 e 4.',
                '(13.1-5) Mostre que o caminho mais longo de $x$ a uma folha tem no máximo o dobro do mais curto.',
                '(13.3-2) Mostre as árvores após inserir 41, 38, 31, 12, 19, 8 numa rubro-negra vazia.',
                '(13.3-5) Mostre que, com $n > 1$ inserções, a árvore tem pelo menos um nó vermelho.',
                'Compare no experimento a altura média da AVL (aula 24) e da rubro-negra com as mesmas chaves.'],
    leitura='Cormen et al., seções 13.1 a 13.3.',
)

AULA_26 = dict(
    n=26, bloco=3, tema='Árvores B e memória secundária', curto='Árvores B',
    cormen='capítulo 18 (seções 18.1 e 18.2)',
    objetivos=['Explicar por que o acesso ao disco muda o modelo de custo',
               'Definir árvore B de grau mínimo $t$ e limitar sua altura',
               'Inserir com divisão preventiva de nós cheios',
               'Medir a altura para $t = 2$, 16 e 128 e conferir $\\log_t\\frac{n+1}2$'],
    roteiro=['Discos e páginas, definição, altura, busca, divisão e inserção',
             'Árvore B em C com divisão preventiva',
             'Altura para três graus mínimos, até 4 milhões de chaves',
             'Bancos de dados, sistemas de arquivos, armazenamento e SSDs'],
    teoria=[
        dict(titulo='Quando o dado está no disco',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Ler uma página do disco (ou de um SSD) custa milhares de vezes mais que acessar a RAM.
\item O custo que importa passa a ser o \textbf{número de páginas lidas}, não o de comparações.
\item Ideia: nós \textbf{gordos}, do tamanho de uma página, com centenas de chaves. A árvore fica baixíssima.
\item Uma página de 4 KB com chaves de 8 bytes guarda cerca de 500 chaves por nó.
\end{itemize}''',
             fig='18.3', altura=0.26, empilhar=True,
             legenda='árvore B de altura 2 com 1000 chaves por nó: mais de um bilhão de chaves com 3 acessos ao disco.'),
        dict(titulo='Definição', fig='18.1', altura=0.45,
             legenda='árvore B com as consoantes do alfabeto: um nó com $n$ chaves tem $n + 1$ filhos.',
             texto=r'''Árvore B de \textbf{grau mínimo} $t \ge 2$:
\begin{itemize}\setlength{\itemsep}{3pt}
\item Cada nó tem de $t - 1$ a $2t - 1$ chaves (a raiz pode ter menos), em ordem.
\item Um nó interno com $n$ chaves tem $n + 1$ filhos; as chaves separam as faixas dos filhos.
\item Todas as folhas estão na \textbf{mesma profundidade}.
\end{itemize}
\textbf{Teorema 18.1:} $h \le \log_t\dfrac{n + 1}{2}$.''', largura_texto=0.46),
        dict(titulo='Inserção com divisão preventiva', fig='18.5', altura=0.27, empilhar=True,
             legenda='divisão de um nó cheio com $t = 4$: a chave do meio, S, sobe para o pai.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{3pt}
\item A chave nova sempre entra numa \textbf{folha}.
\item Na descida, todo nó \textbf{cheio} ($2t - 1$ chaves) é dividido \textbf{antes} de entrar nele: a chave do meio sobe. Assim nunca é preciso voltar.
\item Se a raiz está cheia, ela é dividida e a árvore \textbf{cresce para cima} (Figura 18.6): única forma de aumentar a altura.
\item $O(h)$ acessos ao disco e $O(t\,h) = O(t\log_t n)$ de CPU.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Nó com vetores de até $2t-1$ chaves e $2t$ filhos', '\\Nome{B-Tree-Split-Child} e \\Nome{B-Tree-Insert-Nonfull}',
                'Teste: as letras do exercício 18.2-1 com $t = 2$'],
        arquivos=[('aula26_arvore_b.c', 'Árvore B em C')]),
    experimento=dict(
        programa='aula26_experimento.c', titulo='Quanto o grau achata a árvore',
        pergunta='Qual a altura de uma árvore B com t = 2, 16 e 128 para até 4 milhões de chaves?',
        resumo=['Teorema 18.1: $h \\le \\log_t\\frac{n+1}{2}$', '$t = 2$ (árvore 2-3-4), 16 e 128',
                '$n$ de $2^{10}$ a $2^{22}$ chaves aleatórias'],
        hipotese=r'''A altura nunca passa de $\log_t\frac{n+1}{2}$. Com $t = 128$, cada nó tem de 127 a 255 chaves: quatro milhões de chaves devem caber em \textbf{3 níveis} (2 acessos abaixo da raiz).
Com $t = 2$, a árvore B é uma árvore 2-3-4 (equivalente a uma rubro-negra): altura perto de $\lg n$.''',
        metodo=['Inserção com divisão preventiva (como no livro)', '$t \\in \\{2, 16, 128\\}$; mesmas chaves para os três',
                '$n = 2^{10}, \\dots, 2^{22}$', 'Altura medida descendo pelo primeiro filho'],
        graficos=[
            dict(titulo='Altura para três graus mínimos', ylabel='altura', escala='logx',
                 series=[dict(col='t2', rotulo='$t = 2$'), dict(col='t16', rotulo='$t = 16$'), dict(col='t128', rotulo='$t = 128$')],
                 teoria=[dict(col='t2', f='log((n+1)/2)/log(2)', rotulo='$\\log_2\\frac{n+1}{2}$', limite='superior'),
                         dict(col='t16', f='log((n+1)/2)/log(16)', rotulo='$\\log_{16}\\frac{n+1}{2}$', limite='superior'),
                         dict(col='t128', f='log((n+1)/2)/log(128)', rotulo='$\\log_{128}\\frac{n+1}{2}$', limite='superior')],
                 leitura=r'Quatro milhões de chaves: altura 17 com $t = 2$, 4 com $t = 16$ e só 2 com $t = 128$.'),
        ],
        conclusao=r'''A altura respeitou o teorema 18.1 em todos os casos. Com $t = 128$, quatro milhões de chaves ficam em \textbf{3 níveis}: uma busca lê 3 páginas do disco, contra 22 de uma árvore binária balanceada.
É por isso que \textbf{todo} banco de dados relacional indexa com árvores B (na verdade, B+).'''),
    conexoes=[
        ('\\faDatabase', 'Bancos de dados', 'PostgreSQL, MySQL (InnoDB), SQLite e Oracle indexam tabelas com árvores B+: as chaves nas folhas, ligadas em lista para consultas por intervalo.'),
        ('\\faHdd', 'Sistemas de arquivos', 'NTFS, HFS+, APFS, Btrfs e XFS guardam diretórios e metadados em árvores B: abrir um arquivo entre milhões custa poucas leituras.'),
        ('\\faServer', 'Armazenamento chave-valor', 'LMDB e BoltDB são árvores B mapeadas em memória; MongoDB (WiredTiger) e CouchDB também usam árvores B.'),
        ('\\faMemory', 'SSDs e cache', 'Em SSDs, escrever custa mais que ler: variantes como B$^\\varepsilon$-trees e LSM-trees (aula 4) trocam leituras por menos escritas.'),
    ],
    exercicios=['(18.1-1) Por que não permitir $t = 1$?',
                '(18.1-4) Qual o número máximo de chaves numa árvore B de altura $h$, em função de $t$?',
                '(18.2-1) Mostre as árvores após inserir F, S, Q, K, C, L, H, T, V, W, M, R, N, P, A, B, X, Y, D, Z, E com $t = 2$.',
                '(18.2-6) Com busca binária dentro de cada nó, mostre que o custo de CPU é $O(\\lg n)$, independente de $t$.',
                'Conte no experimento os nós visitados por busca e simule 10 ms por nó lido do disco. Qual $t$ é melhor?'],
    leitura='Cormen et al., seções 18.1 e 18.2 (remoção: 18.3).',
)

PROJETO_3 = dict(
    n=27, bloco=3, tipo='projeto', tema='Projeto 3: mecanismo de busca em miniatura',
    descricao='Apresentação dos projetos do Bloco 3. Cada equipe indexa um conjunto de textos em português com as estruturas do bloco e compara as estruturas experimentalmente.',
    entregas=['Índice invertido em C: palavra → lista de documentos e posições, sobre livros de domínio público (Machado de Assis, por exemplo)',
              'O mesmo índice com quatro dicionários: hash com encadeamento, hash com endereçamento aberto, ABB e uma árvore balanceada (AVL ou rubro-negra)',
              'Experimento: tempo e número de comparações por busca, altura das árvores e tamanho das listas, para 10 mil a 10 milhões de palavras; confronto com a teoria',
              'Consultas por prefixo e por intervalo alfabético: quais estruturas permitem e a que custo',
              'Apresentação de 10 minutos com demonstração de buscas ao vivo'],
)

AULAS_B3 = [AULA_19, AULA_20, AULA_21, AULA_22, AULA_23, AULA_24, AULA_25, AULA_26, PROJETO_3]
