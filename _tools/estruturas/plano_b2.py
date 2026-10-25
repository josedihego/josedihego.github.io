"""Bloco 2 – Dicionários e estruturas lineares (aulas 10 a 18)."""

AULA_10 = dict(
    n=10, bloco=2, tema='Dicionários e conjuntos dinâmicos', curto='Dicionários',
    cormen='introdução da parte III e seção 10.1',
    objetivos=['Definir conjunto dinâmico e as operações de dicionário',
               'Separar consultas (busca, mínimo, máximo, sucessor) de modificações (inserção, remoção)',
               'Implementar um dicionário em vetor ordenado com busca binária',
               'Medir o custo de inserir e de buscar em vetor ordenado e desordenado'],
    roteiro=['O tipo abstrato de dados, as operações e uma tabela de custos',
             'Dicionário em vetor ordenado com consultas de ordem',
             'Vetor ordenado contra desordenado: $n^2/4$, $n\\lg n$ e $n^2/2$',
             'Bancos de dados, linguagens, compiladores e redes'],
    teoria=[
        dict(titulo='Conjuntos dinâmicos',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Um \textbf{conjunto dinâmico} cresce, encolhe e muda ao longo da execução do algoritmo.
\item Cada elemento é um objeto com uma \textbf{chave} (que o identifica) e \textbf{dados satélite}.
\item Um \textbf{dicionário} é um conjunto dinâmico com \Nome{Insert}, \Nome{Delete} e \Nome{Search}.
\item Separar o \textbf{tipo abstrato} (o que as operações fazem) da \textbf{implementação} (como): o mesmo programa pode trocar a estrutura por baixo.
\end{itemize}''',
             rodape=r'Os blocos 2 e 3 são sobre isso: o mesmo dicionário em vetores, listas, tabelas hash e árvores, cada um com seus custos.'),
        dict(titulo='As operações (Cormen, parte III)',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.48\textwidth}
\begin{cartao}{cteoria}\textbf{Consultas}\par\footnotesize
\begin{itemize}\item \Nome{Search}($S, k$): o elemento de chave $k$, ou \textsc{nil}.
\item \Nome{Minimum}($S$), \Nome{Maximum}($S$).
\item \Nome{Successor}($S, x$), \Nome{Predecessor}($S, x$): o próximo e o anterior na ordem das chaves.\end{itemize}\end{cartao}
\end{column}\begin{column}{0.48\textwidth}
\begin{cartao}{cpratica}\textbf{Modificações}\par\footnotesize
\begin{itemize}\item \Nome{Insert}($S, x$): acrescenta $x$.
\item \Nome{Delete}($S, x$): remove $x$ (dado o elemento, não só a chave).\end{itemize}\end{cartao}
\end{column}\end{columns}
\medskip Analisa-se o custo de cada operação em função de $n = |S|$.'''),
        dict(titulo='Primeiras implementações',
             texto=r'''\renewcommand{\arraystretch}{1.3}\begin{tabular}{lccccc}\toprule
 & \textbf{Search} & \textbf{Insert} & \textbf{Delete} & \textbf{Min/Max} & \textbf{Successor}\\\midrule
vetor desordenado & $\Theta(n)$ & $O(1)$ & $\Theta(n)$ & $\Theta(n)$ & $\Theta(n)$\\
vetor ordenado & $\Theta(\lg n)$ & $\Theta(n)$ & $\Theta(n)$ & $O(1)$ & $O(\lg n)$\\
lista ligada (aulas 14–16) & $\Theta(n)$ & $O(1)$ & $O(1)$ dado o nó & $\Theta(n)$ & $\Theta(n)$\\
endereçamento direto (aula 19) & $O(1)$ & $O(1)$ & $O(1)$ & $\Theta(m)$ & $\Theta(m)$\\
\textbf{tabela hash} (aulas 19–21) & $O(1)$ médio & $O(1)$ & $O(1)$ & $\Theta(n)$ & $\Theta(n)$\\
\textbf{árvore balanceada} (aulas 24–25) & $O(\lg n)$ & $O(\lg n)$ & $O(\lg n)$ & $O(\lg n)$ & $O(\lg n)$\\\bottomrule\end{tabular}''',
             rodape=r'Nenhuma estrutura vence em tudo: a escolha depende de quais operações o programa mais usa.'),
        dict(titulo='Busca binária num vetor ordenado', nome='Binary-Search($A, k$)',
             pseudo=r'''\State $\mathit{lo} \atrib 1$;\quad $\mathit{hi} \atrib n$
\While{$\mathit{lo} \le \mathit{hi}$}
\State $m \atrib \lfloor(\mathit{lo} + \mathit{hi})/2\rfloor$
\If{$A[m] = k$} \State \Return $m$
\ElsIf{$A[m] < k$} \State $\mathit{lo} \atrib m + 1$
\Else \State $\mathit{hi} \atrib m - 1$
\EndIf
\EndWhile
\State \Return \textsc{nil}''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Cada comparação descarta metade do intervalo: $T(n) = T(n/2) + \Theta(1) = \Theta(\lg n)$ (exercício 2.3-5).
\item Inserir mantendo a ordem exige deslocar, em média, metade dos elementos: $\Theta(n)$.
\item Em C, \texttt{lo + (hi - lo) / 2} evita estouro de inteiro.
\end{itemize}''', largura_texto=0.44),
    ],
    pratica=dict(
        resumo=['Busca binária que devolve a posição de inserção', 'Inserção e remoção com deslocamento; mínimo e máximo em $O(1)$',
                'Sucessor em $O(\\lg n)$; comandos \\texttt{i}, \\texttt{r}, \\texttt{b}, \\texttt{m}, \\texttt{M}, \\texttt{s}, \\texttt{p}'],
        arquivos=[('aula10_dicionario.c', 'Dicionário em vetor ordenado')]),
    experimento=dict(
        programa='aula10_experimento.c', titulo='Ordenado ou desordenado?',
        pergunta='Quanto custam n inserções e n buscas num dicionário em vetor ordenado e em vetor desordenado?',
        resumo=['Ordenado: inserir desloca $\\approx n^2/4$; buscar custa $\\approx n\\lg n$',
                'Desordenado: inserir não desloca; buscar custa $n(n+1)/2$', '$n$ de 1.000 a 16.000 chaves aleatórias'],
        hipotese=r'''No vetor ordenado, a $i$-ésima inserção desloca em média $i/2$ elementos: total $\approx n^2/4$. As $n$ buscas binárias custam $\approx n\lg n$ comparações.
No desordenado, inserir é só colocar no fim; mas a busca com sucesso pelo $i$-ésimo elemento examina $i$ posições: total $n(n+1)/2$.''',
        metodo=['Mesmas $n$ chaves aleatórias nas duas estruturas', 'Contadores de deslocamentos e de comparações',
                '$n$ de 1.000 a 16.000', 'Buscas por todas as chaves inseridas'],
        graficos=[
            dict(titulo='Inserções e buscas', ylabel='operações', escala='logy',
                 series=[dict(col='des_busca', rotulo='desordenado: buscas'), dict(col='ord_insercao', rotulo='ordenado: inserções'),
                         dict(col='ord_busca', rotulo='ordenado: buscas')],
                 teoria=[dict(col='ord_busca', f='n*log2(n)', rotulo='$n\\lg n$', ajustar=False, tolerancia=0.03),
                         dict(col='ord_insercao', f='n*n/4', rotulo='$n^2/4$', ajustar=False, tolerancia=0.03),
                         dict(col='des_busca', f='n*(n+1)/2', rotulo='$\\frac{n(n+1)}{2}$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Vetor ordenado: buscar é barato ($n\lg n$), inserir é caro ($n^2/4$). Desordenado: o contrário. Hash e árvores (bloco 3) acabam com esse dilema.'),
        ],
        conclusao=r'''As três previsões se confirmam: $n^2/4$ deslocamentos e $n\lg n$ comparações no vetor ordenado, $n(n+1)/2$ comparações no desordenado.
Vetores obrigam a escolher entre inserir rápido e buscar rápido. O resto do curso mostra estruturas que fazem as duas coisas em $O(1)$ ou $O(\lg n)$.'''),
    conexoes=[
        ('\\faDatabase', 'Bancos de dados', 'Uma tabela é um conjunto dinâmico de registros; índices são dicionários sobre uma coluna, e o otimizador escolhe entre varrer e buscar conforme o custo.'),
        ('\\faPython', 'Linguagens', '\\texttt{dict} e \\texttt{set} do Python, \\texttt{Map} do JavaScript, \\texttt{std::map} e \\texttt{std::unordered\\_map} do C++: o mesmo tipo abstrato com implementações diferentes.'),
        ('\\faCogs', 'Compiladores', 'A tabela de símbolos é um dicionário de identificadores; escopos aninhados viram uma pilha de dicionários (aula 11).'),
        ('\\faNetworkWired', 'Redes', 'Tabelas ARP, de rotas e de conexões são dicionários consultados milhões de vezes por segundo: a implementação define a latência.'),
    ],
    exercicios=['Escreva \\Nome{Predecessor}($S, x$) para o vetor ordenado.',
                '(2.3-5) Escreva a busca binária recursiva e prove que é $\\Theta(\\lg n)$.',
                '(2.3-7) Dado um conjunto $S$ de $n$ inteiros e $x$, decida em $\\Theta(n\\lg n)$ se há dois elementos com soma $x$.',
                'Implemente o mesmo dicionário em vetor desordenado e compare os dois com 50\\% de buscas e 50\\% de inserções.',
                'Em que proporção de buscas e inserções o vetor ordenado passa a valer a pena? Meça.'],
    leitura='Cormen et al., introdução da parte III (conjuntos dinâmicos) e exercício 2.3-5.',
)

AULA_11 = dict(
    n=11, bloco=2, tema='Pilhas', curto='Pilhas',
    cormen='seção 10.1',
    objetivos=['Implementar pilhas em vetor (com transbordamento) e em lista ligada',
               'Analisar \\Nome{Push} e \\Nome{Pop} em $O(1)$',
               'Avaliar expressões pós-fixas com uma pilha',
               'Medir o custo por operação das duas implementações'],
    roteiro=['LIFO, as operações, as duas implementações e o que pode dar errado',
             'Pilha em vetor e em lista; avaliador de expressões pós-fixas',
             'Tempo por operação: vetor contra lista ligada',
             'Compiladores, navegadores, sistemas operacionais e IA'],
    teoria=[
        dict(titulo='Último a entrar, primeiro a sair', fig='10.1', altura=0.32, empilhar=True,
             legenda='pilha $S$ em vetor: (a) 4 elementos; (b) após \\Nome{Push}(17) e \\Nome{Push}(3); (c) após \\Nome{Pop}, que devolve 3.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{3pt}
\item O elemento removido é sempre o \textbf{mais recente}: política LIFO.
\item $S.\mathit{topo}$ indica o último; a pilha é $S[1..S.\mathit{topo}]$. Vazia se $S.\mathit{topo} = 0$.
\item Remover de pilha vazia é \textbf{esvaziamento} (\emph{underflow}); inserir em pilha cheia é \textbf{transbordamento} (\emph{overflow}).
\end{itemize}'''),
        dict(titulo='As operações', nome='Push($S, x$) e Pop($S$)',
             pseudo=r'''\State \Comment{\Nome{Push}($S, x$)}
\State $S.\mathit{topo} \atrib S.\mathit{topo} + 1$
\State $S[S.\mathit{topo}] \atrib x$
\State \Comment{\Nome{Pop}($S$)}
\If{\Nome{Stack-Empty}($S$)} \State \textbf{erro} ``esvaziamento''
\Else
\State $S.\mathit{topo} \atrib S.\mathit{topo} - 1$
\State \Return $S[S.\mathit{topo} + 1]$
\EndIf''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Todas $O(1)$.
\item \textbf{Em vetor}: memória contígua, rápida; capacidade fixa (ou vetor dinâmico, aula 13).
\item \textbf{Em lista ligada}: \Nome{Push} insere na cabeça, \Nome{Pop} remove a cabeça (exercício 10.2-2). Sem limite, mas um \texttt{malloc} por elemento.
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Aplicação: expressões pós-fixas',
             texto=r'''\textbf{Notação pós-fixa} (polonesa reversa): o operador vem depois dos operandos, sem parênteses.
\[(3 + 4) \times 2 \quad\longrightarrow\quad 3\;4\;+\;2\;\times\]
\begin{itemize}\setlength{\itemsep}{4pt}
\item Leia da esquerda para a direita: número $\Rightarrow$ \Nome{Push}; operador $\Rightarrow$ dois \Nome{Pop}, calcule, \Nome{Push} do resultado.
\item No fim, a pilha tem exatamente um valor: a resposta. Qualquer outra situação é expressão inválida.
\item Converter de infixa para pós-fixa também usa uma pilha (algoritmo \emph{shunting-yard} de Dijkstra), com as precedências dos operadores.
\end{itemize}''',
             rodape=r'Pilhas também verificam parênteses balanceados, implementam recursão (a pilha de chamadas) e o ``desfazer'' dos editores.'),
    ],
    pratica=dict(
        resumo=['\\texttt{PilhaVetor} com transbordamento e \\texttt{PilhaLista} sem limite', 'Mesma interface: empilha, desempilha, vazia',
                'Avaliador de expressões pós-fixas usando as duas'],
        arquivos=[('aula11_pilha.c', 'Pilhas e expressões pós-fixas em C')]),
    experimento=dict(
        programa='aula11_experimento.c', titulo='Mesmo $O(1)$, custos diferentes',
        pergunta='Quanto custa, em nanossegundos, cada operação de pilha em vetor e em lista ligada?',
        resumo=['$n$ \\Nome{Push} seguidos de $n$ \\Nome{Pop}', 'Tempo por operação, melhor de 5',
                '$n$ de 4 mil a 4 milhões'],
        hipotese=r'''As duas implementações são $O(1)$ por operação: o tempo \textbf{por operação} deve ficar \textbf{constante} quando $n$ cresce.
A constante deve ser bem maior na lista: cada \Nome{Push} chama \texttt{malloc} e cada \Nome{Pop}, \texttt{free}, e os nós ficam espalhados na memória.''',
        metodo=['Vetor alocado de uma vez; lista com um nó por elemento', '$n = 2^{12}, \\dots, 2^{22}$',
                'Tempo total dividido por $2n$ operações', 'Mínimo de 5 repetições'],
        graficos=[
            dict(titulo='Tempo por operação', ylabel='ns por operação', escala='log',
                 series=[dict(col='lista_ns', rotulo='lista ligada'), dict(col='vetor_ns', rotulo='vetor')],
                 teoria=[dict(col='lista_ns', f='1', rotulo='constante', tolerancia=0.15)],
                 leitura=r'Lista: cerca de 7 ns por operação, constante. Vetor: menos de 1 ns, também constante (a oscilação é o cache).'),
        ],
        conclusao=r'''As duas implementações têm custo \textbf{constante} por operação, como prevê a análise, mas a lista ligada é cerca de \textbf{25 vezes} mais cara: \texttt{malloc}, \texttt{free} e saltos pela memória.
A notação $O$ esconde constantes; quando a capacidade é previsível, o vetor (ou o vetor dinâmico da aula 13) é a melhor pilha.'''),
    conexoes=[
        ('\\faCogs', 'Compiladores', 'Analisadores sintáticos casam parênteses e blocos com pilhas; a máquina virtual da JVM e a do Python são \\emph{máquinas de pilha}: \\texttt{iadd} desempilha dois e empilha a soma.'),
        ('\\faGlobe', 'Navegadores e editores', 'Voltar e avançar, desfazer e refazer: duas pilhas. Calculadoras HP usavam notação pós-fixa por ser mais rápida de digitar e de avaliar.'),
        ('\\faDesktop', 'Sistemas operacionais', 'Cada \\emph{thread} tem sua pilha de chamadas; o estouro dela (\\emph{stack overflow}) é o transbordamento desta aula, em hardware.'),
        ('\\faChessKnight', 'Inteligência artificial', 'Busca em profundidade com \\emph{backtracking} (labirintos, sudoku, provadores de teoremas) guarda as alternativas pendentes numa pilha (aula 29).'),
    ],
    exercicios=['(10.1-1) Ilustre \\Nome{Push}(4), \\Nome{Push}(1), \\Nome{Push}(3), \\Nome{Pop}, \\Nome{Push}(8), \\Nome{Pop} numa pilha vazia em $S[1..6]$.',
                '(10.1-2) Implemente duas pilhas num só vetor $A[1..n]$ sem transbordamento enquanto houver espaço.',
                '(10.2-2) Implemente uma pilha com lista simplesmente ligada; \\Nome{Push} e \\Nome{Pop} em $O(1)$.',
                'Implemente a conversão de infixa para pós-fixa (\\emph{shunting-yard}) com $+$, $-$, $\\times$, $/$ e parênteses.',
                'Use uma pilha para verificar se um arquivo HTML tem as marcas bem aninhadas.'],
    leitura='Cormen et al., seção 10.1 e exercício 10.2-2.',
)

AULA_12 = dict(
    n=12, bloco=2, tema='Filas', curto='Filas',
    cormen='seção 10.1',
    objetivos=['Implementar filas em vetor circular e em lista ligada',
               'Distinguir fila cheia de fila vazia',
               'Conhecer deques (filas de duas pontas)',
               'Simular uma fila de atendimento e conferir com a teoria das filas'],
    roteiro=['FIFO, cabeça e cauda, o vetor circular, a fila ligada e o deque',
             'Fila circular e fila ligada em C',
             'Simulação M/M/1: espera média contra $\\rho/(1-\\rho)$',
             'Sistemas operacionais, redes, simulação e computação em nuvem'],
    teoria=[
        dict(titulo='Primeiro a entrar, primeiro a sair', fig='10.2', altura=0.5,
             legenda='(a) fila com 5 elementos em $Q[7..11]$; (b) após \\Nome{Enqueue} de 17, 3 e 5: a cauda dá a volta; (c) após \\Nome{Dequeue}.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Sai sempre o elemento há mais tempo na fila: política FIFO.
\item $Q.\mathit{cabeça}$: o próximo a sair. $Q.\mathit{cauda}$: a próxima posição livre.
\item Os índices andam ``em círculo'': depois de $n$ vem 1 (em C: \texttt{(i + 1) \% n}).
\item Vazia: $\mathit{cabeça} = \mathit{cauda}$. Cheia: $\mathit{cabeça} = \mathit{cauda} + 1$. Com $n$ posições, cabem $n - 1$ elementos (ou guarde a contagem).
\end{itemize}''', largura_texto=0.44),
        dict(titulo='As operações', nome='Enqueue($Q, x$) e Dequeue($Q$)',
             pseudo=r'''\State \Comment{\Nome{Enqueue}($Q, x$)}
\State $Q[Q.\mathit{cauda}] \atrib x$
\If{$Q.\mathit{cauda} = Q.\mathit{comprimento}$} \State $Q.\mathit{cauda} \atrib 1$
\Else \State $Q.\mathit{cauda} \atrib Q.\mathit{cauda} + 1$ \EndIf
\State \Comment{\Nome{Dequeue}($Q$)}
\State $x \atrib Q[Q.\mathit{cabeça}]$
\If{$Q.\mathit{cabeça} = Q.\mathit{comprimento}$} \State $Q.\mathit{cabeça} \atrib 1$
\Else \State $Q.\mathit{cabeça} \atrib Q.\mathit{cabeça} + 1$ \EndIf
\State \Return $x$''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Ambas $O(1)$; o livro omite os testes de cheia e vazia (exercício 10.1-4).
\item \textbf{Fila ligada}: entra na cauda, sai da cabeça; com ponteiros para as duas pontas, $O(1)$ sem limite de tamanho.
\item \textbf{Deque} (exercício 10.1-5): inserir e remover nas duas pontas, também $O(1)$ num vetor circular.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='Filas no mundo: teoria das filas',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Clientes chegam ao acaso (taxa $\lambda$) e são atendidos um por vez (taxa $\mu$), em ordem de chegada: a fila \textbf{M/M/1}.
\item Utilização $\rho = \lambda/\mu < 1$; se $\rho \ge 1$, a fila cresce sem limite.
\item Resultado clássico: o tempo médio de espera \textbf{na fila} é
\[W_q = \frac{\rho}{\mu - \lambda} = \frac{\rho}{1 - \rho}\quad\text{(com } \mu = 1\text{)}.\]
\item Não linear: com $\rho = 0{,}5$, espera-se 1 atendimento; com $\rho = 0{,}9$, 9.
\end{itemize}''',
             rodape=r'Um simulador de eventos discretos é exatamente uma fila FIFO de clientes mais um relógio: é o experimento desta aula.'),
    ],
    pratica=dict(
        resumo=['Fila circular de 4 posições com contagem', 'Fila ligada com ponteiros para cabeça e cauda',
                'Comandos \\texttt{e x} (enfileira) e \\texttt{d} (desenfileira)'],
        arquivos=[('aula12_fila.c', 'Filas em C')]),
    experimento=dict(
        programa='aula12_experimento.c', titulo='Uma fila de banco, simulada',
        pergunta='Na simulação de uma fila M/M/1, o tempo médio de espera segue ρ/(1−ρ)?',
        resumo=['Chegadas e atendimentos exponenciais; atendimento médio = 1', 'Fila circular dos instantes de chegada',
                '2 milhões de clientes para cada $\\rho$ de 0,05 a 0,85'],
        hipotese=r'''Com chegadas de taxa $\rho$ e atendimentos de taxa 1, a teoria das filas prevê espera média na fila de $\rho/(1-\rho)$.
A espera deve explodir perto de $\rho = 1$: dobrar a ocupação de 40\% para 80\% multiplica a espera por 6.''',
        metodo=['Simulação de eventos: próximo evento é uma chegada ou um fim de atendimento', 'Chegadas guardadas numa fila FIFO circular',
                'Espera = início do atendimento $-$ instante de chegada', '$\\rho = 0{,}05, 0{,}10, \\dots, 0{,}85$'],
        graficos=[
            dict(titulo='Espera média na fila', x='rho', xlabel='utilização $\\rho$', ylabel='espera média (atendimentos)',
                 series=[dict(col='espera', rotulo='simulação')],
                 teoria=[dict(col='espera', f='n/(1-n)', rotulo='$\\rho/(1-\\rho)$', ajustar=False, tolerancia=0.03)],
                 leitura=r'Com $\rho = 0{,}85$, a espera média é de 5,7 atendimentos. A curva é a mesma de filas de banco, de CPUs e de roteadores.'),
        ],
        conclusao=r'''A simulação reproduz $\rho/(1-\rho)$ com erro de poucos por cento. A fila FIFO, uma estrutura simples, é o coração de toda simulação de atendimento.
A lição prática: um sistema com 85\% de ocupação já tem esperas longas; perto de 100\%, elas explodem.'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'Processos prontos esperam numa fila; o escalonamento \\emph{round robin} é uma fila circular. Buffers de teclado, disco e impressão são filas.'),
        ('\\faNetworkWired', 'Redes', 'Roteadores guardam pacotes em filas de saída; a teoria das filas desta aula explica o atraso e a perda quando o enlace fica congestionado.'),
        ('\\faCloud', 'Computação em nuvem', 'Filas de mensagens (RabbitMQ, Kafka, SQS) desacoplam serviços: quem produz enfileira, quem consome desenfileira no seu ritmo.'),
        ('\\faProjectDiagram', 'Algoritmos de grafos', 'A busca em largura (aula 28) explora um grafo camada por camada usando exatamente uma fila FIFO.'),
    ],
    exercicios=['(10.1-3) Ilustre \\Nome{Enqueue}(4), \\Nome{Enqueue}(1), \\Nome{Enqueue}(3), \\Nome{Dequeue}, \\Nome{Enqueue}(8), \\Nome{Dequeue} em $Q[1..6]$.',
                '(10.1-4) Reescreva \\Nome{Enqueue} e \\Nome{Dequeue} detectando esvaziamento e transbordamento.',
                '(10.1-5) Implemente um deque com as quatro operações em $O(1)$ num vetor circular.',
                '(10.1-6) Implemente uma fila com duas pilhas. Qual o custo amortizado por operação?',
                'Altere a simulação para dois atendentes (M/M/2) e compare a espera com a de um atendente duas vezes mais rápido.'],
    leitura='Cormen et al., seção 10.1.',
)

AULA_13 = dict(
    n=13, bloco=2, tema='Vetores dinâmicos e análise amortizada', curto='Vetores dinâmicos',
    cormen='seções 17.1 e 17.4',
    objetivos=['Fazer um vetor crescer e encolher conforme o uso',
               'Calcular o custo amortizado pelo método agregado',
               'Entender por que encolher só com $1/4$ de ocupação',
               'Medir $2n$ cópias contra $n^2/2000$ para duas estratégias de crescimento'],
    roteiro=['Tabela dinâmica, método agregado, expansão e contração',
             'Vetor dinâmico em C com expansão e contração',
             'Dobrar ou somar 1000? Contando cópias',
             'Linguagens, bancos de dados, redes e sistemas embarcados'],
    teoria=[
        dict(titulo='Quando o vetor enche', fig='17.3', altura=0.58,
             legenda='tamanho alocado ($\\mathit{size}_i$), ocupação ($\\mathit{num}_i$) e potencial $\\Phi_i$ ao longo de 32 inserções.',
             texto=r'''\Nome{Table-Insert}: ao encher, aloque o \textbf{dobro} e copie tudo.
\begin{itemize}\setlength{\itemsep}{4pt}
\item Uma inserção pode custar $\Theta(n)$ (a cópia).
\item Mas as cópias só acontecem nas potências de 2.
\item O pior caso de \textbf{uma} operação não diz o custo de uma \textbf{sequência}.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='Análise amortizada: método agregado',
             texto=r'''Seja $c_i$ o custo da $i$-ésima inserção: $c_i = i$ se $i - 1$ é potência de 2 (há cópia), senão $c_i = 1$.
\[\sum_{i=1}^{n} c_i \;\le\; n + \sum_{j=0}^{\lfloor\lg n\rfloor} 2^j \;<\; n + 2n \;=\; 3n\]
\begin{itemize}\setlength{\itemsep}{4pt}
\item Custo \textbf{amortizado}: $3n/n = O(1)$ por inserção, \textbf{garantido} (não é caso médio: vale para qualquer sequência).
\item Crescer somando uma constante $c$: as cópias somam $c + 2c + 3c + \dots \approx n^2/(2c)$. Quadrático, por maior que seja $c$.
\item Os métodos contábil e do potencial (seções 17.2 e 17.3) dão o mesmo resultado com outra contabilidade.
\end{itemize}'''),
        dict(titulo='E para encolher?',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item Ideia ingênua: encolher pela metade quando a ocupação cair para $1/2$.
\item Problema: com o vetor cheio, insere (dobra), remove (encolhe), insere (dobra)\dots: \textbf{toda} operação copia $n$ elementos.
\item Solução (seção 17.4.2): dobrar ao encher, mas só encolher quando a ocupação cair para $\mathbf{1/4}$.
\item Depois de uma mudança de tamanho, a ocupação é $1/2$: é preciso muitas operações até a próxima.
\item Inserções e remoções em qualquer ordem: $O(1)$ amortizado.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Expansão ao encher; contração com $1/4$', 'Contador de cópias embutido no vetor',
                'Testes: capacidade depois de inserir e remover'],
        arquivos=[('aula13_vetor_dinamico.c', 'Vetor dinâmico em C')]),
    experimento=dict(
        programa='aula13_experimento.c', titulo='Dobrar ou somar 1000?',
        pergunta='Quantas cópias custam n inserções num vetor que dobra e num que cresce 1000 posições por vez?',
        resumo=['Dobrar: $\\approx 2n$ cópias (amortizado $O(1)$)', 'Somar 1000: $500\\,m(m+1) \\approx n^2/2000$ cópias',
                '$n = 2^k + 1$: logo após uma expansão'],
        hipotese=r'''Dobrando, as cópias são $1 + 2 + 4 + \dots + 2^k = 2^{k+1} - 1 \approx 2n$ quando $n = 2^k + 1$: amortizado, \textbf{2 cópias por inserção}.
Somando 1000 posições, há $m = \lfloor (n-1)/1000\rfloor$ expansões que copiam $1000, 2000, \dots, 1000m$: total $500\,m(m+1) \approx n^2/2000$.''',
        metodo=['Simulação da capacidade e das cópias (sem alocar de verdade)', '$n = 2^{10} + 1, \\dots, 2^{20} + 1$',
                'Capacidade inicial: 1 (dobra) e 1000 (soma)', 'Contagem exata, sem ruído'],
        graficos=[
            dict(titulo='Cópias para $n$ inserções', ylabel='cópias', escala='log',
                 series=[dict(col='mais_mil', rotulo='somar 1000'), dict(col='dobra', rotulo='dobrar')],
                 teoria=[dict(col='mais_mil', f='500*((n-1)//1000)*((n-1)//1000+1)', rotulo='$500\\,m(m+1) \\approx n^2/2000$', ajustar=False, tolerancia=0.0001),
                         dict(col='dobra', f='2*n', rotulo='$2n$', ajustar=False, tolerancia=0.01)],
                 leitura=r'Para um milhão de inserções: 2 milhões de cópias dobrando, 550 milhões somando 1000.'),
        ],
        conclusao=r'''Dobrar custa $\approx 2n$ cópias: \textbf{amortizado $O(1)$} por inserção. Somar uma constante custa $\approx n^2/2000$: quadrático, por maior que seja a constante.
Por isso \texttt{std::vector}, \texttt{ArrayList} e as listas do Python crescem por um \textbf{fator} (1,5 ou 2), nunca por uma quantidade fixa.'''),
    conexoes=[
        ('\\faPython', 'Linguagens', 'A lista do Python cresce cerca de 12\\%, o \\texttt{vector} do C++ (GCC) dobra e o \\texttt{ArrayList} do Java cresce 50\\%: fatores diferentes, todos amortizados $O(1)$.'),
        ('\\faDatabase', 'Bancos de dados', 'Tabelas hash de bancos e caches (Redis) dobram de tamanho e reinserem tudo, às vezes aos poucos (\\emph{rehash} incremental) para não travar o serviço.'),
        ('\\faNetworkWired', 'Redes', 'O TCP aumenta a janela de envio por fator e a reduz pela metade em congestionamento: crescimento multiplicativo, como o vetor dinâmico.'),
        ('\\faMicrochip', 'Sistemas embarcados', 'Em tempo real, um pico de $\\Theta(n)$ numa cópia pode estourar um prazo: lá se prefere capacidade fixa ou crescimento sem cópia (listas de blocos).'),
    ],
    exercicios=['(17.1-3) Uma sequência de $n$ operações em que a $i$-ésima custa $i$ se $i$ é potência de 2 e 1 senão: custo amortizado?',
                '(17.4-2) Mostre que, se a ocupação está acima de $1/2$ e a operação é remoção, o custo amortizado é limitado por uma constante.',
                'Mostre uma sequência de $n$ operações com custo $\\Theta(n^2)$ quando o vetor encolhe já com $1/2$ de ocupação.',
                'Altere o experimento para crescer por fator 1,5 e compare com o fator 2 (cópias e memória desperdiçada).',
                'Implemente uma fila em vetor circular que dobra quando enche.'],
    leitura='Cormen et al., seções 17.1 (método agregado) e 17.4 (tabelas dinâmicas).',
)

AULA_14 = dict(
    n=14, bloco=2, tema='Listas simplesmente ligadas', curto='Listas simplesmente ligadas',
    cormen='seção 10.2',
    objetivos=['Representar uma sequência com nós e ponteiros',
               'Inserir no início e no fim, buscar e remover',
               'Inverter uma lista sem memória extra',
               'Medir a vantagem da lista na inserção e o custo do cache no percurso'],
    roteiro=['Nós, ponteiros, cabeça e cauda; o que custa cada operação',
             'Lista simples em C: insere, remove e inverte',
             'Inserir no início; percorrer uma lista espalhada pela memória',
             'Sistemas operacionais, alocação de memória, arquitetura e editores'],
    teoria=[
        dict(titulo='Lista ligada',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Os elementos ficam em \textbf{nós} espalhados pela memória; cada nó tem a \textit{chave} e um ponteiro \textit{prox} para o seguinte.
\item $L.\mathit{cabeça}$ aponta o primeiro; o último tem $\mathit{prox} = \textsc{nil}$. Lista vazia: $L.\mathit{cabeça} = \textsc{nil}$.
\item A ordem é dada pelos ponteiros, não pela posição na memória (ao contrário do vetor).
\item Tamanho flexível: cresce e encolhe um nó por vez, sem cópias.
\end{itemize}''',
             rodape=r'Variações (Cormen, 10.2): simplesmente ou duplamente ligada; ordenada ou não; linear ou circular; com ou sem sentinela. Esta aula: a mais simples.'),
        dict(titulo='As operações e seus custos',
             texto=r'''\footnotesize\renewcommand{\arraystretch}{1.25}\begin{tabular}{lll}\toprule \textbf{Operação} & \textbf{Como} & \textbf{Custo}\\\midrule
inserir no início & novo nó aponta a cabeça; cabeça $\atrib$ novo & $O(1)$\\
inserir no fim & com ponteiro para a cauda & $O(1)$\\
buscar uma chave & percorrer desde a cabeça & $\Theta(n)$ no pior caso\\
remover dado o nó & é preciso o nó \textbf{anterior} & $\Theta(n)$ para achá-lo\\
inverter & virar cada ponteiro, uma passada & $\Theta(n)$, $O(1)$ de memória\\
acessar o $k$-ésimo & seguir $k$ ponteiros & $\Theta(k)$ (vetor: $O(1)$)\\\bottomrule\end{tabular}

\medskip Remover exige casos especiais: a cabeça (não há anterior) e a cauda (precisa ser atualizada).''',
             rodape=r'É por isso que existe a lista duplamente ligada (aula 15): com o ponteiro \textit{ant}, remover um nó dado custa $O(1)$.'),
        dict(titulo='Do vetor à lista', fig='10.3', altura=0.38, empilhar=True,
             legenda='lista duplamente ligada $\\langle 9, 16, 4, 1\\rangle$, inserção de 25 e remoção de 4. Na lista simples, só existem os ponteiros \\textit{next}.',
             texto=r'''\textbf{Vetor:} acesso por posição em $O(1)$, inserir no meio desloca $\Theta(n)$, memória contígua (amiga do cache).\quad
\textbf{Lista:} acesso por posição $\Theta(n)$, inserir dado o lugar em $O(1)$, memória espalhada (um nó por vez).'''),
    ],
    pratica=dict(
        resumo=['Cabeça e cauda: inserir nas duas pontas em $O(1)$', 'Remoção guardando o anterior; os casos da cabeça e da cauda',
                'Inversão em uma passada (exercício 10.2-7)'],
        arquivos=[('aula14_lista_simples.c', 'Lista simplesmente ligada em C')]),
    experimento=dict(
        programa='aula14_experimento.c', titulo='Ponteiros contra vizinhança',
        pergunta='Quanto custa inserir no início de um vetor? E percorrer uma lista ligada cujos nós estão espalhados pela memória?',
        resumo=['Inserir $n$ vezes no início: vetor desloca $n(n-1)/2$; lista, nada',
                'Percorrer: tempo por elemento de vetor e de lista, $n$ até $2^{24}$', 'Nós da lista em ordem aleatória na memória'],
        hipotese=r'''Inserir no início de um vetor desloca todos os elementos: $n$ inserções movem $n(n-1)/2$ elementos; a lista só ajusta ponteiros.
Para percorrer, os dois são $\Theta(n)$ no modelo RAM. Mas a CPU busca a memória em blocos (linhas de cache): o vetor aproveita cada bloco, a lista espalhada não. Esperamos o mesmo $\Theta(n)$ com \textbf{constantes muito diferentes}.''',
        metodo=['Contagem exata dos deslocamentos', 'Percurso: $n = 2^{10}$ a $2^{24}$; cerca de 33 milhões de visitas por medida',
                'Nós da lista embaralhados (Fisher–Yates)', 'Tempo dividido pelo número de visitas'],
        graficos=[
            dict(titulo='Inserir no início', ylabel='elementos movidos',
                 series=[dict(col='vetor', rotulo='vetor'), dict(col='lista', rotulo='lista ligada')],
                 teoria=[dict(col='vetor', f='n*(n-1)/2', rotulo='$\\binom n2$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'O vetor move exatamente $n(n-1)/2$ elementos; a lista, zero.'),
            dict(titulo='Percorrer: o cache decide', tabela=1, ylabel='ns por elemento', escala='log',
                 series=[dict(col='lista_ns', rotulo='lista (nós espalhados)'), dict(col='vetor_ns', rotulo='vetor')],
                 leitura=r'Enquanto tudo cabe no cache, a lista custa 1 a 4 ns por nó. Fora do cache (milhões de nós), passa de 100 ns: cada nó é uma ida à RAM.'),
        ],
        conclusao=r'''Inserir no início confirma a teoria: $n(n-1)/2$ movimentos no vetor, nenhum na lista.
No percurso, os dois são $\Theta(n)$, mas a lista espalhada fica até \textbf{200 vezes} mais lenta que o vetor quando sai do cache. \textbf{O modelo RAM não vê a hierarquia de memória}; a medição vê.'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'Filas de processos, listas de arquivos abertos e de páginas livres são listas ligadas dentro do kernel; a inserção $O(1)$ é essencial.'),
        ('\\faMemory', 'Alocação de memória', '\\texttt{malloc} encadeia os blocos livres numa lista; programas em C que vazam memória costumam ``perder'' a cabeça de uma lista.'),
        ('\\faMicrochip', 'Arquitetura de computadores', 'O experimento mostra a hierarquia de memória: L1 ($\\approx$1 ns), L2, L3 e RAM ($\\approx$100 ns). Estruturas \\emph{cache-friendly} vencem na prática.'),
        ('\\faCode', 'Linguagens funcionais', 'Em Lisp, Haskell e Erlang a lista ligada é a estrutura básica: inserir na cabeça cria uma lista nova compartilhando o resto, sem copiar nada.'),
    ],
    exercicios=['(10.2-1) É possível inserir em $O(1)$ numa lista simplesmente ligada? E remover? Em que condições?',
                '(10.2-3) Implemente uma fila com lista simplesmente ligada; \\Nome{Enqueue} e \\Nome{Dequeue} em $O(1)$.',
                '(10.2-7) Inverta uma lista simplesmente ligada em $\\Theta(n)$, sem memória extra.',
                'Ache o elemento do meio de uma lista numa só passada (dois ponteiros, um duas vezes mais rápido).',
                'No experimento, aloque os nós em ordem (sem embaralhar). O que acontece com o tempo da lista? Por quê?'],
    leitura='Cormen et al., seção 10.2.',
)

AULA_15 = dict(
    n=15, bloco=2, tema='Listas duplamente ligadas e listas circulares', curto='Listas duplas e circulares',
    cormen='seção 10.2',
    objetivos=['Implementar a lista duplamente ligada e seus casos especiais sem sentinela',
               'Remover um nó dado em $O(1)$',
               'Fechar a lista num círculo e percorrê-la sem fim',
               'Resolver o problema de Josefo e comparar lista circular com vetor'],
    roteiro=['Ponteiro \\textit{ant}, \\Nome{List-Insert}, \\Nome{List-Delete}, listas circulares',
             'Lista dupla sem sentinela e o problema de Josefo em C',
             'Josefo: $(n-1)(k-1)$ passos na lista contra $\\Theta(n^2)$ no vetor',
             'Sistemas operacionais, navegadores, caches e jogos'],
    teoria=[
        dict(titulo='Lista duplamente ligada', fig='10.3', altura=0.38, empilhar=True,
             legenda='(a) lista $\\langle 9, 16, 4, 1\\rangle$; (b) após \\Nome{List-Insert} de 25; (c) após \\Nome{List-Delete} do 4.',
             texto=r'''Cada nó tem \textit{chave}, \textit{prox} e \textit{ant}. Andar para os dois lados e, principalmente, \textbf{remover um nó dado em $O(1)$}: o anterior está em $x.\mathit{ant}$.'''),
        dict(titulo='Inserir e remover sem sentinela', nome='List-Insert($L, x$) e List-Delete($L, x$)',
             pseudo=r'''\State \Comment{\Nome{List-Insert}: $x$ na cabeça}
\State $x.\mathit{prox} \atrib L.\mathit{cabeça}$
\If{$L.\mathit{cabeça} \ne \textsc{nil}$} \State $L.\mathit{cabeça}.\mathit{ant} \atrib x$ \EndIf
\State $L.\mathit{cabeça} \atrib x$;\quad $x.\mathit{ant} \atrib \textsc{nil}$
\State \Comment{\Nome{List-Delete}}
\If{$x.\mathit{ant} \ne \textsc{nil}$} \State $x.\mathit{ant}.\mathit{prox} \atrib x.\mathit{prox}$
\Else \State $L.\mathit{cabeça} \atrib x.\mathit{prox}$ \EndIf
\If{$x.\mathit{prox} \ne \textsc{nil}$} \State $x.\mathit{prox}.\mathit{ant} \atrib x.\mathit{ant}$ \EndIf''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Ambas $O(1)$.
\item Repare nos \textbf{se}: lista vazia, $x$ na cabeça, $x$ na cauda. Cada um é uma chance de erro.
\item Na aula 16, uma \textbf{sentinela} elimina todos esses testes.
\end{itemize}''', largura_texto=0.36),
        dict(titulo='Listas circulares',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Na lista \textbf{circular}, o \textit{prox} da cauda aponta para a cabeça (e, na dupla, o \textit{ant} da cabeça aponta para a cauda).
\item Não há fim: de qualquer nó se chega a todos. Basta guardar um ponteiro para \textbf{um} nó.
\item Na remoção não há extremos, logo não há casos especiais (desde que reste mais de um nó).
\item Usos: escalonamento \emph{round robin}, \emph{buffers} circulares, jogadores em turnos.
\end{itemize}
\medskip\textbf{Problema de Josefo:} $n$ pessoas em roda; contando a partir da primeira, cada $k$-ésima sai, até restar uma. Quem sobrevive? Com lista circular: $(n-1)(k-1)$ passos e $O(1)$ por remoção.''',
             rodape=r'Para $k = 2$ há fórmula fechada: se $n = 2^m + \ell$ com $\ell < 2^m$, sobrevive $2\ell + 1$ (problema 1.3 de \emph{Matemática Concreta}).'),
    ],
    pratica=dict(
        resumo=['Lista dupla sem sentinela: os casos especiais explícitos', 'A mesma lista fechada em círculo',
                'Problema de Josefo: ordem de saída e sobrevivente'],
        arquivos=[('aula15_dupla_circular.c', 'Lista dupla e circular em C')]),
    experimento=dict(
        programa='aula15_experimento.c', titulo='Josefo: lista circular contra vetor',
        pergunta='Quantos passos a lista circular e quantos deslocamentos o vetor gastam para resolver o problema de Josefo?',
        resumo=['$k = 3$; $n$ de 2.000 a 32.000', 'Lista: $(n-1)(k-1)$ passos', 'Vetor: acha a posição em $O(1)$, mas remover desloca'],
        hipotese=r'''Na lista circular, cada eliminação anda $k - 1$ nós e remove em $O(1)$: exatamente $(n-1)(k-1)$ passos, \textbf{linear}.
No vetor, a posição sai de uma conta (\texttt{(pos + k - 1) \% tam}), mas remover desloca os elementos à direita: $\Theta(n^2)$ no total.''',
        metodo=['Lista circular simples com os nós num vetor de \\texttt{struct}', 'Vetor com remoção por deslocamento',
                'Os dois sobreviventes são conferidos', 'Contagem exata de passos e deslocamentos'],
        graficos=[
            dict(titulo='Passos e deslocamentos', ylabel='operações', escala='logy',
                 series=[dict(col='vetor', rotulo='vetor (deslocamentos)'), dict(col='lista', rotulo='lista circular (passos)')],
                 teoria=[dict(col='vetor', f='n*n', rotulo='$n^2$', tolerancia=0.03),
                         dict(col='lista', f='(n-1)*2', rotulo='$(n-1)(k-1)$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Lista: exatamente $2(n-1)$ passos. Vetor: cerca de $0{,}3\,n^2$ deslocamentos; com 32 mil pessoas, 307 milhões contra 64 mil.'),
        ],
        conclusao=r'''A lista circular resolve Josefo em exatamente $(n-1)(k-1)$ passos; o vetor, em $\approx 0{,}3\,n^2$ deslocamentos: \textbf{4.800 vezes} mais trabalho para $n = 32.000$.
Quando a operação dominante é remover no meio, a lista ligada vence; quando é acessar por posição, o vetor vence.'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'O kernel Linux usa listas duplas circulares (\\texttt{list\\_head}) em toda parte; o escalonador \\emph{round robin} percorre uma lista circular de processos.'),
        ('\\faGlobe', 'Navegadores', 'O histórico com voltar e avançar e as abas em ordem são listas duplas: sair de uma aba no meio é remover um nó em $O(1)$.'),
        ('\\faServer', 'Caches LRU', 'Um cache LRU combina uma tabela hash com uma lista dupla: o item usado vai para a frente, o mais antigo sai do fim, tudo em $O(1)$.'),
        ('\\faGamepad', 'Jogos', 'Turnos de jogadores, animações em laço e trilhas de áudio em repetição são percorridos como listas circulares.'),
    ],
    exercicios=['(10.2-5) Implemente \\Nome{Insert}, \\Nome{Delete} e \\Nome{Search} numa lista circular simplesmente ligada. Custos?',
                '(10.2-6) Una dois conjuntos disjuntos guardados em listas em $O(1)$. Que lista usar?',
                '(10.2-8) Lista dupla com um só campo $x.\\mathit{np} = x.\\mathit{prox}$ XOR $x.\\mathit{ant}$: implemente busca, inserção e remoção.',
                'Resolva Josefo para $k = 2$ e confira a fórmula $2\\ell + 1$ para vários $n$.',
                'Implemente um cache LRU de capacidade fixa com lista dupla (e, na aula 19, com tabela hash).'],
    leitura='Cormen et al., seção 10.2 (listas duplamente ligadas e circulares).',
)

AULA_16 = dict(
    n=16, bloco=2, tema='Sentinelas e listas sem ponteiros', curto='Sentinelas e listas em vetores',
    cormen='seções 10.2 e 10.3',
    objetivos=['Usar uma sentinela para eliminar os casos especiais das listas',
               'Implementar a lista circular duplamente ligada com sentinela do livro',
               'Representar listas com vetores e gerenciar posições livres',
               'Medir quantos testes a sentinela economiza numa busca'],
    roteiro=['A sentinela $L.\\mathit{nil}$, listas em vetores e a lista livre',
             'Lista com sentinela e lista em vetores com \\Nome{Allocate-Object}',
             'Busca com e sem sentinela: $2n + 1$ contra $n + 1$ testes',
             'Kernel Linux, alocadores, sistemas de arquivos e bancos de dados'],
    teoria=[
        dict(titulo='A sentinela', fig='10.4', altura=0.5,
             legenda='lista circular duplamente ligada com sentinela $L.\\mathit{nil}$: (a) vazia; (b) com 4 elementos; (c) após inserir 25; (d) após remover 1.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Um nó falso $L.\mathit{nil}$ fica entre a cabeça e a cauda; $L.\mathit{nil}.\mathit{prox}$ é a cabeça e $L.\mathit{nil}.\mathit{ant}$, a cauda.
\item A lista nunca está ``realmente'' vazia: sempre existe a sentinela.
\item \Nome{List-Delete}$'$ vira só duas linhas:
$x.\mathit{ant}.\mathit{prox} \atrib x.\mathit{prox}$;\; $x.\mathit{prox}.\mathit{ant} \atrib x.\mathit{ant}$.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='Busca com sentinela', nome="List-Search'($L, k$)",
             pseudo=r'''\State $x \atrib L.\mathit{nil}.\mathit{prox}$
\While{$x \ne L.\mathit{nil}$ \textbf{e} $x.\mathit{chave} \ne k$}
\State $x \atrib x.\mathit{prox}$
\EndWhile
\State \Return $x$''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Truque clássico: guarde $k$ \textbf{na sentinela} ($L.\mathit{nil}.\mathit{chave} \atrib k$). O laço sempre para nela, e o teste ``$x \ne L.\mathit{nil}$'' sai de dentro do laço.
\item Metade dos testes por elemento: $n + 1$ em vez de $2n + 1$.
\item Mesma ordem de crescimento, constante menor; e código mais simples.
\item Custo: um nó extra por lista (cuidado com milhares de listas pequenas).
\end{itemize}''', largura_texto=0.48),
        dict(titulo='Listas sem ponteiros: vetores', fig='10.5', altura=0.5,
             legenda='a lista da Figura 10.3(a) em três vetores \\textit{next}, \\textit{key} e \\textit{prev}; o ``ponteiro'' é um índice.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Linguagens sem ponteiros, arquivos em disco e memória compartilhada guardam listas em vetores.
\item Também cabe tudo num vetor só, com deslocamentos por campo (Figura 10.6).
\item \textsc{nil} vira um índice inválido (em C, $-1$).
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Alocando e liberando objetos', fig='10.7', altura=0.58,
             legenda='lista livre: (a) estado inicial; (b) após \\Nome{Allocate-Object} e inserção de 25; (c) após remover 16 e \\Nome{Free-Object}.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item As posições livres formam a \textbf{lista livre}, ligada pelo próprio \textit{next}.
\item Ela é usada como \textbf{pilha}: \Nome{Allocate-Object} tira do topo; \Nome{Free-Object} devolve ao topo. Ambos $O(1)$.
\item É, em miniatura, o que faz \texttt{malloc}/\texttt{free}.
\end{itemize}''', largura_texto=0.40),
    ],
    pratica=dict(
        resumo=['Lista circular dupla com sentinela, como no livro', 'Lista em vetores com lista livre (Figura 10.7)',
                'Os mesmos comandos nas duas: inserir, buscar, remover, imprimir'],
        arquivos=[('aula16_lista_sentinela.c', 'Lista com sentinela em C'), ('aula16_lista_vetor.c', 'Lista em vetores com lista livre')]),
    experimento=dict(
        programa='aula16_experimento.c', titulo='Quanto a sentinela economiza',
        pergunta='Quantos testes uma busca sem sucesso faz com e sem sentinela? E quanto tempo?',
        resumo=['Sem sentinela: testa o fim e a chave em cada passo', 'Com sentinela: só a chave', 'Busca sem sucesso em $n$ de $2^{10}$ a $2^{20}$'],
        hipotese=r'''Numa busca sem sucesso, sem sentinela, cada um dos $n$ elementos custa dois testes, mais o teste final do limite: $2n + 1$.
Com a chave guardada na sentinela, um teste por elemento mais o da própria sentinela: $n + 1$. O tempo deve cair, mas menos que pela metade: um dos testes é barato.''',
        metodo=['Vetor com $n$ pares; busca pelo valor 1 (ausente)', 'Contador em cada teste do laço',
                'Tempo por elemento visitado, muitas repetições', '$n = 2^{10}, \\dots, 2^{20}$'],
        graficos=[
            dict(titulo='Testes por busca sem sucesso', ylabel='testes', escala='log',
                 series=[dict(col='sem_sentinela', rotulo='sem sentinela'), dict(col='com_sentinela', rotulo='com sentinela')],
                 teoria=[dict(col='sem_sentinela', f='2*n + 1', rotulo='$2n + 1$', ajustar=False, tolerancia=0.0001),
                         dict(col='com_sentinela', f='n + 1', rotulo='$n + 1$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Exatamente metade dos testes. A ordem de crescimento é a mesma: só a constante muda.'),
            dict(titulo='E no relógio?', ylabel='ns por elemento', escala='logx', opcoes='ymin=0',
                 series=[dict(col='sem_ns', rotulo='sem sentinela'), dict(col='com_ns', rotulo='com sentinela')],
                 leitura=r'Cerca de 10\% mais rápido: o processador prevê o teste do limite quase de graça. A maior vantagem da sentinela é o código sem casos especiais.'),
        ],
        conclusao=r'''A sentinela corta os testes exatamente pela metade ($n + 1$ contra $2n + 1$) e economiza cerca de 10\% do tempo. Mais importante: elimina os casos especiais de lista vazia, cabeça e cauda, que são a fonte da maioria dos erros com listas.
Na representação em vetores, a lista livre faz o papel do \texttt{malloc}: alocar e liberar em $O(1)$.'''),
    conexoes=[
        ('\\faLinux', 'Kernel Linux', 'Toda lista do kernel (\\texttt{list\\_head}) é circular, dupla e com sentinela: a ``cabeça'' é um nó sem dados, exatamente $L.\\mathit{nil}$.'),
        ('\\faMemory', 'Alocadores de memória', '\\texttt{malloc} mantém listas livres de blocos por tamanho; alocadores de \\emph{pool} (jogos, servidores) usam a pilha livre da Figura 10.7.'),
        ('\\faHdd', 'Sistemas de arquivos', 'O FAT do MS-DOS e de pendrives é uma lista em vetor: cada posição diz o próximo bloco do arquivo; os blocos livres formam outra lista.'),
        ('\\faDatabase', 'Bancos de dados', 'Páginas livres de um arquivo de banco são encadeadas numa lista livre guardada no próprio arquivo, com índices no lugar de ponteiros.'),
    ],
    exercicios=['(10.2-4) Como está escrito, cada volta de \\Nome{List-Search}$\'$ faz dois testes. Elimine o teste $x \\ne L.\\mathit{nil}$.',
                '(10.3-2) Escreva \\Nome{Allocate-Object} e \\Nome{Free-Object} para a representação em um único vetor.',
                '(10.3-4) Mantenha os objetos de uma lista dupla compactos nas primeiras $m$ posições. Como remover em $O(1)$?',
                'Reescreva \\texttt{aula15\\_dupla\\_circular.c} com sentinela e compare o número de linhas e de \\texttt{if}.',
                'Use \\texttt{aula16\\_lista\\_vetor.c} com $M = 8$ e insira 9 elementos. O que acontece? Como fazer o vetor crescer?'],
    leitura='Cormen et al., seções 10.2 (sentinelas) e 10.3.',
)

AULA_17 = dict(
    n=17, bloco=2, tema='Filas de prioridade', curto='Filas de prioridade',
    cormen='seção 6.5',
    objetivos=['Definir as operações de uma fila de prioridade',
               'Implementar inserção, extração do máximo e aumento de chave num heap',
               'Comparar heap, vetor ordenado e vetor desordenado como filas de prioridade',
               'Medir $\\Theta(n\\lg n)$ contra $\\Theta(n^2)$ em $n$ inserções e $n$ extrações'],
    roteiro=['O tipo abstrato, as quatro operações e seus custos no heap',
             'Fila de prioridade em C com comandos da entrada',
             'Heap contra vetores: $n\\lg n$ contra $n^2$',
             'Sistemas operacionais, redes, simulação e algoritmos de grafos'],
    teoria=[
        dict(titulo='O que é uma fila de prioridade',
             texto=r'''Mantém um conjunto $S$ de elementos, cada um com uma \textbf{chave}. Fila de máximo:
\begin{itemize}\setlength{\itemsep}{4pt}
\item \Nome{Insert}($S, x$): insere $x$.
\item \Nome{Maximum}($S$): devolve o elemento de maior chave.
\item \Nome{Extract-Max}($S$): remove e devolve o de maior chave.
\item \Nome{Increase-Key}($S, x, k$): aumenta a chave de $x$ para $k$.
\end{itemize}
A fila de mínimo é simétrica (\Nome{Extract-Min}, \Nome{Decrease-Key}).

\medskip\begin{tabular}{lccc}\toprule & \textbf{Insert} & \textbf{Extract-Max} & \textbf{Increase-Key}\\\midrule
vetor desordenado & $O(1)$ & $\Theta(n)$ & $O(1)$\\
vetor ordenado & $\Theta(n)$ & $O(1)$ & $\Theta(n)$\\
\textbf{heap} & $O(\lg n)$ & $O(\lg n)$ & $O(\lg n)$\\\bottomrule\end{tabular}'''),
        dict(titulo='Extrair o máximo', nome='Heap-Extract-Max($A$)',
             pseudo=r'''\If{$A.\mathit{tamanho} < 1$} \State \textbf{erro} ``heap vazio'' \EndIf
\State $\mathit{max} \atrib A[1]$
\State $A[1] \atrib A[A.\mathit{tamanho}]$
\State $A.\mathit{tamanho} \atrib A.\mathit{tamanho} - 1$
\State \Nome{Max-Heapify}($A, 1$)
\State \Return $\mathit{max}$''',
             texto=r'''O último elemento ocupa o lugar da raiz e \textbf{desce}. Custo: $O(\lg n)$, a altura do heap.''', largura_texto=0.38),
        dict(titulo='Aumentar uma chave e inserir', nome='Heap-Increase-Key($A, i, \\mathit{chave}$)',
             pseudo=r'''\If{$\mathit{chave} < A[i]$} \State \textbf{erro} ``nova chave é menor'' \EndIf
\State $A[i] \atrib \mathit{chave}$
\While{$i > 1$ \textbf{e} $A[\text{pai}(i)] < A[i]$}
\State troque $A[i]$ com $A[\text{pai}(i)]$
\State $i \atrib \text{pai}(i)$
\EndWhile''',
             texto=r'''A chave aumentada \textbf{sobe} trocando com o pai.

\medskip \Nome{Max-Heap-Insert}($A$, \textit{chave}): aumenta o tamanho, coloca $-\infty$ na nova folha e chama \Nome{Heap-Increase-Key}. Ambas $O(\lg n)$.''', largura_texto=0.38),
        dict(titulo='Aumento de chave passo a passo', fig='6.5', altura=0.62,
             legenda='\\Nome{Heap-Increase-Key} muda o 4 para 15, que sobe até abaixo da raiz.'),
    ],
    pratica=dict(
        resumo=['Heap com vetor que dobra de tamanho (\\texttt{realloc})', '\\texttt{sobe} e \\texttt{desce}: as duas metades do heap',
                'Comandos: \\texttt{i x}, \\texttt{m}, \\texttt{x}, \\texttt{a k v}'],
        arquivos=[('aula17_fila_prioridade.c', 'Fila de prioridade em C')]),
    experimento=dict(
        programa='aula17_experimento.c', titulo='Três implementações, mesmo trabalho',
        pergunta='Para n inserções seguidas de n extrações, quantas comparações fazem heap, vetor ordenado e vetor desordenado?',
        resumo=['Mesma sequência de operações nas três filas', 'Hipótese: $\\Theta(n\\lg n)$, $\\approx n^2/4$ e $n(n-1)/2$',
                '$n$ de 1.000 a 16.000'],
        hipotese=r'''Cada operação no heap custa $O(\lg n)$: total $\Theta(n\lg n)$.
No vetor ordenado, cada inserção desloca em média metade dos elementos: $\approx n^2/4$.
No desordenado, extrair o máximo examina todos: exatamente $n(n-1)/2$ comparações.''',
        metodo=['Os mesmos $n$ números aleatórios nas três filas', 'Contador de comparações entre chaves',
                '$n$ inserções, depois $n$ extrações', '$n$ de 1.000 a 16.000'],
        graficos=[
            dict(titulo='Comparações das três filas', ylabel='comparações',
                 series=[dict(col='desordenado', rotulo='vetor desordenado'), dict(col='ordenado', rotulo='vetor ordenado'),
                         dict(col='heap', rotulo='heap')],
                 teoria=[dict(col='desordenado', f='n*(n-1)/2', rotulo='$\\binom n2$', ajustar=False, tolerancia=0.0001),
                         dict(col='ordenado', f='n*n/4', rotulo='$n^2/4$', ajustar=False, tolerancia=0.03),
                         dict(col='heap', f='n*log2(n)', rotulo='$n\\lg n$', tolerancia=0.05)],
                 leitura=r'O heap quase some no gráfico: para $n = 16.000$, faz 404 mil comparações contra 64 e 128 milhões.'),
        ],
        conclusao=r'''O vetor desordenado faz exatamente $n(n-1)/2$ comparações e o ordenado, $n^2/4$; o heap fica em $\approx 1{,}8\,n\lg n$.
Para $n = 16.000$, o heap é \textbf{150 vezes} mais barato que o vetor ordenado. A estrutura certa muda a ordem de crescimento.'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'Escalonadores escolhem o próximo processo pela prioridade; temporizadores do kernel disparam o evento mais próximo: \\Nome{Extract-Min} num heap.'),
        ('\\faNetworkWired', 'Redes de computadores', 'Roteadores com QoS servem primeiro os pacotes de voz e vídeo; o roteamento OSPF roda Dijkstra com fila de prioridade em cada roteador.'),
        ('\\faClock', 'Simulação de eventos', 'Simuladores (filas de banco, tráfego, epidemias) processam eventos em ordem de tempo: o próximo evento sai de uma fila de mínimo.'),
        ('\\faCompress', 'Compressão de dados', 'O código de Huffman (aula 34) junta repetidamente os dois símbolos menos frequentes, retirados de uma fila de prioridade.'),
    ],
    exercicios=['(6.5-1) Ilustre \\Nome{Heap-Extract-Max} em $A = \\langle 15,13,9,5,12,8,7,4,0,6,2,1\\rangle$.',
                '(6.5-2) Ilustre \\Nome{Max-Heap-Insert}($A$, 10) no mesmo heap.',
                '(6.5-8) Implemente \\Nome{Heap-Delete}($A, i$) em $O(\\lg n)$.',
                '(6.5-9) Intercale $k$ listas ordenadas em $O(n\\lg k)$ com uma fila de mínimo.',
                'Altere a fila para guardar pares (prioridade, nome de tarefa) e simule um escalonador.'],
    leitura='Cormen et al., seção 6.5.',
)

PROJETO_2 = dict(
    n=18, bloco=2, tipo='projeto', tema='Projeto 2: simulador de escalonamento de processos',
    descricao='Apresentação dos projetos do Bloco 2. Cada equipe constrói um simulador de escalonamento de CPU com as estruturas do bloco e compara políticas com experimentos.',
    entregas=['Simulador em C: processos chegam com tempo de execução e prioridade; fila circular (FIFO e round robin), lista duplamente ligada com sentinela (processos bloqueados), pilha (chamadas de cada processo) e fila de prioridade em heap (menor trabalho primeiro)',
              'Três políticas: FIFO, menor trabalho primeiro (heap) e \\emph{round robin} (fila circular)',
              'Experimento: tempo médio de espera e vazão para 1.000 a 1.000.000 de processos, com o custo das operações confrontado com a teoria',
              'Relatório: qual política vence em cada carga e quanto custa cada estrutura (gráficos com curvas teóricas)',
              'Apresentação de 10 minutos com demonstração ao vivo'],
)

AULAS_B2 = [AULA_10, AULA_11, AULA_12, AULA_13, AULA_14, AULA_15, AULA_16, AULA_17, PROJETO_2]
