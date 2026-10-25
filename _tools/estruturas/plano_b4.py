"""Bloco 4 – Grafos (aulas 28 a 36)."""

AULA_28 = dict(
    n=28, bloco=4, tema='Grafos e busca em largura', curto='Busca em largura',
    cormen='seções 22.1 e 22.2',
    objetivos=['Representar grafos por listas de adjacência e por matriz de adjacência',
               'Executar a busca em largura e obter distâncias e a árvore de caminhos mínimos',
               'Provar que a BFS custa $O(V + E)$',
               'Medir o custo linear e o ``mundo pequeno'' de grafos aleatórios'],
    roteiro=['Representações, BFS, distâncias, árvore de busca em largura',
             'BFS em C com o grafo da Figura 22.3',
             'Operações $= V + 2E$; distância média em grafos aleatórios',
             'Redes sociais, web, roteamento e jogos'],
    teoria=[
        dict(titulo='Duas representações', fig='22.1', altura=0.38, empilhar=True,
             legenda='(a) grafo não direcionado; (b) listas de adjacência; (c) matriz de adjacência.',
             texto=r'''\textbf{Listas:} memória $\Theta(V + E)$; ótimas para grafos \textbf{esparsos} ($E \ll V^2$), como quase todos os reais.\quad
\textbf{Matriz:} memória $\Theta(V^2)$; responde ``existe a aresta $(u, v)$?'' em $O(1)$; boa para grafos \textbf{densos}.'''),
        dict(titulo='Busca em largura', nome='BFS($G, s$)',
             pseudo=r'''\For{cada $u \in G.V - \{s\}$}
\State $u.\mathit{cor} \atrib$ \textsc{branco};\; $u.d \atrib \infty$;\; $u.\pi \atrib \textsc{nil}$
\EndFor
\State $s.\mathit{cor} \atrib$ \textsc{cinza};\; $s.d \atrib 0$;\; $Q \atrib \{s\}$
\While{$Q \ne \emptyset$}
\State $u \atrib$ \Nome{Dequeue}($Q$)
\For{cada $v \in G.\mathit{Adj}[u]$}
\If{$v.\mathit{cor} = \textsc{branco}$}
\State $v.\mathit{cor} \atrib$ \textsc{cinza};\; $v.d \atrib u.d + 1$;\; $v.\pi \atrib u$
\State \Nome{Enqueue}($Q, v$)
\EndIf
\EndFor
\State $u.\mathit{cor} \atrib$ \textsc{preto}
\EndWhile''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Explora em \textbf{camadas}: todos à distância $k$ antes de qualquer um à distância $k + 1$.
\item Fila FIFO (aula 12).
\item Cada vértice entra na fila uma vez; cada lista é percorrida uma vez: $O(V + E)$.
\item \textbf{Teorema 22.5:} $v.d = \delta(s, v)$, a distância mínima em arestas.
\end{itemize}''', largura_texto=0.34),
        dict(titulo='BFS passo a passo', fig='22.3', altura=0.62,
             legenda='BFS a partir de $s$: cinza = na fila, preto = terminado; $Q$ mostra a fila e as distâncias.'),
    ],
    pratica=dict(
        resumo=['Listas de adjacência com inserção na cabeça', 'Fila em vetor: cada vértice entra uma vez',
                'Teste com o grafo da Figura 22.3 (vértices r a y)'],
        arquivos=[('aula28_bfs.c', 'Busca em largura em C')]),
    experimento=dict(
        programa='aula28_experimento.c', titulo='Linear em $V + E$, e o mundo é pequeno',
        pergunta='A BFS faz exatamente V + 2E operações? Qual a distância média num grafo aleatório com grau médio 10?',
        resumo=['Operações contadas: vértices que saem da fila + entradas de adjacência', 'Grafos com até 2 milhões de vértices',
                'Distância média com grau médio 10'],
        hipotese=r'''Num grafo não direcionado conexo, a BFS retira cada vértice da fila uma vez e examina cada entrada de adjacência uma vez: exatamente $V + 2E$ operações. Com $E = 4V$: $9V$.
Num grafo aleatório com grau médio $d$, as camadas crescem como $d^k$: a distância típica é $\approx \ln V / \ln d$, que cresce \textbf{muito devagar}.''',
        metodo=['Listas compactas (CSR) para economizar memória', '$V = 2^{12}$ a $2^{21}$, $E = 4V$, com um caminho que garante conexidade',
                'Distância: grafo aleatório com $E = 5V$ (grau médio 10)', 'Contagem exata das operações'],
        graficos=[
            dict(titulo='Operações da BFS', ylabel='operações', escala='log',
                 series=[dict(col='operacoes', rotulo='medido')],
                 teoria=[dict(col='operacoes', f='9*n', rotulo='$V + 2E = 9V$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Exatamente $9V$ em todos os tamanhos: o custo é linear no tamanho do grafo.'),
            dict(titulo='Distância média: seis graus de separação', tabela=1, ylabel='distância média', escala='logx',
                 series=[dict(col='distancia_media', rotulo='grau médio 10')],
                 teoria=[dict(col='distancia_media', f='log(n)', rotulo='$\\ln V$', tolerancia=0.06)],
                 leitura=r'Dois milhões de vértices a uma distância média de 6,4. A constante ajustada fica perto de $1/\ln 10 = 0{,}43$.'),
        ],
        conclusao=r'''A BFS faz exatamente $V + 2E$ operações: \textbf{linear}. E grafos aleatórios são ``pequenos'': com dois milhões de vértices e grau médio 10, a distância média é 6,4, crescendo como $\ln V$.
É o fenômeno dos \textbf{seis graus de separação}, medido por BFS em redes sociais reais.'''),
    conexoes=[
        ('\\faUsers', 'Redes sociais', 'O Facebook mediu, com BFS em 721 milhões de usuários, uma distância média de 4,74; ``pessoas que você talvez conheça'' são vértices à distância 2.'),
        ('\\faSpider', 'Web e buscadores', 'Rastreadores (\\emph{crawlers}) percorrem a web em largura a partir de páginas-semente: a BFS encontra primeiro as páginas mais próximas e relevantes.'),
        ('\\faNetworkWired', 'Redes de computadores', '\\emph{Broadcast} e descoberta de vizinhos inundam a rede camada por camada; o \\texttt{traceroute} revela as camadas da BFS da internet.'),
        ('\\faGamepad', 'Jogos e robótica', 'Em mapas em grade sem pesos, a BFS dá o menor caminho de um personagem ou robô; o cubo de Rubik foi resolvido (``número de Deus'' = 20) com buscas em largura.'),
    ],
    exercicios=['(22.1-1) Com listas de adjacência, quanto custa calcular o grau de saída e o de entrada de todos os vértices?',
                '(22.1-5) Calcule o quadrado de um grafo ($u \\to w$ se há caminho de 2 arestas) com listas e com matriz.',
                '(22.2-1) Execute a BFS na Figura 22.2(a) a partir do vértice 3.',
                '(22.2-7) Divida lutadores em ``bons'' e ``maus'' com rivalidades entre grupos: é testar se o grafo é bipartido. Faça em $O(V + E)$.',
                'Baixe uma rede real (SNAP, Stanford) e meça a distância média com o seu código.'],
    leitura='Cormen et al., seções 22.1 e 22.2.',
)

AULA_29 = dict(
    n=29, bloco=4, tema='Busca em profundidade e ordenação topológica', curto='Busca em profundidade',
    cormen='seções 22.3 e 22.4',
    objetivos=['Executar a DFS e registrar tempos de descoberta e de término',
               'Classificar arestas (árvore, retorno, avanço, cruzamento)',
               'Ordenar topologicamente um grafo acíclico pela ordem de término',
               'Medir $V + E$ operações e o efeito do cache no tempo'],
    roteiro=['DFS, estrutura de parênteses, tipos de arestas, ordenação topológica',
             'O exemplo de se vestir (Figura 22.7) em C',
             'DFS iterativa em DAGs de até 2 milhões de vértices',
             'Compiladores, builds, planilhas e verificação de deadlocks'],
    teoria=[
        dict(titulo='Busca em profundidade', fig='22.4', altura=0.48,
             legenda='DFS num grafo direcionado: $d/f$ = tempos de descoberta e término; B, F, C marcam arestas de retorno, avanço e cruzamento.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Vai fundo: explora o vizinho mais recente antes de voltar (pilha, ou recursão).
\item \Nome{DFS-Visit}($u$): marca $u$ cinza, $u.d \atrib$ tempo; visita os vizinhos brancos; marca preto, $u.f \atrib$ tempo.
\item Recomeça de todo vértice ainda branco: produz uma \textbf{floresta}.
\item Custo $\Theta(V + E)$.
\end{itemize}''', largura_texto=0.38),
        dict(titulo='Parênteses e tipos de arestas', fig='22.5', altura=0.5,
             legenda='(a) tempos da DFS; (b) os intervalos $[d, f]$ formam uma estrutura de parênteses; (c) arestas classificadas.',
             texto=r'''\textbf{Teorema 22.7 (parênteses):} para $u$ e $v$, os intervalos $[u.d, u.f]$ e $[v.d, v.f]$ são disjuntos ou um contém o outro.

\medskip Tipos de aresta $(u, v)$:
\begin{itemize}\setlength{\itemsep}{2pt}
\item \textbf{árvore}: $v$ descoberto por $u$;
\item \textbf{retorno}: $v$ é ancestral (cinza);
\item \textbf{avanço} e \textbf{cruzamento}: as demais.
\end{itemize}
\textbf{Lema 22.11:} o grafo é acíclico $\iff$ a DFS não encontra aresta de retorno.''', largura_texto=0.42),
        dict(titulo='Ordenação topológica', fig='22.7', altura=0.6,
             legenda='(a) o que vestir antes de quê, com tempos $d/f$; (b) os vértices em ordem decrescente de término.',
             texto=r'''Num grafo direcionado acíclico (DAG), uma ordem linear em que toda aresta $(u, v)$ tem $u$ antes de $v$.

\medskip\Nome{Topological-Sort}($G$): rode a DFS; ao terminar cada vértice, insira-o na \textbf{frente} de uma lista.

\medskip\textbf{Teorema 22.12:} num DAG, toda aresta $(u, v)$ tem $v.f < u.f$. Custo $\Theta(V + E)$.''', largura_texto=0.40),
    ],
    pratica=dict(
        resumo=['DFS recursiva com cores e tempos', 'Numeração escolhida para reproduzir a Figura 22.7',
                'Imprime a ordem e os tempos $d/f$'],
        arquivos=[('aula29_dfs_topologica.c', 'DFS e ordenação topológica em C')]),
    experimento=dict(
        programa='aula29_experimento.c', titulo='DFS em DAGs grandes',
        pergunta='A DFS faz exatamente V + E operações num DAG? O tempo também cresce linearmente?',
        resumo=['DAG aleatório com $E = 8V$, ordem escondida por uma permutação', 'DFS iterativa (a recursiva estouraria a pilha)',
                'Verificação: toda aresta respeita a ordem produzida'],
        hipotese=r'''A DFS descobre cada vértice uma vez e examina cada aresta uma vez: com $E = 8V$, exatamente $9V$ operações.
No modelo RAM, o tempo também seria linear. Mas a DFS salta pela memória (como a lista ligada da aula 14): esperamos o tempo crescer \textbf{mais} que linearmente quando o grafo sair do cache.''',
        metodo=['$V = 2^{14}$ a $2^{21}$; arestas sempre de rótulo menor para maior (acíclico)', 'Pilha explícita com a posição na lista de cada vértice',
                'Conferência da ordem topológica em todas as arestas', 'Tempo com \\texttt{CLOCK\\_MONOTONIC}'],
        graficos=[
            dict(titulo='Operações: exatamente $V + E$', ylabel='operações', escala='log',
                 series=[dict(col='operacoes', rotulo='medido')],
                 teoria=[dict(col='operacoes', f='9*n', rotulo='$V + E = 9V$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Contagem exata, e a ordem produzida respeitou todas as 16 milhões de arestas do maior grafo.'),
            dict(titulo='Tempo: o cache aparece', ylabel='tempo (ms)', escala='log',
                 series=[dict(col='tempo_ms', rotulo='medido')],
                 leitura=r'Até $\approx 10^5$ vértices o tempo é linear; depois cresce mais rápido: cada vértice novo está longe na memória.'),
        ],
        conclusao=r'''A contagem é \textbf{exatamente} $V + E$ e a ordem topológica é sempre válida. O tempo, porém, só é linear enquanto o grafo cabe no cache: depois, cada acesso aleatório custa uma ida à RAM.
Bibliotecas de grafos de alto desempenho renumeram os vértices para que vizinhos fiquem próximos na memória.'''),
    conexoes=[
        ('\\faCogs', 'Compiladores e builds', '\\texttt{make}, Maven, Bazel e gerenciadores de pacotes (npm, apt) ordenam topologicamente as dependências; um ciclo é um erro de configuração.'),
        ('\\faTable', 'Planilhas', 'Ao mudar uma célula, a planilha recalcula as dependentes em ordem topológica e detecta referências circulares com a DFS.'),
        ('\\faLock', 'Sistemas operacionais', 'Detectar \\emph{deadlock} é achar um ciclo no grafo de espera entre processos e recursos: uma aresta de retorno na DFS.'),
        ('\\faProjectDiagram', 'Gestão de projetos e dados', 'Diagramas PERT/CPM, pipelines de dados (Airflow) e redes neurais (o grafo de computação do PyTorch) são DAGs executados em ordem topológica.'),
    ],
    exercicios=['(22.3-2) Mostre a DFS do grafo da Figura 22.6 com tempos e tipos de arestas.',
                '(22.3-7) Reescreva a DFS com uma pilha explícita, sem recursão.',
                '(22.4-1) Mostre a ordenação topológica do DAG da Figura 22.8.',
                '(22.4-3) Decida se um grafo não direcionado tem ciclo em $O(V)$, independente de $E$.',
                'Renumere os vértices do experimento em ordem de BFS antes da DFS e meça de novo o tempo.'],
    leitura='Cormen et al., seções 22.3 e 22.4.',
)

AULA_30 = dict(
    n=30, bloco=4, tema='Conjuntos disjuntos e árvores geradoras mínimas', curto='Árvores geradoras mínimas',
    cormen='capítulo 21 e capítulo 23',
    objetivos=['Implementar conjuntos disjuntos com união por posto e compressão de caminho',
               'Enunciar a propriedade de corte que justifica os algoritmos gulosos de AGM',
               'Executar Kruskal e Prim',
               'Medir o custo quase constante das operações de conjuntos disjuntos'],
    roteiro=['Floresta de conjuntos disjuntos; corte e aresta leve; Kruskal e Prim',
             'Kruskal com conjuntos disjuntos no grafo da Figura 23.1',
             'Ingênuo contra heurísticas: $\\Theta(n)$ contra constante',
             'Redes elétricas, telecomunicações, agrupamento e visão computacional'],
    teoria=[
        dict(titulo='Conjuntos disjuntos', fig='21.4', altura=0.55,
             legenda='floresta de conjuntos disjuntos: (a) dois conjuntos; (b) depois de \\Nome{Union}.',
             texto=r'''Operações: \Nome{Make-Set}($x$), \Nome{Find-Set}($x$) (o representante) e \Nome{Union}($x, y$).
\begin{itemize}\setlength{\itemsep}{4pt}
\item Cada conjunto é uma árvore; a raiz é o representante.
\item \textbf{União por posto:} a árvore mais baixa vira filha da mais alta.
\item \textbf{Compressão de caminho:} na busca, todos os nós do caminho passam a apontar para a raiz.
\item Com as duas: $O(m\,\alpha(n))$ para $m$ operações, com $\alpha(n) \le 4$ para qualquer $n$ do universo.
\end{itemize}''', largura_texto=0.48),
        dict(titulo='Compressão de caminho', fig='21.5', altura=0.6,
             legenda='\\Nome{Find-Set}($a$) antes (a) e depois (b): todo o caminho aponta para a raiz.'),
        dict(titulo='Árvore geradora mínima', fig='23.1', altura=0.5,
             legenda='uma AGM de peso 37 (arestas sombreadas). Trocar $(b, c)$ por $(a, h)$ dá outra AGM de mesmo peso.',
             texto=r'''Num grafo conexo com pesos, escolher $V - 1$ arestas que ligam todos os vértices com \textbf{peso total mínimo}.

\medskip\textbf{Teorema 23.1 (corte):} para qualquer corte que respeite as arestas já escolhidas, a aresta \textbf{leve} (mais barata) que cruza o corte é segura.

\medskip Os dois algoritmos são \textbf{gulosos}: sempre pegam a aresta segura mais barata.''', largura_texto=0.44),
        dict(titulo='Kruskal e Prim', fig='23.4', altura=0.6,
             legenda='Kruskal na Figura 23.1: arestas em ordem de peso; a seta indica a aresta examinada.',
             texto=r'''\textbf{Kruskal:} ordene as arestas; para cada uma, se liga componentes diferentes (\Nome{Find-Set} diferentes), escolha-a e una. $O(E\lg V)$, dominado pela ordenação.

\medskip\textbf{Prim:} cresça uma árvore a partir de uma raiz, sempre pela aresta mais leve que sai dela, com fila de prioridade. $O(E\lg V)$ com heap binário.''', largura_texto=0.40),
    ],
    pratica=dict(
        resumo=['\\texttt{acha} com compressão; \\texttt{une} por posto', 'Arestas da Figura 23.1 ordenadas com \\texttt{qsort}',
                'Imprime as arestas escolhidas e o peso total (37)'],
        arquivos=[('aula30_kruskal.c', 'Kruskal com conjuntos disjuntos')]),
    experimento=dict(
        programa='aula30_experimento.c', titulo='Quase constante por operação',
        pergunta='Quantos ponteiros uma operação de conjuntos disjuntos segue, sem e com as heurísticas?',
        resumo=['Uniões em corrente (0-1, 1-2, …): o pior caso do ingênuo', '4 buscas aleatórias para cada união',
                'Ingênuo até $n = 16.000$; heurísticas até 2 milhões'],
        hipotese=r'''Sem heurísticas, as uniões em corrente formam uma lista; uma busca aleatória sobe em média $u^2/(2n)$ ponteiros depois de $u$ uniões, o que dá $\approx \frac{2n}{15}$ por operação: \textbf{linear}.
Com união por posto e compressão de caminho, o custo por operação é $O(\alpha(n))$: na prática, \textbf{constante}.''',
        metodo=['$m = 5n$ operações: uniões $x$-$(x+1)$ e 4 buscas sorteadas', 'Contador de ponteiros seguidos até a raiz',
                'Ingênuo: $n$ de 1.000 a 16.000', 'Heurísticas: $n$ de $2^{12}$ a $2^{21}$'],
        graficos=[
            dict(titulo='Ingênuo: linear por operação', ylabel='ponteiros por operação',
                 series=[dict(col='ingenuo', rotulo='sem heurísticas'), dict(col='heuristicas', rotulo='posto + compressão')],
                 teoria=[dict(col='ingenuo', f='2*n/15', rotulo='$2n/15$', ajustar=False, tolerancia=0.05)],
                 leitura=r'Com $n = 16.000$: 2.141 ponteiros por operação sem heurísticas; 0,6 com elas.'),
            dict(titulo='Com heurísticas: constante', tabela=1, ylabel='ponteiros por operação', escala='logx', opcoes='ymin=0,ymax=1',
                 series=[dict(col='heuristicas_grande', rotulo='posto + compressão')],
                 teoria=[dict(col='heuristicas_grande', f='1', rotulo='constante', tolerancia=0.05)],
                 leitura=r'0,60 ponteiro por operação de quatro mil a dois milhões de elementos: $\alpha(n)$ na prática.'),
        ],
        conclusao=r'''Sem heurísticas, cada operação custa $\approx 2n/15$: com 16 mil elementos, mais de 2 mil passos. Com união por posto e compressão de caminho, o custo cai para \textbf{0,6} e não muda até dois milhões de elementos.
É o que torna o Kruskal $O(E\lg V)$: o gargalo passa a ser só a ordenação das arestas.'''),
    conexoes=[
        ('\\faBolt', 'Redes de infraestrutura', 'Projetar redes elétricas, de fibra óptica ou de saneamento ligando todos os pontos com o menor custo de cabo é uma AGM (Borůvka, 1926, eletrificação da Morávia).'),
        ('\\faObjectGroup', 'Agrupamento de dados', 'Remover as $k - 1$ arestas mais pesadas da AGM separa os dados em $k$ grupos: o agrupamento por ligação simples (\\emph{single linkage}).'),
        ('\\faImage', 'Visão computacional', 'A segmentação de imagens de Felzenszwalb e Huttenlocher une pixels parecidos com conjuntos disjuntos, no estilo do Kruskal.'),
        ('\\faProjectDiagram', 'Compiladores e redes', 'Conjuntos disjuntos resolvem unificação de tipos (inferência de tipos) e acompanham componentes conexas de redes que mudam em tempo real.'),
    ],
    exercicios=['(21.3-1) Refaça o exercício 21.2-2 com união por posto e compressão de caminho.',
                '(23.1-1) Mostre que uma aresta de peso mínimo pertence a alguma AGM.',
                '(23.2-1) Kruskal pode dar AGMs diferentes conforme a ordem dos empates. Mostre que toda AGM pode ser obtida assim.',
                '(23.2-8) O algoritmo ``divida os vértices ao meio, ache as AGMs e ligue pela aresta mais leve'' funciona? Prove ou dê contraexemplo.',
                'Implemente Prim com heap e confira que dá o mesmo peso que o Kruskal em grafos aleatórios.'],
    leitura='Cormen et al., seções 21.1 a 21.3 e capítulo 23.',
)

AULA_31 = dict(
    n=31, bloco=4, tema='Caminhos mínimos: Bellman-Ford e Dijkstra', curto='Caminhos mínimos',
    cormen='seções 24.1 e 24.3',
    objetivos=['Definir caminhos mínimos com pesos e o papel dos ciclos negativos',
               'Usar o relaxamento como operação básica',
               'Executar Bellman-Ford ($O(VE)$) e Dijkstra ($O((V + E)\\lg V)$ com heap)',
               'Medir vetor contra heap no Dijkstra e o custo do Bellman-Ford'],
    roteiro=['Relaxamento, Bellman-Ford, Dijkstra, a escolha da fila de prioridade',
             'Dijkstra com heap na Figura 24.6',
             'Três implementações em grafos esparsos',
             'GPS, roteamento na internet, logística e jogos'],
    teoria=[
        dict(titulo='Relaxamento',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item $\delta(s, v)$: peso do caminho mínimo de $s$ a $v$; $v.d$ é a estimativa atual, começando em $\infty$.
\item \Nome{Relax}($u, v, w$): \textbf{se} $v.d > u.d + w(u, v)$ \textbf{então} $v.d \atrib u.d + w(u, v)$ e $v.\pi \atrib u$.
\item Todos os algoritmos do capítulo 24 diferem só na \textbf{ordem} e no \textbf{número} de relaxamentos.
\item Subcaminhos de caminhos mínimos são mínimos (lema 24.1): a base da programação dinâmica e da gulosa.
\item Ciclo de peso negativo alcançável: $\delta$ não está definido ($-\infty$).
\end{itemize}'''),
        dict(titulo='Bellman-Ford', nome='Bellman-Ford($G, w, s$)',
             pseudo=r'''\State \Nome{Initialize-Single-Source}($G, s$)
\For{$i \atrib 1$ \textbf{até} $|G.V| - 1$}
\For{cada aresta $(u, v) \in G.E$}
\State \Nome{Relax}($u, v, w$)
\EndFor
\EndFor
\For{cada aresta $(u, v) \in G.E$}
\If{$v.d > u.d + w(u, v)$} \State \Return \textsc{falso} \Comment{ciclo negativo} \EndIf
\EndFor
\State \Return \textsc{verdadeiro}''',
             fig='24.4', legenda='Bellman-Ford com pesos negativos: cada passada relaxa todas as arestas.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Aceita pesos \textbf{negativos}.
\item Após $i$ passadas, acerta todo caminho mínimo com até $i$ arestas.
\item Detecta ciclos negativos.
\item Custo $\Theta(VE)$.
\end{itemize}''', largura_texto=0.32),
        dict(titulo='Dijkstra', nome='Dijkstra($G, w, s$)',
             pseudo=r'''\State \Nome{Initialize-Single-Source}($G, s$)
\State $S \atrib \emptyset$;\quad $Q \atrib G.V$ \Comment{fila de mínimo por $d$}
\While{$Q \ne \emptyset$}
\State $u \atrib$ \Nome{Extract-Min}($Q$)
\State $S \atrib S \cup \{u\}$
\For{cada $v \in G.\mathit{Adj}[u]$}
\State \Nome{Relax}($u, v, w$) \Comment{\Nome{Decrease-Key}}
\EndFor
\EndWhile''',
             fig='24.6', legenda='Dijkstra a partir de $s$: em preto, os vértices já em $S$; sombreadas, as arestas da árvore.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Exige pesos \textbf{não negativos}.
\item Guloso: o vértice de menor $d$ em $Q$ já tem $d = \delta$ (teorema 24.6).
\item Vetor: $O(V^2)$. Heap: $O((V + E)\lg V)$. Heap de Fibonacci: $O(V\lg V + E)$.
\end{itemize}''', largura_texto=0.32),
    ],
    pratica=dict(
        resumo=['Heap de mínimo com \\texttt{pos[]}: \\Nome{Decrease-Key} em $O(\\lg V)$', 'O grafo da Figura 24.6',
                'Imprime $d$ e o caminho até $x$ pelos predecessores $\\pi$'],
        arquivos=[('aula31_dijkstra.c', 'Dijkstra em C')]),
    experimento=dict(
        programa='aula31_experimento.c', titulo='A estrutura de dados decide',
        pergunta='Em grafos esparsos, quantas operações fazem Dijkstra com vetor, Dijkstra com heap e Bellman-Ford?',
        resumo=['Grafo com $E = 8V$ e pesos de 1 a 100', 'Vetor: $V^2 + E$; heap: $\\Theta((V + E)\\lg V)$; Bellman-Ford: $(V-1)E$',
                '$V$ de 250 a 4.000'],
        hipotese=r'''Com vetor, cada \Nome{Extract-Min} varre $V$ posições: $V^2 + E = V^2 + 8V$ operações. Com heap, $\Theta((V + E)\lg V)$.
Bellman-Ford relaxa as $E$ arestas $V - 1$ vezes: exatamente $8V(V-1)$.''',
        metodo=['Mesmo grafo para os três algoritmos', 'Vetor: varreduras + relaxamentos',
                'Heap: comparações do heap + relaxamentos', 'Bellman-Ford sem parada antecipada'],
        graficos=[
            dict(titulo='Operações das três implementações', ylabel='operações', escala='logy',
                 series=[dict(col='bellman_ford', rotulo='Bellman-Ford'), dict(col='vetor', rotulo='Dijkstra com vetor'),
                         dict(col='heap', rotulo='Dijkstra com heap')],
                 teoria=[dict(col='heap', f='n*log2(n)', rotulo='$V\\lg V$', tolerancia=0.05),
                         dict(col='vetor', f='n*n + 8*n', rotulo='$V^2 + E$', ajustar=False, tolerancia=0.0001),
                         dict(col='bellman_ford', f='8*n*(n-1)', rotulo='$(V-1)E$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Para $V = 4.000$: 124 mil operações com heap, 16 milhões com vetor, 128 milhões no Bellman-Ford.'),
        ],
        conclusao=r'''As contagens batem: $V^2 + E$ e $(V-1)E$ exatos, e $\Theta(V\lg V)$ com heap. Em grafos esparsos, o heap é \textbf{130 vezes} mais barato que o vetor para $V = 4.000$.
Em grafos densos ($E \approx V^2$), o vetor volta a ser competitivo: a melhor estrutura depende da \textbf{densidade} do grafo.'''),
    conexoes=[
        ('\\faRoute', 'Navegação (GPS)', 'Google Maps e Waze usam Dijkstra com acelerações (A*, hierarquias de contração) em grafos de bilhões de arestas, com pesos que mudam com o trânsito.'),
        ('\\faNetworkWired', 'Roteamento na internet', 'OSPF e IS-IS rodam Dijkstra em cada roteador; RIP e BGP são variações distribuídas do Bellman-Ford (vetor de distâncias).'),
        ('\\faExchangeAlt', 'Finanças', 'Com pesos $-\\log(\\text{câmbio})$, um ciclo negativo é uma oportunidade de arbitragem entre moedas: Bellman-Ford a detecta.'),
        ('\\faTruck', 'Logística', 'Roteirização de entregas e planejamento de rotas de transporte público começam com caminhos mínimos entre todos os pontos de interesse.'),
    ],
    exercicios=['(24.1-1) Execute Bellman-Ford na Figura 24.4 a partir de $z$.',
                '(24.3-1) Execute Dijkstra na Figura 24.2 a partir de $s$ e depois de $z$.',
                '(24.3-2) Dê um grafo com aresta negativa em que Dijkstra erra.',
                '(24.3-4) Verifique em $O(V + E)$ se valores $d$ e $\\pi$ dados são caminhos mínimos.',
                'Repita o experimento com grafos densos ($E = V^2/4$). Onde as curvas do vetor e do heap se cruzam?'],
    leitura='Cormen et al., seções 24.1 a 24.3.',
)

AULA_32 = dict(
    n=32, bloco=4, tema='Caminhos mínimos entre todos os pares: Floyd-Warshall', curto='Floyd-Warshall',
    cormen='seção 25.2',
    objetivos=['Formular caminhos mínimos entre todos os pares por programação dinâmica',
               'Executar Floyd-Warshall e reconstruir caminhos',
               'Calcular o fecho transitivo',
               'Medir $V^3$ contra $V$ execuções de Dijkstra em grafos esparsos'],
    roteiro=['A recorrência dos intermediários, o algoritmo, o fecho transitivo',
             'Floyd-Warshall no grafo da Figura 25.1',
             'Tempo de Floyd-Warshall contra $V\\times$ Dijkstra',
             'Redes, bioinformática, mapas e análise de dependências'],
    teoria=[
        dict(titulo='A recorrência',
             texto=r'''Numere os vértices $1..n$. Seja $d_{ij}^{(k)}$ o peso do caminho mínimo de $i$ a $j$ cujos vértices \textbf{intermediários} estão todos em $\{1, \dots, k\}$:
\[d_{ij}^{(k)} = \begin{cases} w_{ij} & k = 0\\[2pt] \min\big(d_{ij}^{(k-1)},\; d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\big) & k \ge 1\end{cases}\]
\begin{itemize}\setlength{\itemsep}{4pt}
\item Ou o caminho mínimo não passa por $k$, ou passa \textbf{uma vez}, e as duas metades são mínimas.
\item A resposta é $D^{(n)}$. Pesos negativos são permitidos; ciclos negativos, não.
\end{itemize}'''),
        dict(titulo='O algoritmo', nome='Floyd-Warshall($W$)',
             pseudo=r'''\State $n \atrib W.\mathit{linhas}$;\quad $D \atrib W$
\For{$k \atrib 1$ \textbf{até} $n$}
\For{$i \atrib 1$ \textbf{até} $n$}
\For{$j \atrib 1$ \textbf{até} $n$}
\State $d_{ij} \atrib \min(d_{ij},\; d_{ik} + d_{kj})$
\EndFor
\EndFor
\EndFor
\State \Return $D$''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Três laços, $\Theta(n^3)$, constante pequena.
\item Uma só matriz basta (exercício 25.2-4).
\item Predecessores $\pi_{ij}$ reconstroem os caminhos.
\item \textbf{Fecho transitivo:} troque $\min$ e $+$ por \textsc{ou} e \textsc{e}.
\end{itemize}''', largura_texto=0.44),
        dict(titulo='As matrizes $D^{(k)}$ e $\\Pi^{(k)}$', fig='25.4', altura=0.63,
             legenda='Floyd-Warshall no grafo da Figura 25.1: de $D^{(0)}$ a $D^{(5)}$, com as matrizes de predecessores.'),
    ],
    pratica=dict(
        resumo=['O grafo da Figura 25.1, com pesos negativos', 'Três laços: $k$ por fora', 'Imprime $D^{(5)}$ (Figura 25.4)'],
        arquivos=[('aula32_floyd_warshall.c', 'Floyd-Warshall em C')]),
    experimento=dict(
        programa='aula32_experimento.c', titulo='$V^3$ contra $V\\times$ Dijkstra',
        pergunta='Em grafos esparsos, Floyd-Warshall (V³) ou V execuções de Dijkstra (V²lg V)?',
        resumo=['Grafo com $E = 8V$; as duas respostas são conferidas', 'Floyd-Warshall: $\\Theta(V^3)$',
                '$V\\times$ Dijkstra com heap: $\\Theta(V(V + E)\\lg V) = \\Theta(V^2\\lg V)$'],
        hipotese=r'''Floyd-Warshall custa $\Theta(V^3)$, sem depender de $E$. Rodar Dijkstra de cada vértice custa $\Theta(V(V + E)\lg V)$: em grafos esparsos, $\Theta(V^2\lg V)$.
Apesar da constante menor do Floyd-Warshall, a diferença de ordem deve aparecer já para algumas centenas de vértices.''',
        metodo=['$V$ de 200 a 1.600; $E = 8V$; pesos de 1 a 100', 'Floyd-Warshall com matriz em um vetor contíguo',
                'Dijkstra com heap binário a partir de cada vértice', 'Soma das distâncias conferida entre os dois métodos'],
        graficos=[
            dict(titulo='Tempo para todos os pares', ylabel='tempo (ms)', escala='log',
                 series=[dict(col='floyd_ms', rotulo='Floyd-Warshall'), dict(col='dijkstra_ms', rotulo='$V\\times$ Dijkstra')],
                 teoria=[dict(col='floyd_ms', f='n**3', rotulo='$V^3$', tolerancia=0.25),
                         dict(col='dijkstra_ms', f='n*n*log2(n)', rotulo='$V^2\\lg V$', tolerancia=0.25)],
                 leitura=r'Em log-log, inclinação 3 contra pouco mais de 2. Para $V = 1.600$: 1,5 s contra 0,27 s.'),
        ],
        conclusao=r'''As duas formas de crescimento se confirmam: $V^3$ para Floyd-Warshall e $V^2\lg V$ para $V$ execuções de Dijkstra, com as mesmas respostas.
Em grafos \textbf{esparsos}, Dijkstra repetido vence; em grafos \textbf{densos} ou pequenos, a simplicidade do Floyd-Warshall compensa, e ele aceita pesos negativos.'''),
    conexoes=[
        ('\\faNetworkWired', 'Redes', 'Matrizes de latência entre todos os servidores de um data center ou de uma CDN orientam onde colocar réplicas e como balancear carga.'),
        ('\\faDna', 'Bioinformática', 'Distâncias entre todas as espécies (ou genes) alimentam a construção de árvores filogenéticas por métodos de distância.'),
        ('\\faMapMarked', 'Mapas e logística', 'Tabelas de distância entre todas as cidades (o ``mapa rodoviário'') são pré-calculadas para planejar rotas e entregas.'),
        ('\\faProjectDiagram', 'Análise de dependências', 'O fecho transitivo responde ``A depende de B, direta ou indiretamente?'' em compiladores, bancos de dados (consultas recursivas) e controle de acesso.'),
    ],
    exercicios=['(25.2-1) Execute Floyd-Warshall no grafo da Figura 25.2 e mostre cada $D^{(k)}$.',
                '(25.2-4) Mostre que basta uma única matriz (sem os índices $k$).',
                '(25.2-6) Use a saída de Floyd-Warshall para detectar um ciclo negativo.',
                '(25.2-9) Calcule o fecho transitivo de um grafo direcionado em $O(V^3)$ com bits.',
                'Troque a ordem dos laços para $i, j, k$. O resultado continua correto? Por quê?'],
    leitura='Cormen et al., seção 25.2.',
)

AULA_33 = dict(
    n=33, bloco=4, tema='Programação dinâmica', curto='Programação dinâmica',
    cormen='seções 15.1, 15.3 e 15.4',
    objetivos=['Reconhecer subestrutura ótima e subproblemas sobrepostos',
               'Resolver o corte de hastes de cima para baixo (memoização) e de baixo para cima',
               'Calcular a maior subsequência comum (LCS) e reconstruí-la',
               'Medir $2^n$ chamadas contra $n(n+1)/2$'],
    roteiro=['Corte de hastes, o grafo de subproblemas, LCS',
             'Corte de hastes e LCS em C',
             'Recursão ingênua contra memoização',
             'Bioinformática, \\texttt{diff}, linguagem natural e finanças'],
    teoria=[
        dict(titulo='Corte de hastes', fig='15.1', altura=0.18, empilhar=True,
             legenda='preço $p_i$ de uma haste de comprimento $i$.',
             texto=r'''Cortar uma haste de comprimento $n$ em pedaços para \textbf{maximizar a receita} $r_n$:
\[r_n = \max_{1 \le i \le n}\big(p_i + r_{n-i}\big), \qquad r_0 = 0\]
O primeiro pedaço tem comprimento $i$; o resto, $n - i$, é cortado da melhor forma: \textbf{subestrutura ótima}.
Para $n = 4$: cortar em $2 + 2$ dá $5 + 5 = 10$, melhor que vender inteira (9).'''),
        dict(titulo='Por que a recursão ingênua explode', fig='15.3', altura=0.55,
             legenda='árvore de recursão de \\Nome{Cut-Rod}($p$, 4): os mesmos subproblemas aparecem muitas vezes.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \Nome{Cut-Rod}($p, n$) chama a si mesma para $n-1, n-2, \dots, 0$.
\item $T(n) = 1 + \sum_{j=0}^{n-1} T(j) = 2^n$ chamadas.
\item São só $n + 1$ subproblemas diferentes: \textbf{sobrepostos}.
\item Guardar cada resposta na primeira vez (\textbf{memoização}) ou calcular de baixo para cima: $\Theta(n^2)$.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='O grafo de subproblemas', fig='15.4', altura=0.55,
             legenda='o grafo de subproblemas para $n = 4$: uma aresta $x \\to y$ indica que $x$ depende de $y$.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Os subproblemas e suas dependências formam um \textbf{DAG}.
\item De baixo para cima = resolver em ordem topológica reversa (aula 29).
\item Custo = (número de vértices) $\times$ (trabalho por vértice) = soma dos graus de saída: $\Theta(n^2)$.
\item \textbf{Quatro passos:} caracterizar a solução ótima, recorrência, calcular os valores, reconstruir a solução.
\end{itemize}''', largura_texto=0.48),
        dict(titulo='Maior subsequência comum (LCS)', fig='15.8', altura=0.48,
             legenda='tabela $c$ e setas $b$ para $X = $ ABCBDAB e $Y = $ BDCABA: LCS = BCBA, de tamanho 4.',
             texto=r'''\[c[i, j] = \begin{cases} 0 & i = 0 \text{ ou } j = 0\\ c[i-1, j-1] + 1 & x_i = y_j\\ \max(c[i-1, j],\, c[i, j-1]) & x_i \ne y_j\end{cases}\]
\begin{itemize}\setlength{\itemsep}{3pt}
\item Tabela $(m + 1)\times(n + 1)$: $\Theta(mn)$.
\item Seguindo as setas a partir de $c[m, n]$, reconstrói-se a LCS.
\end{itemize}''', largura_texto=0.46),
    ],
    pratica=dict(
        resumo=['Corte de hastes de baixo para cima com os preços da Figura 15.1', 'LCS com tabela e reconstrução de trás para frente',
                'Testes: a LCS de ABCBDAB e BDCABA é BCBA'],
        arquivos=[('aula33_programacao_dinamica.c', 'Corte de hastes e LCS em C')]),
    experimento=dict(
        programa='aula33_experimento.c', titulo='$2^n$ contra $n(n+1)/2$',
        pergunta='Quantas chamadas faz o corte de hastes recursivo ingênuo e quantas faz a versão memoizada?',
        resumo=['Recursão ingênua: $2^n$ chamadas', 'Memoizada: $n(n+1)/2 + 1$ chamadas',
                'As duas versões têm de dar a mesma receita'],
        hipotese=r'''A recursão ingênua faz $T(n) = 1 + \sum_{j<n} T(j) = 2^n$ chamadas: \textbf{exponencial}.
A versão memoizada resolve cada subproblema uma vez; as chamadas que encontram a resposta pronta somam $n(n+1)/2$, mais a chamada inicial: \textbf{quadrática}.''',
        metodo=['Preços sintéticos para comprimentos 1 a 40', '$n$ de 2 a 26', 'Contador global de chamadas', 'Comparação das receitas'],
        graficos=[
            dict(titulo='Chamadas recursivas', ylabel='chamadas', escala='logy',
                 series=[dict(col='ingenua', rotulo='ingênua'), dict(col='memoizada', rotulo='memoizada')],
                 teoria=[dict(col='ingenua', f='2**n', rotulo='$2^n$', ajustar=False, tolerancia=0.0001),
                         dict(col='memoizada', f='n*(n+1)/2 + 1', rotulo='$\\frac{n(n+1)}{2} + 1$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Para $n = 26$: 67 milhões de chamadas contra 352. Com $n = 50$, a ingênua levaria anos.'),
        ],
        conclusao=r'''As contagens são \textbf{exatamente} $2^n$ e $n(n+1)/2 + 1$. Guardar as respostas dos subproblemas transforma um algoritmo exponencial em quadrático, com o mesmo resultado.
A programação dinâmica troca \textbf{memória por tempo}: uma tabela de $n + 1$ posições economiza bilhões de chamadas.'''),
    conexoes=[
        ('\\faDna', 'Bioinformática', 'Alinhar sequências de DNA e proteínas (Needleman–Wunsch, Smith–Waterman) é uma LCS com pesos: a base do BLAST e da comparação de genomas.'),
        ('\\faCodeBranch', 'Controle de versão', '\\texttt{diff} e \\texttt{git diff} calculam a menor sequência de edições entre dois arquivos, uma variação da LCS.'),
        ('\\faLanguage', 'Linguagem natural', 'Corretores ortográficos (distância de edição), reconhecimento de voz (Viterbi) e análise sintática (CYK) são programação dinâmica.'),
        ('\\faChartLine', 'Finanças e IA', 'Precificação de opções em árvores binomiais e aprendizado por reforço (equação de Bellman) resolvem subproblemas de baixo para cima.'),
    ],
    exercicios=['(15.1-2) Mostre que a estratégia gulosa ``maior densidade $p_i/i$ primeiro'' não é ótima no corte de hastes.',
                '(15.1-3) Cada corte custa $c$. Modifique o algoritmo.',
                '(15.4-1) Ache a LCS de $\\langle 1,0,0,1,0,1,0,1\\rangle$ e $\\langle 0,1,0,1,1,0,1,1,0\\rangle$.',
                '(15.4-5) Ache a maior subsequência crescente de $n$ números em $O(n^2)$.',
                'Implemente a distância de edição entre duas palavras e use-a para sugerir correções ortográficas.'],
    leitura='Cormen et al., seções 15.1, 15.3 e 15.4.',
)

AULA_34 = dict(
    n=34, bloco=4, tema='Algoritmos gulosos: seleção de atividades e Huffman', curto='Algoritmos gulosos',
    cormen='seções 16.1 a 16.3',
    objetivos=['Reconhecer a propriedade da escolha gulosa e a subestrutura ótima',
               'Resolver a seleção de atividades escolhendo sempre a que termina primeiro',
               'Construir códigos de Huffman com fila de prioridade',
               'Medir o comprimento médio de Huffman contra a entropia de Shannon'],
    roteiro=['Seleção de atividades, gulosos contra programação dinâmica, códigos de prefixo',
             'Huffman em C com as frequências da Figura 16.3',
             'Huffman, entropia e código fixo para alfabetos de 2 a 4.096 símbolos',
             'Compressão, redes, agendamento e aprendizado de máquina'],
    teoria=[
        dict(titulo='Seleção de atividades', fig='16.1', altura=0.48,
             legenda='\\Nome{Recursive-Activity-Selector}: em cada passo, a próxima atividade compatível que termina primeiro.',
             texto=r'''Atividades $a_i = [s_i, f_i)$ disputam uma sala. Escolher o maior conjunto sem sobreposição.
\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Escolha gulosa:} a atividade que \textbf{termina primeiro} deixa a sala livre o mais cedo possível.
\item \textbf{Teorema 16.1:} ela pertence a alguma solução ótima.
\item Depois, o problema restante tem a mesma forma.
\item Com as atividades ordenadas por término: $\Theta(n)$.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='Códigos de prefixo', fig='16.4', altura=0.5,
             legenda='(a) código de tamanho fixo, 300 mil bits; (b) código ótimo, 224 mil bits.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Código de prefixo}: nenhuma palavra é prefixo de outra; decodificar é só seguir a árvore.
\item Custo de uma árvore $T$: $B(T) = \sum_c c.\mathit{freq}\cdot d_T(c)$.
\item Símbolos frequentes devem ficar perto da raiz.
\item Um código ótimo corresponde a uma árvore \textbf{cheia} (todo nó interno tem dois filhos).
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Huffman', fig='16.5', altura=0.66,
             legenda='construção do código de Huffman: juntar sempre os dois menos frequentes.',
             texto=r'''\Nome{Huffman}($C$): coloque os símbolos numa fila de mínimo por frequência; $n - 1$ vezes, retire os dois menores $x$ e $y$, crie $z$ com $z.\mathit{freq} = x.\mathit{freq} + y.\mathit{freq}$ e filhos $x$, $y$, e reinsira $z$.

\medskip Custo $O(n\lg n)$ com heap (aula 17).

\medskip\textbf{Lemas 16.2 e 16.3:} a escolha gulosa é segura e o problema restante tem subestrutura ótima.''', largura_texto=0.44),
    ],
    pratica=dict(
        resumo=['Frequências de a a f da Figura 16.3', 'Fila de prioridade simples (vetor) para 6 símbolos',
                'Imprime o código de cada símbolo e o total: 224 mil bits'],
        arquivos=[('aula34_huffman.c', 'Códigos de Huffman em C')]),
    experimento=dict(
        programa='aula34_experimento.c', titulo='Huffman contra o limite de Shannon',
        pergunta='O comprimento médio do código de Huffman fica entre a entropia H e H + 1? Quanto ele ganha do código fixo?',
        resumo=['Alfabetos de 2 a 4.096 símbolos com frequências de Zipf', 'Huffman com heap',
                'Verificação: $H \\le L < H + 1$ em todos os casos'],
        hipotese=r'''Para qualquer código de prefixo, o comprimento médio $L$ é pelo menos a \textbf{entropia} $H = -\sum p_i\lg p_i$ (Shannon). O código de Huffman é ótimo e garante $H \le L < H + 1$.
O código de tamanho fixo usa $\lceil\lg n\rceil$ bits: Huffman nunca pode ser pior.''',
        metodo=['Frequências proporcionais a $1/i$ (lei de Zipf)', '$n = 2, 4, 8, \\dots, 4.096$ símbolos',
                '$L = \\sum p_i \\cdot$ profundidade da folha $i$', 'O programa aborta se $L \\notin [H, H + 1)$'],
        graficos=[
            dict(titulo='Bits por símbolo', ylabel='bits por símbolo', escala='logx',
                 series=[dict(col='fixo', rotulo='código fixo'), dict(col='huffman', rotulo='Huffman'), dict(col='entropia', rotulo='entropia $H$')],
                 teoria=[dict(col='huffman', f='ceil(log2(n))', rotulo='$\\lceil\\lg n\\rceil$', limite='superior')],
                 leitura=r'Huffman fica colado na entropia (diferença de 0,03 a 0,08 bit) e economiza 2 a 3 bits por símbolo em relação ao código fixo.'),
        ],
        conclusao=r'''Em todos os alfabetos, $H \le L < H + 1$, e na prática $L - H < 0{,}1$ bit: Huffman fica praticamente no \textbf{limite teórico} da compressão sem perdas símbolo a símbolo.
Um algoritmo guloso de cinco linhas atinge o ótimo, e a teoria da informação diz que ninguém pode fazer melhor.'''),
    conexoes=[
        ('\\faFileArchive', 'Compressão', 'DEFLATE (ZIP, gzip, PNG), JPEG e MP3 usam códigos de Huffman na etapa final; formatos modernos usam codificação aritmética, que chega ainda mais perto de $H$.'),
        ('\\faNetworkWired', 'Redes', 'O HTTP/2 comprime cabeçalhos com HPACK, que usa uma tabela de Huffman fixa: cada requisição web economiza bytes.'),
        ('\\faCalendarAlt', 'Agendamento', 'Escalonar tarefas por prazo (\\emph{earliest deadline first}) e alocar salas, frequências de rádio ou pistas de pouso são problemas gulosos parentes da seleção de atividades.'),
        ('\\faBrain', 'Aprendizado de máquina', 'Árvores de decisão escolhem gulosamente o atributo de maior ganho de informação (entropia!); o \\emph{hierarchical softmax} usa árvores de Huffman.'),
    ],
    exercicios=['(16.1-1) Escreva a seleção de atividades por programação dinâmica e compare com a gulosa.',
                '(16.1-3) Mostre que escolher a atividade mais curta (ou com menos conflitos) não é ótimo.',
                '(16.2-2) Resolva a mochila 0-1 por programação dinâmica em $O(nW)$. Por que a gulosa falha?',
                '(16.3-3) Qual o código de Huffman para frequências de Fibonacci $1, 1, 2, 3, 5, 8, 13, 21$?',
                'Comprima um livro em português (Domínio Público) com seu Huffman por caractere. Compare com \\texttt{gzip}.'],
    leitura='Cormen et al., seções 16.1 a 16.3.',
)

AULA_35 = dict(
    n=35, bloco=4, tema='Casamento de cadeias: o algoritmo de Knuth-Morris-Pratt', curto='Casamento de cadeias',
    cormen='seções 32.1 e 32.4',
    objetivos=['Definir o problema de casamento de cadeias e o algoritmo ingênuo',
               'Calcular a função de prefixo $\\pi$ de um padrão',
               'Executar o KMP e mostrar que ele é $\\Theta(n + m)$',
               'Medir o pior caso do ingênuo contra o KMP'],
    roteiro=['O problema, o ingênuo, a função de prefixo e o KMP',
             'KMP em C',
             'Texto $a^n$ e padrão $a^{99}b$: $(n - m + 1)m$ contra $\\le 3n$',
             'Buscadores, segurança, bioinformática e editores'],
    teoria=[
        dict(titulo='O problema', fig='32.1', altura=0.3, empilhar=True,
             legenda='o padrão $P = $ abaa ocorre no texto $T$ com deslocamento $s = 3$.',
             texto=r'''Dado um texto $T[1..n]$ e um padrão $P[1..m]$, achar todos os deslocamentos $s$ com $T[s+1..s+m] = P$.
\textbf{Ingênuo:} testa cada um dos $n - m + 1$ deslocamentos comparando até $m$ caracteres: $O((n - m + 1)m)$. Pior caso: $T = a^n$, $P = a^{m-1}b$.'''),
        dict(titulo='Os algoritmos do capítulo', fig='32.2', altura=0.3, empilhar=True,
             legenda='tempos de pré-processamento e de casamento.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Rabin-Karp}: compara hashes das janelas (aula 20); rápido em média, $O((n-m+1)m)$ no pior caso.
\item \textbf{Autômato finito}: $\Theta(n)$ para casar, mas pré-processamento $O(m|\Sigma|)$.
\item \textbf{KMP}: $\Theta(m)$ de pré-processamento e $\Theta(n)$ para casar, sem depender do alfabeto.
\end{itemize}'''),
        dict(titulo='A função de prefixo', fig='32.10', altura=0.48,
             legenda='(a) $q = 5$ caracteres casaram e o próximo falha; (b) desloca-se $P$ para o maior prefixo que é também sufixo; (c) $\\pi[5] = 3$.',
             texto=r'''$\pi[q]$ = tamanho do maior prefixo \textbf{próprio} de $P_q$ que também é \textbf{sufixo} de $P_q$.
\begin{itemize}\setlength{\itemsep}{4pt}
\item Depois de casar $q$ caracteres e falhar, não é preciso voltar no texto: o padrão continua da posição $\pi[q]$.
\item Os caracteres do texto nunca são relidos para trás.
\item Calcular $\pi$ é o KMP do padrão contra ele mesmo: $\Theta(m)$.
\end{itemize}''', largura_texto=0.40),
        dict(titulo='KMP', nome='KMP-Matcher($T, P$)',
             pseudo=r'''\State $\pi \atrib$ \Nome{Compute-Prefix-Function}($P$)
\State $q \atrib 0$ \Comment{caracteres casados}
\For{$i \atrib 1$ \textbf{até} $n$}
\While{$q > 0$ \textbf{e} $P[q+1] \ne T[i]$} \State $q \atrib \pi[q]$ \EndWhile
\If{$P[q+1] = T[i]$} \State $q \atrib q + 1$ \EndIf
\If{$q = m$}
\State imprima ``ocorrência com deslocamento'' $i - m$
\State $q \atrib \pi[q]$
\EndIf
\EndFor''',
             texto=r'''\textbf{Análise amortizada:} $q$ aumenta no máximo $n$ vezes (uma por caractere); cada volta do \textbf{enquanto} diminui $q$. Então o \textbf{enquanto} roda no máximo $n$ vezes no total.

\medskip Casamento: $\Theta(n)$. Total com o pré-processamento: $\Theta(n + m)$.''', largura_texto=0.40),
    ],
    pratica=dict(
        resumo=['Função de prefixo com índices de 0', 'KMP que relata todas as ocorrências (inclusive sobrepostas)',
                'Testes com o exemplo da Figura 32.10'],
        arquivos=[('aula35_kmp.c', 'Knuth-Morris-Pratt em C')]),
    experimento=dict(
        programa='aula35_experimento.c', titulo='O pior caso do ingênuo',
        pergunta='Com texto aⁿ e padrão a⁹⁹b, quantas comparações fazem o algoritmo ingênuo e o KMP?',
        resumo=['Texto $a^n$, padrão $a^{99}b$ ($m = 100$)', 'Ingênuo: exatamente $(n - m + 1)m$',
                'KMP: no máximo $3n$ (contando o teste que encerra cada laço)'],
        hipotese=r'''No ingênuo, cada deslocamento casa 99 caracteres antes de falhar no último: exatamente $(n - 99)\cdot100$ comparações.
No KMP, cada caractere do texto custa no máximo uma comparação no \textbf{se}, uma que encerra o \textbf{enquanto} e, amortizadas, as voltas do \textbf{enquanto}: no máximo $3n$.''',
        metodo=['$n$ de 10.000 a 160.000', 'Contador em toda comparação entre caracteres',
                'Mesma entrada para os dois algoritmos', 'Padrão ausente: nenhuma ocorrência'],
        graficos=[
            dict(titulo='Comparações: ingênuo contra KMP', ylabel='comparações', escala='logy',
                 series=[dict(col='ingenuo', rotulo='ingênuo'), dict(col='kmp', rotulo='KMP')],
                 teoria=[dict(col='ingenuo', f='(n-99)*100', rotulo='$(n-m+1)m$', ajustar=False, tolerancia=0.0001),
                         dict(col='kmp', f='3*n', rotulo='$3n$', limite='superior')],
                 leitura=r'Para $n = 160.000$: 16 milhões de comparações no ingênuo, 480 mil no KMP: 33 vezes menos, e a razão cresce com $m$.'),
        ],
        conclusao=r'''O ingênuo faz exatamente $(n - m + 1)m$ comparações no pior caso; o KMP fica abaixo de $3n$, \textbf{independente de $m$}.
A função de prefixo é uma pequena tabela que evita reler o texto: mais uma vez, pré-processar troca memória por tempo.'''),
    conexoes=[
        ('\\faSearch', 'Busca em texto', '\\texttt{grep}, o ``localizar'' dos editores e navegadores e as bibliotecas de strings usam KMP, Boyer-Moore ou variações para buscar em gigabytes.'),
        ('\\faShieldAlt', 'Segurança', 'Antivírus e sistemas de detecção de intrusão (Snort, Suricata) procuram milhares de assinaturas ao mesmo tempo com Aho-Corasick, a generalização do KMP.'),
        ('\\faDna', 'Bioinformática', 'Localizar motivos em DNA, sítios de restrição e sequências repetidas: casamento de cadeias sobre o alfabeto $\\{A, C, G, T\\}$.'),
        ('\\faCode', 'Compiladores', 'Analisadores léxicos reconhecem palavras-chave e tokens com autômatos finitos, o mesmo modelo da seção 32.3.'),
    ],
    exercicios=['(32.1-2) Se todos os caracteres de $P$ são diferentes, acelere o ingênuo para $O(n)$.',
                '(32.4-1) Calcule a função de prefixo de ababbabbabbababbabb.',
                '(32.4-7) Decida se $T$ é uma rotação cíclica de $T\'$ em tempo linear.',
                '(32.2-1) Simule o Rabin-Karp com módulo 11 em $T = $ 3141592653589793 e $P = 26$: quantos alarmes falsos?',
                'Meça o experimento com texto aleatório em português. O ingênuo ainda perde? Por quê?'],
    leitura='Cormen et al., seções 32.1, 32.2 e 32.4.',
)

PROJETO_4 = dict(
    n=36, bloco=4, tipo='projeto', tema='Projeto 4: rotas e redes numa cidade real',
    descricao='Apresentação dos projetos finais. Cada equipe monta o grafo de ruas de um bairro de Salvador (OpenStreetMap) e resolve problemas reais com os algoritmos do bloco, comparando teoria e medições.',
    entregas=['Grafo de ruas extraído do OpenStreetMap (vértices = cruzamentos, arestas = trechos com comprimento), com pelo menos 10 mil vértices',
              'Menor caminho entre dois endereços com BFS (número de quarteirões), Dijkstra com vetor e com heap, e Bellman-Ford; tempos medidos e confrontados com a teoria',
              'Rede de menor custo ligando pontos de interesse (escolas, postos de saúde) com Kruskal ou Prim',
              'Uma técnica de projeto aplicada: programação dinâmica (por exemplo, rota que visita pontos em ordem) ou gulosa (por exemplo, cobertura de pontos)',
              'Apresentação de 10 minutos com mapa e demonstração ao vivo'],
)

AULAS_B4 = [AULA_28, AULA_29, AULA_30, AULA_31, AULA_32, AULA_33, AULA_34, AULA_35, PROJETO_4]
