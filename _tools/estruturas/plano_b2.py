"""Bloco 2 – Ordenação avançada e estruturas lineares (aulas 10 a 18)."""

AULA_10 = dict(
    n=10, bloco=2, tema='Filas de prioridade', curto='Filas de prioridade',
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
        arquivos=[('aula10_fila_prioridade.c', 'Fila de prioridade em C')]),
    experimento=dict(
        programa='aula10_experimento.c', titulo='Três implementações, mesmo trabalho',
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

AULA_11 = dict(
    n=11, bloco=2, tema='Quicksort', curto='Quicksort',
    cormen='seções 7.1 e 7.2',
    objetivos=['Executar \\Nome{Partition} e provar sua corretude pelo invariante das quatro regiões',
               'Analisar o pior caso ($\\Theta(n^2)$) e o melhor caso ($\\Theta(n\\lg n)$)',
               'Entender por que partições desbalanceadas em proporção constante ainda dão $n\\lg n$',
               'Medir $\\approx 2n\\ln n$ comparações em entradas aleatórias e $n^2/2$ em entradas ordenadas'],
    roteiro=['Partição de Lomuto, invariante, desempenho do quicksort',
             'Quicksort em C',
             'Aleatório contra ordenado: $1{,}39\\,n\\lg n$ contra $n^2/2$',
             'Bibliotecas padrão, bancos de dados, segurança e paralelismo'],
    teoria=[
        dict(titulo='Dividir e conquistar, de outro jeito',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \textbf{Dividir:} reorganiza $A[p..r]$ em $A[p..q-1] \le A[q] < A[q+1..r]$. O trabalho está aqui.
\item \textbf{Conquistar:} ordena as duas partes recursivamente.
\item \textbf{Combinar:} nada a fazer: o vetor já está ordenado.
\end{itemize}
\medskip Ao contrário do merge sort (divisão trivial, combinação cara), o quicksort tem divisão cara e combinação trivial. É \textbf{no lugar} e, na prática, o mais rápido em média.''',
             rodape=r'Inventado por C. A. R. Hoare em 1959, ao traduzir dicionários de russo; está nas bibliotecas de C, C++, Java e Go.'),
        dict(titulo='A partição', nome='Partition($A, p, r$)',
             pseudo=r'''\State $x \atrib A[r]$ \Comment{pivô}
\State $i \atrib p - 1$
\For{$j \atrib p$ \textbf{até} $r - 1$}
\If{$A[j] \le x$}
\State $i \atrib i + 1$
\State troque $A[i]$ com $A[j]$
\EndIf
\EndFor
\State troque $A[i+1]$ com $A[r]$
\State \Return $i + 1$''',
             fig='7.2', legenda='as quatro regiões: $\\le x$, $> x$, ainda não vista e o pivô.',
             texto=r'''\textbf{Invariante} (início de cada volta):
\begin{enumerate}\item $A[p..i] \le x$\item $A[i+1..j-1] > x$\item $A[r] = x$\end{enumerate}
Custo: $\Theta(n)$, exatamente $n - 1$ comparações.''', largura_texto=0.34),
        dict(titulo='Partição passo a passo', fig='7.1', altura=0.66,
             legenda='\\Nome{Partition} em $\\langle 2,8,7,1,3,5,6,4\\rangle$ com pivô 4: cinza claro $\\le x$, cinza escuro $> x$.'),
        dict(titulo='Pior caso, melhor caso',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.48\textwidth}
\begin{cartao}{cconexoes}\textbf{Pior caso}\par\footnotesize Partição com 0 e $n-1$ elementos (vetor já ordenado!):
\[T(n) = T(n-1) + \Theta(n) = \Theta(n^2)\]\end{cartao}
\end{column}\begin{column}{0.48\textwidth}
\begin{cartao}{cok}\textbf{Melhor caso}\par\footnotesize Partição ao meio:
\[T(n) = 2T(n/2) + \Theta(n) = \Theta(n\lg n)\]\end{cartao}
\end{column}\end{columns}''',
             fig='7.4', altura=0.36, empilhar=True,
             legenda='mesmo a divisão 9 para 1 dá profundidade $\\log_{10/9} n$ e custo $O(n\\lg n)$.'),
    ],
    pratica=dict(
        resumo=['Partição de Lomuto, como no livro', 'Recursão nas duas partes; nada a combinar',
                'Teste com o vetor da Figura 7.1'],
        notas=[dict(titulo='Cuidados práticos',
                    texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \textbf{Pilha de recursão.} No pior caso, a recursão tem profundidade $n$: estoura a pilha para $n$ grande. Solução: recursão só no lado \textbf{menor} e laço no maior, garantindo profundidade $O(\lg n)$ (problema 7-4). O experimento faz isso.
\item \textbf{Chaves repetidas.} Com muitos iguais, Lomuto degenera; a partição de Hoare (problema 7-1) ou a de três vias resolve.
\item \textbf{Subvetores pequenos.} Bibliotecas trocam para a inserção abaixo de $\approx 16$ elementos (exercício 7.4-5).
\end{itemize}''')],
        arquivos=[('aula11_quicksort.c', 'Quicksort em C')]),
    experimento=dict(
        programa='aula11_experimento.c', titulo='Caso médio e pior caso, medidos',
        pergunta='Quantas comparações o quicksort faz em vetores aleatórios e em vetores já ordenados?',
        resumo=['Aleatório: $2(n+1)H_n - 4n \\approx 1{,}39\\,n\\lg n$', 'Ordenado: exatamente $n(n-1)/2$',
                '$n$ até $2^{20}$ no caso aleatório'],
        hipotese=r'''Em vetores aleatórios, o número esperado de comparações é
\[2(n+1)H_n - 4n \approx 2n\ln n \approx 1{,}39\,n\lg n.\]
Num vetor já ordenado, o pivô $A[r]$ é sempre o máximo: partições $n-1$ e 0, e exatamente $n(n-1)/2$ comparações.''',
        metodo=['Contador na comparação $A[j] \\le x$', 'Aleatório: $n = 2^{12}$ a $2^{20}$, média de 5 vetores',
                'Ordenado: $n$ de 1.000 a 12.000', 'Recursão no lado menor (pilha $O(\\lg n)$)'],
        graficos=[
            dict(titulo='Vetores aleatórios', ylabel='comparações', escala='log',
                 series=[dict(col='aleatorio', rotulo='medido')],
                 teoria=[dict(col='aleatorio', f='2*(n+1)*(log(n) + 0.5772156649) - 4*n', rotulo='$2(n+1)H_n - 4n$', ajustar=False, tolerancia=0.03)],
                 leitura=r'$H_n \approx \ln n + 0{,}5772$ (constante de Euler). O medido fica a cerca de 1\% da previsão.'),
            dict(titulo='Vetor já ordenado: o pior caso', tabela=1, ylabel='comparações',
                 series=[dict(col='ordenado', rotulo='medido')],
                 teoria=[dict(col='ordenado', f='n*(n-1)/2', rotulo='$n(n-1)/2$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Exatamente $n(n-1)/2$: com 12.000 elementos já ordenados, 72 milhões de comparações. Aleatório com $2^{20}$: 26 milhões.'),
        ],
        conclusao=r'''A previsão de caso médio, $2(n+1)H_n - 4n \approx 1{,}39\,n\lg n$, se confirma com desvio de cerca de 1\%.
E o pior caso é exatamente $n(n-1)/2$, justamente na entrada mais ``fácil'', o vetor ordenado. A próxima aula elimina esse risco com aleatoriedade.'''),
    conexoes=[
        ('\\faCode', 'Bibliotecas padrão', '\\texttt{qsort} (C), \\texttt{std::sort} (introsort em C++), \\texttt{Arrays.sort} para primitivos (quicksort de dois pivôs no Java) e \\texttt{sort} do Go (pdqsort).'),
        ('\\faDatabase', 'Bancos de dados', 'Ordenar resultados em memória (\\texttt{ORDER BY}) e preparar \\emph{joins} usa quicksort ou variações; a partição também aparece na seleção do $k$-ésimo (\\texttt{LIMIT}).'),
        ('\\faUserSecret', 'Segurança', 'Um adversário que conhece o pivô pode montar entradas $\\Theta(n^2)$ (``McIlroy killer''): por isso as bibliotecas aleatorizam ou usam introsort.'),
        ('\\faMicrochip', 'Computação paralela', 'Depois de particionar, as duas partes são independentes; GPUs ordenam com variações paralelas da partição.'),
    ],
    exercicios=['(7.1-1) Ilustre \\Nome{Partition} em $A = \\langle 13,19,9,5,12,8,7,4,21,2,6,11\\rangle$.',
                '(7.1-2) Que valor $q$ \\Nome{Partition} devolve quando todos são iguais? Modifique-a para devolver o meio.',
                '(7.2-3) Mostre que o quicksort é $\\Theta(n^2)$ quando $A$ está em ordem decrescente.',
                '(Problema 7-1) Implemente a partição de Hoare e compare o número de trocas com o de Lomuto.',
                'Meça o experimento com 90\\% de chaves repetidas. O que acontece com Lomuto?'],
    leitura='Cormen et al., seções 7.1 e 7.2; problema 7-1.',
)

AULA_12 = dict(
    n=12, bloco=2, tema='Quicksort aleatorizado e a análise do caso médio', curto='Quicksort aleatorizado',
    cormen='seções 7.3 e 7.4',
    objetivos=['Aleatorizar a escolha do pivô e entender o que isso garante',
               'Calcular o número esperado de comparações com variáveis indicadoras',
               'Distinguir caso médio (sobre entradas) de tempo esperado (sobre sorteios)',
               'Medir a concentração das comparações em torno da esperança'],
    roteiro=['Pivô sorteado, análise por pares comparados, $E[X] = O(n\\lg n)$',
             'Quicksort aleatorizado em C',
             'Entrada ordenada: pivô fixo contra pivô sorteado; histograma',
             'Algoritmos aleatorizados em redes, segurança, IA e sistemas distribuídos'],
    teoria=[
        dict(titulo='Aleatoriedade contra o adversário', nome='Randomized-Partition($A, p, r$)',
             pseudo=r'''\State $i \atrib$ \Nome{Random}($p, r$)
\State troque $A[r]$ com $A[i]$
\State \Return \Nome{Partition}($A, p, r$)''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Nenhuma entrada específica provoca o pior caso: ele depende só do \textbf{sorteio}.
\item O \textbf{tempo esperado} vale para \textbf{toda} entrada, inclusive a ordenada.
\item Caso médio (aula 11) supunha entradas aleatórias; aqui a aleatoriedade está no algoritmo.
\end{itemize}''', largura_texto=0.50),
        dict(titulo='Quem é comparado com quem?',
             texto=r'''Renomeie os elementos em ordem: $z_1 < z_2 < \dots < z_n$, e seja $Z_{ij} = \{z_i, \dots, z_j\}$.
\begin{itemize}\setlength{\itemsep}{5pt}
\item Dois elementos são comparados \textbf{no máximo uma vez}: só com o pivô, que depois sai do jogo.
\item $z_i$ e $z_j$ são comparados \textbf{se e somente se} o primeiro pivô escolhido em $Z_{ij}$ é $z_i$ ou $z_j$. Se for um elemento do meio, eles vão para lados diferentes e nunca se encontram.
\item Todos os $j - i + 1$ elementos de $Z_{ij}$ têm a mesma chance de ser o primeiro pivô:
\[\Pr\{z_i \text{ comparado com } z_j\} = \frac{2}{j - i + 1}\]
\end{itemize}'''),
        dict(titulo='Somando as probabilidades',
             texto=r'''Com $X_{ij}$ indicadora de ``$z_i$ é comparado com $z_j$'' e $X = \sum X_{ij}$:
\[E[X] = \sum_{i=1}^{n-1}\sum_{j=i+1}^{n} \frac{2}{j-i+1} = \sum_{i=1}^{n-1}\sum_{k=1}^{n-i}\frac{2}{k+1} < \sum_{i=1}^{n-1}\sum_{k=1}^{n} \frac{2}{k} = \sum_{i=1}^{n-1} O(\lg n) = O(n\lg n)\]
Fazendo a conta exata: $E[X] = 2(n+1)H_n - 4n \approx 1{,}39\,n\lg n$.''',
             rodape=r'Linearidade da esperança: a esperança da soma é a soma das esperanças, mesmo que os $X_{ij}$ sejam dependentes.'),
        dict(titulo='Partições boas são a regra', fig='7.5', altura=0.36, empilhar=True,
             legenda='(a) uma partição ruim seguida de uma boa custa o mesmo que (b) uma boa: o custo da ruim é absorvido.',
             texto=r'''Com pivô aleatório, a chance de a partição ser pior que 1 para 9 é só 20\%. Partições ruins ocasionais são absorvidas pelas boas: a recursão continua com profundidade $O(\lg n)$.'''),
    ],
    pratica=dict(
        resumo=['\\texttt{rand()} sorteia o pivô em $[p, r]$', '\\texttt{srand(time(NULL))}: sorteios diferentes a cada execução',
                'Entrada já ordenada deixa de ser problema'],
        arquivos=[('aula12_quicksort_aleatorio.c', 'Quicksort aleatorizado em C')]),
    experimento=dict(
        programa='aula12_experimento.c', titulo='O pior caso desaparece',
        pergunta='Com entrada já ordenada, o pivô sorteado faz o quicksort voltar a 2(n+1)H_n − 4n comparações?',
        resumo=['Entrada ordenada: pivô fixo contra sorteado', 'Pivô sorteado: média de 20 execuções por $n$',
                'Histograma de 20.000 execuções com $n = 1000$'],
        hipotese=r'''Na entrada já ordenada, o pivô fixo ($A[r]$) faz $n(n-1)/2$ comparações.
Com pivô sorteado, a esperança é $2(n+1)H_n - 4n$ para \textbf{qualquer} entrada, inclusive esta. E as execuções devem se concentrar perto da esperança.''',
        metodo=['Mesmo vetor ordenado $0, 1, \\dots, n-1$', '$n$ de 1.000 a 16.000',
                'Histograma: 20.000 execuções, $n = 1000$, classes de 250', 'Semente fixa (\\texttt{srand(12)}): reproduzível'],
        graficos=[
            dict(titulo='Pivô fixo contra pivô sorteado (entrada ordenada)', ylabel='comparações', escala='logy',
                 series=[dict(col='fixo', rotulo='pivô fixo'), dict(col='aleatorizado', rotulo='pivô sorteado')],
                 teoria=[dict(col='aleatorizado', f='2*(n+1)*(log(n) + 0.5772156649) - 4*n', rotulo='$2(n+1)H_n-4n$', ajustar=False, tolerancia=0.03),
                         dict(col='fixo', f='n*(n-1)/2', rotulo='$n(n-1)/2$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Eixo $y$ logarítmico: para $n = 16.000$, o pivô sorteado faz cerca de 500 vezes menos comparações.'),
            dict(titulo='Como as execuções se distribuem ($n = 1000$)', tabela=1, x='comparacoes', xlabel='comparações',
                 ylabel='execuções', opcoes='ybar,bar width=4pt,ymin=0',
                 series=[dict(col='frequencia', rotulo='20.000 execuções', estilo='ybar,fill=cexperimento!60,draw=cexperimento,mark=none')],
                 leitura=r'Média perto de $2\cdot1001\cdot H_{1000} - 4000 \approx 10.986$. Nenhuma das 20.000 execuções chegou perto do pior caso, $499.500$.'),
        ],
        conclusao=r'''Na entrada que destrói o pivô fixo ($n(n-1)/2$ comparações), o pivô sorteado volta à esperança $2(n+1)H_n - 4n$.
O histograma mostra execuções concentradas: a probabilidade de algo perto do pior caso é desprezível. \textbf{Aleatoriedade troca uma entrada ruim por uma sorte ruim, e sorte ruim é rara.}'''),
    conexoes=[
        ('\\faShieldAlt', 'Segurança', 'Tabelas hash de linguagens (Python, Rust) sorteiam a semente da função hash a cada execução pelo mesmo motivo: impedir que um atacante escolha a entrada do pior caso.'),
        ('\\faNetworkWired', 'Redes', 'O Ethernet usa recuo exponencial aleatório após colisões; balanceadores de carga usam ``a melhor de duas escolhas aleatórias'' para distribuir requisições.'),
        ('\\faBrain', 'Aprendizado de máquina', 'Gradiente estocástico, \\emph{random forests} e \\emph{dropout}: a aleatoriedade torna algoritmos mais rápidos e mais robustos, com garantias em esperança.'),
        ('\\faServer', 'Sistemas distribuídos', 'Protocolos de fofoca (\\emph{gossip}) e eleição de líder no Raft usam tempos aleatórios para evitar empates e espalhar informação em $O(\\lg n)$ rodadas.'),
    ],
    exercicios=['(7.3-1) Por que analisamos o tempo \\emph{esperado} e não o de pior caso do quicksort aleatorizado?',
                '(7.3-2) Quantas chamadas a \\Nome{Random} ocorrem no pior e no melhor caso?',
                '(7.4-2) Mostre que o melhor caso do quicksort é $\\Omega(n\\lg n)$.',
                '(Problema 7-5) Implemente a partição pela mediana de 3 e meça a diferença.',
                'No experimento, troque a semente e verifique que a média muda menos de 1\\%.'],
    leitura='Cormen et al., seções 7.3 e 7.4; apêndice C.3 (variáveis indicadoras).',
)

AULA_13 = dict(
    n=13, bloco=2, tema='O limite inferior da ordenação por comparação', curto='Limite inferior',
    cormen='seção 8.1',
    objetivos=['Modelar algoritmos de ordenação por comparação como árvores de decisão',
               'Provar que todo algoritmo desse tipo faz $\\Omega(n\\lg n)$ comparações no pior caso',
               'Usar a aproximação de Stirling para $\\lg(n!)$',
               'Medir quão perto do limite o merge sort chega'],
    roteiro=['Árvore de decisão, altura e folhas, o teorema 8.1',
             'Pior caso exato do merge sort em todas as $n!$ permutações',
             'Merge sort contra $\\lceil\\lg n!\\rceil$ e contra $\\lg n!$ para $n$ grande',
             'Teoria da informação, compressão, criptografia e computação quântica'],
    teoria=[
        dict(titulo='Árvores de decisão', fig='8.1', altura=0.55,
             legenda='árvore de decisão da inserção para $n = 3$: $3! = 6$ folhas.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Um algoritmo de \textbf{comparação} só aprende sobre a ordem comparando pares $a_i \le a_j$.
\item Cada nó interno é uma comparação; cada folha é uma permutação de saída.
\item Uma execução é um caminho da raiz a uma folha: o número de comparações é o comprimento do caminho.
\item O \textbf{pior caso} é a \textbf{altura} da árvore.
\end{itemize}''', largura_texto=0.44),
        dict(titulo='Teorema 8.1: $\\Omega(n\\lg n)$',
             texto=r'''Todo algoritmo de ordenação por comparação faz $\Omega(n\lg n)$ comparações no pior caso.

\medskip\textbf{Prova.} Uma árvore correta precisa de pelo menos $n!$ folhas, uma por permutação. Uma árvore binária de altura $h$ tem no máximo $2^h$ folhas. Logo
\[n! \le \ell \le 2^h \quad\Longrightarrow\quad h \ge \lg(n!) = \Omega(n\lg n),\]
pois, por Stirling, $\lg(n!) = n\lg n - n\lg e + O(\lg n) \approx n\lg n - 1{,}44\,n$.''',
             rodape=r'\textbf{Corolário 8.2:} heapsort e merge sort são \textbf{assintoticamente ótimos} entre os algoritmos de comparação.'),
        dict(titulo='O que o limite não diz',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item Vale para \textbf{comparações}. Se as chaves são inteiros pequenos, contagem e radix sort ordenam em $O(n)$ (aula 14).
\item É um limite de \textbf{pior caso}, mas também vale para o caso médio: a profundidade média das folhas de uma árvore binária com $n!$ folhas é pelo menos $\lg(n!)$ (problema 8-1).
\item Não diz qual algoritmo é mais rápido na prática: constantes, memória e cache decidem entre heapsort, merge sort e quicksort.
\item \textbf{Informação:} cada comparação dá no máximo 1 bit; identificar uma de $n!$ permutações exige $\lg(n!)$ bits.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Gera as $n!$ permutações (algoritmo de Heap)', 'Guarda o maior número de comparações do merge sort',
                'Compara com $\\lceil\\lg n!\\rceil$, calculado com \\texttt{lgamma}'],
        arquivos=[('aula13_arvore_decisao.c', 'A altura da árvore do merge sort')]),
    experimento=dict(
        programa='aula13_experimento.c', titulo='O merge sort perto do limite',
        pergunta='O pior caso do merge sort fica acima de ⌈lg n!⌉? Quão perto do limite ele chega em média?',
        resumo=['Pior caso exato: todas as $n!$ permutações, $n = 2..10$', 'Média para $n$ até $2^{20}$ contra $\\lg n!$',
                'Nenhum algoritmo pode ficar abaixo do limite'],
        hipotese=r'''Para todo $n$, o pior caso do merge sort é $\ge \lceil\lg n!\rceil$ (teorema 8.1).
Para $n$ grande, o merge sort faz em média $n\lg n - 1{,}26\,n$, e $\lg n! \approx n\lg n - 1{,}44\,n$: a diferença deve ser de apenas $\approx 0{,}18\,n$, menos de 1\% para $n = 2^{20}$.''',
        metodo=['$n = 2..10$: todas as permutações (até 3.628.800)', '$n = 2^{10}..2^{20}$: média de 3 vetores aleatórios',
                '$\\lg n! = \\ln\\Gamma(n+1)/\\ln 2$ via \\texttt{lgamma}', 'Verificação: medido $\\ge$ limite em todos os $n$'],
        graficos=[
            dict(titulo='Pior caso exato contra o limite', ylabel='comparações', xlabel='$n$',
                 series=[dict(col='pior_merge', rotulo='merge sort (pior caso)'), dict(col='limite', rotulo='$\\lceil\\lg n!\\rceil$')],
                 teoria=[dict(col='pior_merge', f='ceil(lgamma(n+1)/log(2) - 1e-9)', rotulo='$\\lceil\\lg n!\\rceil$', limite='inferior')],
                 leitura=r'Até $n = 4$, o merge sort é ótimo. Para $n = 10$, faz 25 comparações no pior caso; o limite é 22.'),
            dict(titulo='Média do merge sort contra $\\lg n!$', tabela=1, ylabel='comparações', escala='log',
                 series=[dict(col='media_merge', rotulo='merge sort (média)')],
                 teoria=[dict(col='media_merge', f='lgamma(n+1)/log(2)', rotulo='$\\lg n!$', ajustar=False, tolerancia=0.02)],
                 leitura=r'A razão medido$/\lg n!$ cai para 1,01: o merge sort está a 1\% do ótimo teórico.'),
        ],
        conclusao=r'''Em todos os $n$ testados, o pior caso do merge sort ficou \textbf{acima} de $\lceil\lg n!\rceil$, como o teorema exige, e para $n \le 4$ ele atinge o limite.
Para $n = 2^{20}$, o merge sort faz só 1\% mais comparações que $\lg n!$. Não há como fazer muito melhor \textbf{comparando}; para ir além, é preciso usar a estrutura das chaves.'''),
    conexoes=[
        ('\\faInfo', 'Teoria da informação', 'O argumento é de Shannon: uma comparação gera no máximo 1 bit. O mesmo raciocínio dá limites para busca ($\\lg n$) e para jogos como ``vinte perguntas''.'),
        ('\\faFileArchive', 'Compressão', 'Nenhum compressor sem perdas reduz todos os arquivos: há $2^n$ arquivos de $n$ bits e menos códigos menores. É o argumento de contagem das folhas.'),
        ('\\faKey', 'Criptografia', 'Uma chave de 128 bits tem $2^{128}$ possibilidades: um ataque de força bruta precisa de $\\Omega(2^{127})$ tentativas em média. Limites inferiores são a base da segurança.'),
        ('\\faAtom', 'Computação quântica', 'O algoritmo de Grover busca em $O(\\sqrt n)$, e há prova de que nenhum algoritmo quântico faz melhor: limites inferiores também valem no modelo quântico.'),
    ],
    exercicios=['(8.1-1) Qual a menor profundidade possível de uma folha numa árvore de decisão de ordenação?',
                '(8.1-3) Mostre que não existe ordenação por comparação linear para metade das $n!$ entradas.',
                '(8.1-4) Limite inferior para ordenar $n/k$ subsequências de $k$ elementos cada.',
                'Use \\texttt{aula13\\_arvore\\_decisao.c} para achar o pior caso da \\textbf{inserção} até $n = 10$.',
                'Por que $\\lceil\\lg 5!\\rceil = 7$, mas o merge sort precisa de 8? Existe algoritmo com 7? (Pesquise ``merge insertion'' de Ford e Johnson.)'],
    leitura='Cormen et al., seção 8.1; aproximação de Stirling (equação 3.18).',
)

AULA_14 = dict(
    n=14, bloco=2, tema='Ordenação em tempo linear: contagem e radix', curto='Contagem e radix sort',
    cormen='seções 8.2 e 8.3',
    objetivos=['Ordenar inteiros em $0..k$ por contagem em $\\Theta(n + k)$',
               'Explicar por que a estabilidade é essencial para o radix sort',
               'Ordenar $d$ dígitos em $\\Theta(d(n + k))$ e escolher a base',
               'Medir tempo por elemento: constante no radix, $\\lg n$ no \\texttt{qsort}'],
    roteiro=['Counting sort, estabilidade, radix sort LSD e escolha da base',
             'Contagem e radix em C',
             'Radix (base 256) contra \\texttt{qsort} até 4 milhões de elementos',
             'GPUs, bancos de dados, bioinformática e processamento de imagens'],
    teoria=[
        dict(titulo='Ordenação por contagem', nome='Counting-Sort($A, B, k$)',
             pseudo=r'''\State crie $C[0..k]$ com zeros
\For{$j \atrib 1$ \textbf{até} $n$} \State $C[A[j]] \atrib C[A[j]] + 1$ \EndFor
\State \Comment{$C[i]$ = quantos iguais a $i$}
\For{$i \atrib 1$ \textbf{até} $k$} \State $C[i] \atrib C[i] + C[i-1]$ \EndFor
\State \Comment{$C[i]$ = quantos $\le i$}
\For{$j \atrib n$ \textbf{descendo até} 1}
\State $B[C[A[j]]] \atrib A[j]$
\State $C[A[j]] \atrib C[A[j]] - 1$
\EndFor''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Nenhuma comparação entre chaves: o limite $\Omega(n\lg n)$ não se aplica.
\item Custo $\Theta(n + k)$: linear quando $k = O(n)$.
\item O último laço anda \textbf{de trás para frente}: iguais saem na ordem original. O algoritmo é \textbf{estável}.
\end{itemize}''', largura_texto=0.40),
        dict(titulo='Contagem passo a passo', fig='8.2', altura=0.6,
             legenda='(a) contagens; (b) somas acumuladas; (c)–(e) os três últimos elementos vão para $B$; (f) resultado.'),
        dict(titulo='Radix sort: dígito por dígito', fig='8.3', altura=0.5,
             legenda='do dígito menos significativo para o mais significativo.',
             texto=r'''\Nome{Radix-Sort}($A, d$): para $i = 1$ até $d$, ordene $A$ pelo dígito $i$ com uma ordenação \textbf{estável}.

\medskip\textbf{Lema 8.3:} $d$ dígitos em base $k$: $\Theta(d(n + k))$.

\medskip\textbf{Lema 8.4:} chaves de $b$ bits em grupos de $r$ bits: $\Theta(\frac br(n + 2^r))$. Com $r \approx \lg n$: $\Theta(bn/\lg n)$.''', largura_texto=0.48),
        dict(titulo='Por que a estabilidade importa',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item Depois de ordenar pelo dígito $i$, os empates nesse dígito devem \textbf{manter} a ordem dada pelos dígitos anteriores (menos significativos).
\item Invariante: após a passada $i$, o vetor está ordenado pelos $i$ dígitos menos significativos.
\item Uma ordenação instável (quicksort, heapsort) quebraria o invariante.
\item \textbf{Base na prática:} inteiros de 32 bits em base 256 ($r = 8$): 4 passadas de contagem com vetor $C$ de 256 posições, que cabe no cache.
\end{itemize}''',
             rodape=r'Radix sort é linear, mas não está sempre à frente: precisa de memória extra $\Theta(n)$, e cada passada percorre o vetor todo.'),
    ],
    pratica=dict(
        resumo=['Contagem para chaves pequenas; radix em base 10 para as maiores', 'Laço final de trás para frente: estabilidade',
                'Testes com as entradas das Figuras 8.2 e 8.3'],
        arquivos=[('aula14_contagem_radix.c', 'Contagem e radix sort em C')]),
    experimento=dict(
        programa='aula14_experimento.c', titulo='Linear contra $n\\lg n$, em tempo real',
        pergunta='O tempo por elemento do radix sort fica constante enquanto o do qsort cresce como lg n?',
        resumo=['Radix LSD em base 256 (4 passadas)', '\\texttt{qsort} da biblioteca C',
                'Tempo por elemento, $n = 2^{16}$ a $2^{22}$'],
        hipotese=r'''Se $T(n) = c\,n$, então $T(n)/n = c$: o tempo \textbf{por elemento} do radix sort deve ser \textbf{constante}.
Para o \texttt{qsort}, $T(n)/n = c'\lg n$: deve crescer devagar, como o logaritmo.''',
        metodo=['Inteiros de 32 bits aleatórios', '$n = 2^{16}, \\dots, 2^{22}$ (até 4 milhões)',
                'Tempo: melhor de 3, dividido por $n$ (ns por elemento)', 'Mesmos dados para os dois algoritmos'],
        graficos=[
            dict(titulo='Tempo por elemento', ylabel='ns por elemento', escala='log',
                 series=[dict(col='qsort_ns', rotulo='\\texttt{qsort}'), dict(col='radix_ns', rotulo='radix (base 256)')],
                 teoria=[dict(col='qsort_ns', f='log2(n)', rotulo='$\\lg n$', tolerancia=0.25),
                         dict(col='radix_ns', f='1', rotulo='constante', tolerancia=0.25)],
                 leitura=r'O radix fica em torno de 8 ns por elemento; o \texttt{qsort} passa de 100 ns, e cresce com $\lg n$.'),
        ],
        conclusao=r'''O tempo por elemento do radix sort é praticamente \textbf{constante} (linear no total) e mais de 10 vezes menor que o do \texttt{qsort}, cujo custo por elemento cresce como $\lg n$.
O limite $\Omega(n\lg n)$ não se aplica porque o radix sort \textbf{não compara chaves}: usa os bits delas.''',
        extra=r'Parte da diferença é constante: \texttt{qsort} chama uma função de comparação por ponteiro a cada passo. Compare também com o seu quicksort da aula 11.'),
    conexoes=[
        ('\\faMicrochip', 'GPUs', 'Radix sort é o padrão para ordenar em GPU (CUB, Thrust): as contagens e somas de prefixo paralelizam muito bem.'),
        ('\\faDatabase', 'Bancos de dados', 'Ordenar por chaves inteiras (datas, códigos) com radix e agrupar por contagem (\\texttt{GROUP BY}) aparecem em bancos colunares como DuckDB.'),
        ('\\faDna', 'Bioinformática', 'Arranjos de sufixos de genomas são construídos com radix sort sobre o alfabeto $\\{A, C, G, T\\}$: base 4, chaves curtas.'),
        ('\\faImage', 'Processamento de imagens', 'O histograma de uma imagem é a primeira etapa da contagem; a equalização de histograma usa exatamente as somas acumuladas de $C$.'),
    ],
    exercicios=['(8.2-1) Ilustre a contagem em $A = \\langle 6,0,2,0,1,3,4,6,1,3,2\\rangle$.',
                '(8.2-3) Se o último laço andar de 1 até $n$, o algoritmo ainda funciona? Ainda é estável?',
                '(8.3-1) Ilustre o radix em COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX.',
                '(8.3-4) Ordene $n$ inteiros em $0..n^3 - 1$ em tempo $O(n)$.',
                'Varie a base do experimento (16, 256, 65.536) e explique o resultado pelo lema 8.4 e pelo cache.'],
    leitura='Cormen et al., seções 8.2 e 8.3.',
)

AULA_15 = dict(
    n=15, bloco=2, tema='Bucket sort e seleção em tempo linear', curto='Bucket sort e seleção',
    cormen='seção 8.4 e capítulo 9',
    objetivos=['Ordenar dados uniformes em $[0, 1)$ em tempo esperado linear com baldes',
               'Achar o $i$-ésimo menor sem ordenar, em tempo esperado $\\Theta(n)$',
               'Conhecer a seleção determinística linear (mediana das medianas)',
               'Medir $\\approx 3{,}39\\,n$ comparações para a mediana'],
    roteiro=['Bucket sort e a hipótese de distribuição; \\Nome{Randomized-Select}; \\Nome{Select}',
             'Seleção aleatorizada em C',
             'Mediana em $3{,}39\\,n$; bucket sort uniforme contra concentrado',
             'Estatística, bancos de dados, redes e aprendizado de máquina'],
    teoria=[
        dict(titulo='Bucket sort', fig='8.4', altura=0.58,
             legenda='10 valores em $[0, 1)$ distribuídos em 10 baldes, cada um ordenado e depois concatenado.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Supõe entrada \textbf{uniforme} em $[0, 1)$.
\item $n$ baldes; o valor $x$ vai para o balde $\lfloor n\,x\rfloor$.
\item Cada balde é ordenado por inserção; depois os baldes são concatenados.
\item Com $n_i$ elementos no balde $i$: $E[n_i^2] = 2 - 1/n$, então o tempo esperado é $\Theta(n)$.
\end{itemize}''', largura_texto=0.48),
        dict(titulo='O $i$-ésimo menor', nome='Randomized-Select($A, p, r, i$)',
             pseudo=r'''\If{$p = r$} \State \Return $A[p]$ \EndIf
\State $q \atrib$ \Nome{Randomized-Partition}($A, p, r$)
\State $k \atrib q - p + 1$ \Comment{posição do pivô}
\If{$i = k$} \State \Return $A[q]$
\ElsIf{$i < k$} \State \Return \Nome{Randomized-Select}($A, p, q-1, i$)
\Else \State \Return \Nome{Randomized-Select}($A, q+1, r, i-k$)
\EndIf''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Como o quicksort, mas recursão em \textbf{um} lado só.
\item Tempo esperado $\Theta(n)$: em média, o subproblema encolhe em proporção constante.
\item Para a mediana: $\approx 2(1 + \ln 2)\,n \approx 3{,}39\,n$ comparações.
\item Pior caso: $\Theta(n^2)$, mas só com sorteios muito azarados.
\end{itemize}''', largura_texto=0.40),
        dict(titulo='Seleção linear no pior caso: mediana das medianas', fig='9.1', altura=0.5,
             legenda='grupos de 5; $x$ é a mediana das medianas. A região sombreada é garantidamente maior que $x$.',
             texto=r'''\Nome{Select} (Blum, Floyd, Pratt, Rivest e Tarjan, 1973):
\begin{enumerate}\setlength{\itemsep}{2pt}
\item Divida em grupos de 5 e ache a mediana de cada um.
\item Ache recursivamente a mediana $x$ dessas medianas.
\item Particione em torno de $x$: pelo menos $\frac{3n}{10} - 6$ elementos ficam de cada lado.
\item Recursão no lado certo.
\end{enumerate}
$T(n) \le T(\lceil n/5\rceil) + T(7n/10 + 6) + O(n) = O(n)$.''', largura_texto=0.48),
    ],
    pratica=dict(
        resumo=['Partição aleatorizada da aula 12', 'Laço em vez de recursão: só um lado continua',
                'Lê o vetor e $i$; imprime o $i$-ésimo menor'],
        arquivos=[('aula15_selecao.c', 'Seleção aleatorizada em C')]),
    experimento=dict(
        programa='aula15_experimento.c', titulo='Seleção linear e baldes sob duas distribuições',
        pergunta='A seleção da mediana faz cerca de 3,39 n comparações? E o bucket sort depende da distribuição?',
        resumo=['Mediana: média de no mínimo 200 execuções por $n$', 'Bucket sort: dados uniformes contra todos no mesmo balde',
                'Deslocamentos da inserção dentro dos baldes'],
        hipotese=r'''A seleção aleatorizada da mediana faz em média $2(1 + \ln 2)\,n \approx 3{,}39\,n$ comparações: \textbf{linear}.
No bucket sort, com dados uniformes cada balde tem $O(1)$ elementos e os deslocamentos somam $\approx n/4$; se todos caem no mesmo balde, vira uma inserção: $\approx n^2/4$.''',
        metodo=['Seleção: $n = 2^{10}$ a $2^{18}$; muitas execuções por $n$ (uma só varia de $2n$ a $5n$)',
                'Bucket sort: $n$ baldes, $n$ de 1.000 a 16.000',
                'Concentrada: todos os valores em $[0, 1/n)$', 'Contadores de comparações e deslocamentos'],
        graficos=[
            dict(titulo='Comparações para achar a mediana', ylabel='comparações', escala='log',
                 series=[dict(col='mediana', rotulo='seleção aleatorizada')],
                 teoria=[dict(col='mediana', f='2*(1+log(2))*n', rotulo='$2(1+\\ln 2)\\,n$', ajustar=False, tolerancia=0.05)],
                 leitura=r'Achar a mediana custa só 3,4 comparações por elemento; ordenar, $1{,}39\lg n$ por elemento (mais de 25 para $n = 2^{18}$).'),
            dict(titulo='Bucket sort: a distribuição importa', tabela=1, ylabel='deslocamentos', escala='logy',
                 series=[dict(col='concentrada', rotulo='todos num balde'), dict(col='uniforme', rotulo='uniforme')],
                 teoria=[dict(col='concentrada', f='n*(n-1)/4', rotulo='$n(n-1)/4$', ajustar=False, tolerancia=0.04),
                         dict(col='uniforme', f='n', rotulo='$n$', tolerancia=0.1)],
                 leitura=r'Uniforme: cerca de $0{,}25\,n$ deslocamentos (linear). Concentrada: $n^2/4$, a inserção pura.'),
        ],
        conclusao=r'''A seleção da mediana fica em $\approx 3{,}39\,n$ comparações em média: \textbf{linear}, sem ordenar.
O bucket sort é linear \textbf{se} a hipótese de uniformidade vale; com todos os dados num balde, volta a ser quadrático.
\textbf{Algoritmos de caso médio dependem da distribuição da entrada; aleatorizados, só da sorte.}'''),
    conexoes=[
        ('\\faChartBar', 'Estatística e dados', 'Mediana, quartis e percentis (p50, p99) são seleções. Ferramentas de monitoramento calculam percentis de latência sem ordenar milhões de amostras.'),
        ('\\faDatabase', 'Bancos de dados', '\\texttt{ORDER BY ... LIMIT k} e \\texttt{PERCENTILE\\_CONT} usam seleção; histogramas em baldes guiam o otimizador de consultas.'),
        ('\\faBrain', 'Aprendizado de máquina', 'Árvores de decisão (k-d trees) dividem pela mediana de cada coordenada; a mediana é um estimador robusto contra valores extremos.'),
        ('\\faHashtag', 'Tabelas hash', 'O bucket sort é uma tabela hash ordenada: a análise dos baldes ($E[n_i^2]$) é a mesma do encadeamento da aula 19.'),
    ],
    exercicios=['(8.4-1) Ilustre o bucket sort em $\\langle .79,.13,.16,.64,.39,.20,.89,.53,.71,.42\\rangle$.',
                '(8.4-2) Qual o pior caso do bucket sort? Como torná-lo $O(n\\lg n)$ sem perder o caso médio?',
                '(9.2-3) Escreva \\Nome{Randomized-Select} iterativo.',
                '(9.3-1) No \\Nome{Select}, grupos de 7 funcionam? E grupos de 3?',
                'Implemente o \\Nome{Select} determinístico e meça a constante. Por que ninguém o usa na prática?'],
    leitura='Cormen et al., seção 8.4 e capítulo 9.',
)

AULA_16 = dict(
    n=16, bloco=2, tema='Pilhas, filas e vetores dinâmicos', curto='Pilhas e filas',
    cormen='seção 10.1 e seção 17.4',
    objetivos=['Implementar pilha (LIFO) e fila circular (FIFO) com vetores',
               'Tratar transbordamento e esvaziamento',
               'Analisar o vetor que dobra de tamanho: custo amortizado $O(1)$',
               'Medir $2n$ cópias contra $n^2/2000$ para duas estratégias de crescimento'],
    roteiro=['Pilha, fila circular, análise amortizada da tabela dinâmica',
             'Pilha dinâmica e fila circular em C; parênteses balanceados',
             'Dobrar ou somar 1000? Contando cópias',
             'Compiladores, navegadores, sistemas operacionais e linguagens'],
    teoria=[
        dict(titulo='Pilha: último a entrar, primeiro a sair', fig='10.1', altura=0.32, empilhar=True,
             legenda='(a) pilha com 4 elementos; (b) depois de \\Nome{Push}(17) e \\Nome{Push}(3); (c) depois de \\Nome{Pop}.',
             texto=r'''\Nome{Push}($S, x$): $S.\mathit{topo} \atrib S.\mathit{topo} + 1$; $S[S.\mathit{topo}] \atrib x$.\quad
\Nome{Pop}($S$): se vazia, \textbf{erro}; senão devolve $S[S.\mathit{topo}]$ e decrementa o topo.\quad Todas $O(1)$.'''),
        dict(titulo='Fila circular: primeiro a entrar, primeiro a sair', fig='10.2', altura=0.5,
             legenda='(a) fila com 5 elementos; (b) após \\Nome{Enqueue} de 17, 3 e 5: a cauda dá a volta; (c) após \\Nome{Dequeue}.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \textit{cabeça}: próximo a sair. \textit{cauda}: próxima posição livre.
\item Os índices andam ``em círculo'': depois de $n$ vem 1. Em C: \texttt{(i + 1) \% n}.
\item Vazia: \textit{cabeça} = \textit{cauda}. Para distinguir cheia de vazia, guarde o número de elementos (ou deixe uma posição livre).
\end{itemize}''', largura_texto=0.42),
        dict(titulo='E quando o vetor enche? Tabela dinâmica', fig='17.3', altura=0.58,
             legenda='tamanho alocado ($\\mathit{size}_i$), ocupação ($\\mathit{num}_i$) e potencial $\\Phi_i$ ao longo de 32 inserções.',
             texto=r'''Ao encher, aloque o \textbf{dobro} e copie tudo.
\begin{itemize}\setlength{\itemsep}{4pt}
\item Uma inserção pode custar $\Theta(n)$ (a cópia).
\item Mas $n$ inserções custam no total $n + (1 + 2 + 4 + \dots) < 3n$.
\item \textbf{Custo amortizado} $O(1)$ por inserção.
\item Somar uma constante $c$ em vez de dobrar: total $\Theta(n^2/c)$.
\end{itemize}''', largura_texto=0.42),
    ],
    pratica=dict(
        resumo=['Pilha que dobra com \\texttt{realloc}', 'Fila circular de tamanho fixo (Figura 10.2)',
                'Aplicação: parênteses, colchetes e chaves balanceados'],
        arquivos=[('aula16_pilha_fila.c', 'Pilha e fila em C')]),
    experimento=dict(
        programa='aula16_experimento.c', titulo='Dobrar ou somar 1000?',
        pergunta='Quantas cópias custam n inserções num vetor que dobra e num que cresce 1000 posições por vez?',
        resumo=['Dobrar: $\\approx 2n$ cópias (amortizado $O(1)$)', 'Somar 1000: $\\approx n^2/2000$ cópias',
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
        ('\\faCogs', 'Compiladores', 'Analisadores sintáticos usam pilhas para casar parênteses e blocos; a pilha de chamadas guarda variáveis locais e endereços de retorno.'),
        ('\\faGlobe', 'Navegadores e editores', 'Voltar e avançar, desfazer e refazer: duas pilhas. O DOM é percorrido com pilha (profundidade) ou fila (largura).'),
        ('\\faDesktop', 'Sistemas operacionais', 'Buffers de teclado, de rede e de impressão são filas circulares; o \\emph{ring buffer} é a estrutura dos drivers de rede de alto desempenho.'),
        ('\\faPython', 'Linguagens', 'A lista do Python, o \\texttt{vector} do C++ e o \\texttt{slice} do Go são vetores dinâmicos com crescimento por fator, exatamente a análise desta aula.'),
    ],
    exercicios=['(10.1-1) Ilustre \\Nome{Push}(4), \\Nome{Push}(1), \\Nome{Push}(3), \\Nome{Pop}, \\Nome{Push}(8), \\Nome{Pop} numa pilha vazia.',
                '(10.1-4) Reescreva \\Nome{Enqueue} e \\Nome{Dequeue} detectando transbordamento e esvaziamento.',
                '(10.1-6) Implemente uma fila com duas pilhas. Qual o custo amortizado?',
                'E se, além de crescer, o vetor encolher pela metade quando ficar com $1/4$ ocupado? Por que não encolher já com $1/2$ (seção 17.4.2)?',
                'Altere o experimento para crescer por fator 1,5 e compare com o fator 2.'],
    leitura='Cormen et al., seções 10.1 e 17.4 (tabelas dinâmicas).',
)

AULA_17 = dict(
    n=17, bloco=2, tema='Listas ligadas e sentinelas', curto='Listas ligadas',
    cormen='seções 10.2 e 10.3',
    objetivos=['Implementar busca, inserção e remoção em listas duplamente ligadas',
               'Usar uma sentinela para eliminar casos especiais',
               'Representar listas com vetores (sem ponteiros)',
               'Medir a vantagem da lista na inserção e o custo do cache no percurso'],
    roteiro=['Listas duplamente ligadas, sentinelas, listas em vetores',
             'Lista com sentinela em C',
             'Inserir no início; percorrer uma lista espalhada pela memória',
             'Sistemas operacionais, editores, alocação de memória e cache'],
    teoria=[
        dict(titulo='Lista duplamente ligada', fig='10.3', altura=0.4, empilhar=True,
             legenda='(a) lista $\\langle 9, 16, 4, 1\\rangle$; (b) após \\Nome{List-Insert} de 25; (c) após remover o 4.',
             texto=r'''Cada nó tem \textit{chave}, \textit{prox} e \textit{ant}. \Nome{List-Search}: $\Theta(n)$ no pior caso. \Nome{List-Insert} na cabeça: $O(1)$. \Nome{List-Delete} dado o nó: $O(1)$.'''),
        dict(titulo='Sentinelas', fig='10.4', altura=0.5,
             legenda='lista circular com sentinela $L.\\mathit{nil}$: (a) vazia; (b)–(d) inserções e remoções.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Um nó falso $L.\mathit{nil}$ fica entre a cabeça e a cauda.
\item $L.\mathit{nil}.\mathit{prox}$ é a cabeça; $L.\mathit{nil}.\mathit{ant}$ é a cauda.
\item Remover passa a ser só:
$x.\mathit{ant}.\mathit{prox} \atrib x.\mathit{prox}$;\; $x.\mathit{prox}.\mathit{ant} \atrib x.\mathit{ant}$.
\item Sem testes de lista vazia ou de extremos: código menor e mais difícil de errar.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='Listas sem ponteiros', fig='10.5', altura=0.55,
             legenda='a lista da Figura 10.3(a) guardada em três vetores \\textit{next}, \\textit{key} e \\textit{prev}.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Linguagens sem ponteiros (ou dados em disco) usam índices como ``ponteiros''.
\item Os nós livres formam uma \textbf{lista livre}, usada como pilha: \Nome{Allocate-Object} e \Nome{Free-Object} em $O(1)$.
\item É assim que alocadores de memória e sistemas de arquivos gerenciam blocos.
\end{itemize}''', largura_texto=0.44),
    ],
    pratica=dict(
        resumo=['\\texttt{struct No} com \\texttt{ant} e \\texttt{prox}; sentinela dentro da lista',
                'Inserção na cabeça, busca e remoção sem casos especiais', 'Comandos: \\texttt{i}, \\texttt{b}, \\texttt{r}, \\texttt{p}'],
        arquivos=[('aula17_lista.c', 'Lista com sentinela em C')]),
    experimento=dict(
        programa='aula17_experimento.c', titulo='Ponteiros contra vizinhança',
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
        ('\\faDesktop', 'Sistemas operacionais', 'O kernel Linux usa listas duplamente ligadas circulares com sentinela (\\texttt{list\\_head}) em processos, arquivos abertos e filas de espera.'),
        ('\\faMemory', 'Alocação de memória', '\\texttt{malloc} guarda os blocos livres em listas livres, como na Figura 10.5; coletores de lixo percorrem listas de objetos.'),
        ('\\faMicrochip', 'Arquitetura de computadores', 'O experimento mostra a hierarquia de memória: L1 ($\\approx$1 ns), L2, L3 e RAM ($\\approx$100 ns). Estruturas \\emph{cache-friendly} vencem na prática.'),
        ('\\faEdit', 'Editores de texto', 'Editores mantêm o texto em listas de linhas ou em \\emph{piece tables} ligadas: inserir no meio de um documento grande custa $O(1)$.'),
    ],
    exercicios=['(10.2-1) É possível inserir em $O(1)$ numa lista simplesmente ligada? E remover?',
                '(10.2-2) Implemente uma pilha com lista simplesmente ligada.',
                '(10.2-7) Inverta uma lista simplesmente ligada em $\\Theta(n)$, sem memória extra.',
                '(10.3-2) Implemente \\Nome{Allocate-Object} e \\Nome{Free-Object} para a representação em um só vetor.',
                'No experimento, aloque os nós em ordem (sem embaralhar). O que acontece com o tempo da lista? Por quê?'],
    leitura='Cormen et al., seções 10.2 e 10.3.',
)

PROJETO_2 = dict(
    n=18, bloco=2, tipo='projeto', tema='Projeto 2: simulador de escalonamento de processos',
    descricao='Apresentação dos projetos do Bloco 2. Cada equipe constrói um simulador de escalonamento de CPU com as estruturas do bloco e compara políticas com experimentos.',
    entregas=['Simulador em C: processos chegam com tempo de execução e prioridade; fila (FIFO), heap (prioridade e menor trabalho primeiro) e lista ligada (processos bloqueados)',
              'Três políticas: FIFO, menor trabalho primeiro (heap) e \\emph{round robin} (fila circular)',
              'Experimento: tempo médio de espera e vazão para 1.000 a 1.000.000 de processos, com o custo das operações confrontado com a teoria',
              'Relatório: qual política vence em cada carga e quanto custa cada estrutura (gráficos com curvas teóricas)',
              'Apresentação de 10 minutos com demonstração ao vivo'],
)

AULAS_B2 = [AULA_10, AULA_11, AULA_12, AULA_13, AULA_14, AULA_15, AULA_16, AULA_17, PROJETO_2]
