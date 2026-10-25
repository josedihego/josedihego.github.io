"""Bloco 1 – Fundamentos, ordenação e custo (aulas 1 a 9)."""

AULA_01 = dict(
    n=1, bloco=1, tema='Algoritmos, eficiência e o método experimental', curto='Algoritmos e eficiência',
    cormen='capítulo 1',
    objetivos=['Definir algoritmo, instância e corretude',
               'Explicar por que eficiência importa mais que hardware',
               'Medir tempo de execução em C de forma confiável',
               'Usar a razão de dobra para reconhecer crescimento linear e quadrático'],
    roteiro=['Algoritmos como tecnologia; o exemplo dos dois computadores',
             'Cronômetro em C: relógio monotônico, repetições, melhor de 5',
             'Dobrar $n$ e observar o tempo: $\\times 2$ ou $\\times 4$?',
             'IA, criptografia, computação verde e engenharia de desempenho'],
    teoria=[
        dict(titulo='O que é um algoritmo',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Um procedimento computacional bem definido que recebe uma \textbf{entrada} e produz uma \textbf{saída}.
\item Resolve um \textbf{problema}: a relação desejada entre entrada e saída. Uma \textbf{instância} é uma entrada concreta.
\item É \textbf{correto} se, para toda instância, para com a saída certa.
\item Uma \textbf{estrutura de dados} organiza os dados para facilitar acesso e modificação: nenhuma serve para tudo.
\item Alguns problemas não têm solução eficiente conhecida: os \textbf{NP-completos} (caixeiro-viajante, por exemplo).
\end{itemize}''',
             rodape=r'Este curso: algoritmos clássicos de ordenação, busca e grafos e as estruturas que os tornam rápidos, sempre com teoria \textbf{e} medição.'),
        dict(titulo='Eficiência vale mais que hardware',
             texto=r'''Ordenar $n = 10^7$ números (exemplo da seção 1.2):

\medskip\begin{tabular}{lll}\toprule & \textbf{Computador A} & \textbf{Computador B}\\\midrule
Velocidade & $10^{10}$ instr./s & $10^{7}$ instr./s (1000$\times$ mais lento)\\
Algoritmo & inserção, $2n^2$ & merge sort, $50\,n\lg n$\\
Programador & o melhor do mundo, em assembly & mediano, com compilador ruim\\
\textbf{Tempo} & $\dfrac{2\cdot(10^7)^2}{10^{10}} = 20\,000$ s $\approx$ \textbf{5,5 h} & $\dfrac{50\cdot10^7\lg 10^7}{10^7} \approx 1\,163$ s $<$ \textbf{20 min}\\\bottomrule\end{tabular}''',
             rodape=r'O computador 1000 vezes mais lento termina \textbf{17 vezes antes}. Com $n = 10^8$, a vantagem passa de 100 vezes.'),
        dict(titulo='Duas maneiras de medir',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.48\textwidth}
\begin{cartao}{cteoria}\textbf{Contar operações}\par\footnotesize Conta comparações, atribuições ou acessos.
\begin{itemize}\item Independe da máquina e do compilador.\item Exata e reproduzível.\item Ignora cache, desvio de fluxo e memória.\end{itemize}\end{cartao}
\end{column}\begin{column}{0.48\textwidth}
\begin{cartao}{cexperimento}\textbf{Medir tempo}\par\footnotesize Relógio antes e depois.
\begin{itemize}\item Mostra o custo real.\item Ruidoso: outros processos, frequência da CPU.\item Pede repetições e o \textbf{mínimo} (ou a mediana).\end{itemize}\end{cartao}
\end{column}\end{columns}''',
             rodape=r'\textbf{Razão de dobra:} se $T(n) \approx c\,n^k$, então $T(2n)/T(n) \approx 2^k$. Razão 2: linear. Razão 4: quadrático. Razão 8: cúbico.'),
    ],
    pratica=dict(
        resumo=['\\texttt{clock\\_gettime(CLOCK\\_MONOTONIC)}: o relógio certo para medir',
                'Um algoritmo linear (soma) e um quadrático (pares com soma zero)',
                '\\texttt{volatile} impede o compilador de apagar o trabalho'],
        notas=[dict(titulo='Armadilhas de quem mede tempo',
                    texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \textbf{Otimização elimina código morto.} Se o resultado não é usado, \texttt{-O2} pode apagar o laço inteiro. Guarde o resultado numa variável \texttt{volatile}.
\item \textbf{Resolução do relógio.} \texttt{clock()} mede tempo de CPU em passos grosseiros; use \texttt{clock\_gettime} e repita até o tempo passar de milissegundos.
\item \textbf{Ruído do sistema.} Interrupções só aumentam o tempo: o \textbf{mínimo} de várias execuções é a estimativa mais limpa.
\item \textbf{Aquecimento.} A primeira execução paga falhas de página e cache frio.
\end{itemize}''')],
        arquivos=[('aula01_cronometro.c', 'Cronômetro e dois algoritmos')]),
    experimento=dict(
        programa='aula01_experimento.c', titulo='Dobrar $n$: o tempo dobra ou quadruplica?',
        pergunta='Ao dobrar n, o tempo de um algoritmo linear dobra e o de um quadrático quadruplica?',
        resumo=['Hipótese: $T_{\\text{lin}} \\approx a\\,n$ e $T_{\\text{quad}} \\approx b\\,n^2$',
                'Melhor de 5 execuções, $n$ de 2.000 a 32.000', 'Ajuste da constante por mínimos quadrados'],
        hipotese=r'''A soma percorre o vetor uma vez: $T(n) \approx a\,n$. A contagem de pares examina $\binom{n}{2}$ pares: $T(n) \approx b\,n^2$.
Ao dobrar $n$, esperamos razões perto de 2 e de 4. As constantes $a$ e $b$ dependem da máquina; as \textbf{formas} não.''',
        metodo=['Vetor aleatório de inteiros em $[-1000, 1000]$',
                '$n$ de 2.000 a 32.000, passo 2.000',
                'Tempo: mínimo de 5 execuções (\\texttt{CLOCK\\_MONOTONIC})',
                'Ajuste $c\\cdot f(n)$ pelo método dos mínimos quadrados'],
        graficos=[
            dict(titulo='Tempo do algoritmo quadrático', ylabel='tempo (ms)',
                 series=[dict(col='quadratico_ms', rotulo='pares (medido)')],
                 teoria=[dict(col='quadratico_ms', f='n**2', rotulo='$n^2$', tolerancia=0.25)],
                 leitura=r'A razão tempo$/n^2$ estabiliza: esse valor é a constante $b$ da sua máquina.'),
            dict(titulo='Tempo do algoritmo linear', ylabel='tempo (ms)',
                 series=[dict(col='linear_ms', rotulo='soma (medido)')],
                 teoria=[dict(col='linear_ms', f='n', rotulo='$n$', tolerancia=0.25)],
                 leitura=r'Uma reta. Pontos fora da curva são interrupções do sistema: por isso usamos o mínimo de 5.'),
        ],
        conclusao=r'''Os dois tempos seguem a forma prevista: a curva do quadrático é uma parábola e a do linear, uma reta.
Para $n = 32.000$, o algoritmo quadrático já gasta cerca de 100 vezes mais que o linear, e a distância cresce com $n$.
\textbf{A forma da curva é uma propriedade do algoritmo; a constante é da máquina.}''',
        extra=r'Rode na sua máquina: as constantes mudam, as razões de dobra não.'),
    conexoes=[
        ('\\faBrain', 'Inteligência artificial', 'Treinar um modelo de linguagem custa da ordem de $6 \\times$ parâmetros $\\times$ tokens operações: a análise de custo decide quais modelos são viáveis.'),
        ('\\faLock', 'Criptografia', 'A segurança do RSA depende de não existir algoritmo eficiente conhecido para fatorar inteiros grandes: a ineficiência vira proteção.'),
        ('\\faLeaf', 'Computação verde', 'Data centers consomem cerca de 1--2\\% da energia elétrica mundial. Trocar $n^2$ por $n\\lg n$ economiza energia, não só tempo.'),
        ('\\faTachometerAlt', 'Engenharia de desempenho', 'Ferramentas como \\texttt{perf}, \\texttt{gprof} e testes de regressão de desempenho em integração contínua aplicam o método desta aula na indústria.'),
    ],
    exercicios=['(1.1-1) Dê um exemplo do mundo real que exija ordenação e um que exija o menor caminho.',
                '(1.2-2) Para que $n$ a inserção ($8n^2$ passos) vence o merge sort ($64\\,n\\lg n$ passos)?',
                '(1.2-3) Qual o menor $n$ em que $100\\,n^2$ é mais rápido que $2^n$?',
                'Rode o experimento com \\texttt{-O0} e com \\texttt{-O2}. O que muda: a forma ou a constante?',
                'Implemente uma contagem de pares em $O(n\\lg n)$ (ordene e use dois índices) e meça.'],
    leitura='Cormen et al., capítulo 1 e problema 1-1.',
)

AULA_03 = dict(
    n=3, bloco=1, tema='Análise de algoritmos: o modelo RAM e os casos', curto='Análise de algoritmos',
    cormen='seção 2.2',
    objetivos=['Descrever o modelo RAM e o que ele ignora',
               'Calcular $T(n)$ da inserção somando custo $\\times$ vezes de cada linha',
               'Distinguir melhor caso, pior caso e caso médio',
               'Prever e medir o caso médio exato: $n(n-1)/4 + n - H_n$'],
    roteiro=['Modelo RAM, custo por linha, melhor e pior caso, ordem de crescimento',
             'Instrumentar cada linha da inserção e conferir a tabela do livro',
             'Média de 300 permutações e o histograma das comparações',
             'Tempo real, segurança, compiladores e serviços web'],
    teoria=[
        dict(titulo='O modelo RAM',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Um processador, instruções executadas \textbf{uma após a outra}, sem concorrência.
\item Operações elementares custam tempo \textbf{constante}: aritmética, comparação, cópia, desvio, acesso a uma posição da memória.
\item Palavras de tamanho limitado ($c\lg n$ bits): não se esconde trabalho em inteiros gigantes.
\item Ignora a hierarquia de memória (cache, memória virtual). Quando ela importa, medimos.
\end{itemize}''',
             rodape=r'\textbf{Tamanho da entrada} depende do problema: número de itens (ordenação), número de bits (multiplicação), vértices e arestas (grafos).'),
        dict(titulo='Custo linha a linha da inserção',
             texto=r'''\renewcommand{\arraystretch}{1.25}\begin{tabular}{rlcl}\toprule & \textbf{Linha} & \textbf{Custo} & \textbf{Vezes}\\\midrule
1 & \textbf{para} $j \atrib 2$ \textbf{até} $n$ & $c_1$ & $n$\\
2 & $\mathit{chave} \atrib A[j]$ & $c_2$ & $n-1$\\
4 & $i \atrib j-1$ & $c_4$ & $n-1$\\
5 & \textbf{enquanto} $i>0$ \textbf{e} $A[i]>\mathit{chave}$ & $c_5$ & $\sum_{j=2}^{n} t_j$\\
6 & $A[i+1] \atrib A[i]$ & $c_6$ & $\sum_{j=2}^{n} (t_j - 1)$\\
7 & $i \atrib i-1$ & $c_7$ & $\sum_{j=2}^{n} (t_j - 1)$\\
8 & $A[i+1] \atrib \mathit{chave}$ & $c_8$ & $n-1$\\\bottomrule\end{tabular}

\medskip $t_j$ = número de testes do \textbf{enquanto} para aquele $j$. $T(n)$ = soma de custo $\times$ vezes.'''),
        dict(titulo='Melhor caso e pior caso',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.48\textwidth}
\begin{cartao}{cok}\textbf{Melhor caso: vetor ordenado}\par\footnotesize
$t_j = 1$ para todo $j$:
\[T(n) = (c_1{+}c_2{+}c_4{+}c_5{+}c_8)\,n - (c_2{+}c_4{+}c_5{+}c_8) = a n + b\]
Função \textbf{linear} de $n$.\end{cartao}
\end{column}\begin{column}{0.48\textwidth}
\begin{cartao}{cconexoes}\textbf{Pior caso: vetor invertido}\par\footnotesize
$t_j = j$, e $\sum_{j=2}^{n} j = \frac{n(n+1)}{2} - 1$:
\[T(n) = a n^2 + b n + c\]
Função \textbf{quadrática} de $n$.\end{cartao}
\end{column}\end{columns}''',
             rodape=r'Por que olhar o \textbf{pior caso}? É uma garantia; ocorre com frequência (buscar algo ausente); e o caso médio costuma ser tão ruim quanto ele.'),
        dict(titulo='Caso médio e ordem de crescimento',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Numa permutação aleatória, cada elemento é menor que metade dos anteriores, em média: $t_j \approx j/2$. Ainda \textbf{quadrático}.
\item Mais precisamente: comparações = inversões $+ (n-1) -$ (mínimos à esquerda $-1$). Como $E[\text{inversões}] = n(n-1)/4$ e $E[\text{mínimos}] = H_n$:
\[E[\text{comparações}] = \frac{n(n-1)}{4} + n - H_n, \qquad H_n = 1 + \tfrac12 + \dots + \tfrac1n \approx \ln n\]
\item \textbf{Ordem de crescimento:} só o termo dominante importa, sem a constante: a inserção é $\Theta(n^2)$ no pior caso.
\end{itemize}''',
             rodape=r'Um algoritmo é mais eficiente que outro se seu pior caso tem ordem de crescimento menor. Para $n$ pequeno, as constantes podem inverter isso.'),
    ],
    pratica=dict(
        resumo=['Um contador para cada linha do pseudocódigo', 'Conferir a coluna ``vezes'' da tabela do livro',
                'Testes: ordenado, invertido e a entrada da Figura 2.2'],
        arquivos=[('aula03_custo_por_linha.c', 'Contando cada linha')]),
    experimento=dict(
        programa='aula03_experimento.c', titulo='O caso médio, medido',
        pergunta='A média de comparações da inserção em permutações aleatórias bate com n(n−1)/4 + n − H_n?',
        resumo=['Hipótese: média exata $n(n-1)/4 + n - H_n$', '300 permutações uniformes (Fisher–Yates) por $n$',
                'Histograma de 100.000 execuções com $n = 100$'],
        hipotese=r'''A média de comparações da inserção numa permutação uniforme é
\[\frac{n(n-1)}{4} + n - H_n,\]
entre o melhor caso ($n-1$) e o pior ($n(n-1)/2$), praticamente na metade do pior.
Além disso, as execuções se \textbf{concentram} em torno da média.''',
        metodo=['Permutações uniformes com o embaralhamento de Fisher–Yates',
                '$n$ de 100 a 2.000; média de 300 permutações por $n$',
                'Histograma: $n = 100$, 100.000 permutações, classes de largura 50',
                'Comparação direta com a fórmula (sem ajuste de constante)'],
        graficos=[
            dict(titulo='Média medida e fórmula exata', ylabel='comparações',
                 series=[dict(col='pior', rotulo='pior caso'), dict(col='media', rotulo='média medida'),
                         dict(col='melhor', rotulo='melhor caso')],
                 teoria=[dict(col='media', f='n*(n-1)/4 + n - sum(1/k for k in range(1, int(n)+1))',
                              rotulo='$\\frac{n(n-1)}{4}+n-H_n$', ajustar=False, tolerancia=0.02)],
                 leitura=r'A média fica a menos de 1\% da fórmula: com 300 amostras, a média amostral já está muito perto da esperança.'),
            dict(titulo='Como as execuções se distribuem ($n = 100$)', tabela=1, x='comparacoes', xlabel='comparações',
                 ylabel='permutações', opcoes='ybar,bar width=3pt,ymin=0',
                 series=[dict(col='frequencia', rotulo='100.000 execuções', estilo='ybar,fill=cexperimento!60,draw=cexperimento,mark=none')],
                 leitura=r'Forma de sino em torno de $100\cdot99/4 + 100 - H_{100} \approx 2570$. O desvio padrão cresce como $n^{3/2}$, mais devagar que a média ($n^2$): em proporção, as execuções ficam cada vez mais parecidas.'),
        ],
        conclusao=r'''A fórmula do caso médio é confirmada: a média medida fica a menos de 1\% de $n(n-1)/4 + n - H_n$, praticamente a metade do pior caso.
O histograma mostra que execuções muito diferentes da média são raras. \textbf{Caso médio quadrático:} para dados aleatórios, a inserção não escapa de $\Theta(n^2)$.'''),
    conexoes=[
        ('\\faHeartbeat', 'Sistemas de tempo real', 'Freio ABS e marca-passo não podem atrasar: a análise de \\textbf{pior caso} de tempo de execução (WCET) garante que todo prazo seja cumprido.'),
        ('\\faUserSecret', 'Segurança', 'Ataques de complexidade enviam a entrada do pior caso de propósito: expressões regulares catastróficas (ReDoS) e colisões em tabelas hash derrubam servidores.'),
        ('\\faCogs', 'Compiladores', 'Otimizadores usam modelos de custo por instrução, como a tabela desta aula, para decidir desenrolar laços, embutir funções ou vetorizar.'),
        ('\\faServer', 'Serviços web', 'Média engana: plataformas monitoram a \\textbf{cauda} (latência p99, p99,9), porque com milhões de requisições o pior caso acontece a cada segundo.'),
    ],
    exercicios=['(2.2-1) Escreva $n^3/1000 - 100n^2 - 100n + 3$ em notação $\\Theta$.',
                '(2.2-2) Ordenação por seleção: escreva o pseudocódigo, dê o invariante e o tempo de melhor e pior caso.',
                '(2.2-3) Busca linear: quantos elementos são examinados, em média e no pior caso?',
                'Use \\texttt{aula03\\_custo\\_por\\_linha.c} para conferir: linha 5 executa $\\sum t_j$ vezes; linhas 6 e 7, $\\sum (t_j - 1)$.',
                'Altere o experimento para $n = 400$ e compare a largura relativa do histograma com a de $n = 100$.'],
    leitura='Cormen et al., seção 2.2; para $H_n$, apêndice A.1.',
)

AULA_02 = dict(
    n=2, bloco=1, tema='Ordenação por inserção e invariantes de laço', curto='Ordenação por inserção',
    cormen='seção 2.1',
    objetivos=['Executar a ordenação por inserção à mão, passo a passo',
               'Provar a corretude com um invariante de laço: inicialização, manutenção e término',
               'Traduzir o pseudocódigo (índices $1..n$) para C (índices $0..n-1$)',
               'Medir comparações e confrontar com $n-1$, $n^2/4$ e $n(n-1)/2$'],
    roteiro=['O problema da ordenação, o algoritmo e a prova por invariante',
             'Implementação em C e testes com a entrada do livro',
             'Contar comparações em entradas ordenadas, aleatórias e invertidas',
             'Timsort, sistemas embarcados, fluxos de dados e verificação formal'],
    teoria=[
        dict(titulo='O problema da ordenação',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Entrada:} uma sequência de $n$ números $\langle a_1, a_2, \dots, a_n\rangle$.
\item \textbf{Saída:} uma permutação $\langle a'_1, a'_2, \dots, a'_n\rangle$ com $a'_1 \le a'_2 \le \dots \le a'_n$.
\item Os números são as \textbf{chaves}; na prática, cada chave carrega \emph{dados satélite} (um registro inteiro).
\item Ordenação por inserção: eficiente para $n$ pequeno, \textbf{no lugar} (\emph{in place}) e \textbf{estável}.
\item Ideia: como ordenamos cartas na mão. Cada carta nova é comparada da direita para a esquerda até achar seu lugar.
\end{itemize}''',
             rodape=r'Um algoritmo é \textbf{correto} se, para toda entrada, ele para com a saída certa. Testes mostram erros; só a prova mostra corretude.'),
        dict(titulo='O algoritmo', nome='Ordena-Inserção($A$)',
             pseudo=r'''\For{$j \atrib 2$ \textbf{até} $A.\mathit{comprimento}$}
\State $\mathit{chave} \atrib A[j]$
\State \Comment{insere $A[j]$ na sequência ordenada $A[1..j-1]$}
\State $i \atrib j - 1$
\While{$i > 0$ \textbf{e} $A[i] > \mathit{chave}$}
\State $A[i+1] \atrib A[i]$
\State $i \atrib i - 1$
\EndWhile
\State $A[i+1] \atrib \mathit{chave}$
\EndFor''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item $j$ aponta a ``carta'' que será inserida.
\item $A[1..j-1]$ já está ordenado: é a mão.
\item O \textbf{enquanto} desloca para a direita todos os maiores que a chave.
\item A chave cai no buraco aberto em $A[i+1]$.
\end{itemize}''', largura_texto=0.40),
        dict(titulo='Execução em $A = \\langle 5, 2, 4, 6, 1, 3\\rangle$', fig='2.2',
             legenda='(a)–(e) cada volta do \\textbf{para}: o retângulo preto é $A[j]$; as setas mostram os deslocamentos. (f) vetor ordenado.',
             altura=0.5,
             rodape=r'Em (d), a chave 1 é a menor de todas: o \textbf{enquanto} percorre a mão inteira. Esse é o caso que custa caro.'),
        dict(titulo='Invariante de laço',
             texto=r'''No início de cada iteração do \textbf{para} (linhas 1–8), o subvetor $A[1..j-1]$ contém os elementos que estavam originalmente em $A[1..j-1]$, \textbf{em ordem}.

\medskip Para usar um invariante, mostramos três coisas:
\begin{enumerate}\setlength{\itemsep}{4pt}
\item \textbf{Inicialização:} vale antes da primeira iteração.
\item \textbf{Manutenção:} se vale antes de uma iteração, vale antes da próxima.
\item \textbf{Término:} quando o laço acaba, o invariante dá uma propriedade útil.
\end{enumerate}''',
             rodape=r'É a \textbf{indução matemática}: inicialização é a base, manutenção é o passo. A diferença: paramos quando o laço termina.'),
        dict(titulo='A prova de corretude',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item \textbf{Inicialização.} Com $j = 2$, $A[1..1]$ tem um só elemento, o original, e um elemento sozinho está ordenado.
\item \textbf{Manutenção.} O corpo do laço move $A[j-1], A[j-2], \dots$ uma posição à direita até achar o lugar de $A[j]$ e o insere ali. Então $A[1..j]$ tem os elementos originais, em ordem. Incrementar $j$ restaura o invariante.
\item \textbf{Término.} O laço para quando $j = n + 1$. Substituindo no invariante: $A[1..n]$ tem os elementos originais, em ordem. Ou seja, \textbf{o vetor inteiro está ordenado}.
\end{itemize}''',
             rodape=r'Rigor completo exigiria um invariante também para o \textbf{enquanto} interno (exercício 2.1-3 usa a mesma técnica na busca linear).'),
    ],
    pratica=dict(
        resumo=['Do pseudocódigo ($1..n$) para C ($0..n-1$)', 'Leitura com \\texttt{malloc}, ordenação e impressão',
                'Teste com a entrada da Figura 2.2'],
        notas=[dict(titulo='Do livro para o C',
                    texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.5\textwidth}
\renewcommand{\arraystretch}{1.3}\begin{tabular}{ll}\toprule \textbf{Cormen} & \textbf{C}\\\midrule
$A[1..n]$ & \texttt{A[0]} a \texttt{A[n-1]}\\
\textbf{para} $j \atrib 2$ \textbf{até} $n$ & \texttt{for (j = 1; j < n; j++)}\\
$i > 0$ & \texttt{i >= 0}\\
$A.\mathit{comprimento}$ & parâmetro \texttt{n}\\\bottomrule\end{tabular}
\end{column}\begin{column}{0.44\textwidth}
\begin{destaque}[cpratica]O erro mais comum: copiar o $i > 0$ do livro. Em C o primeiro elemento é \texttt{A[0]}; com \texttt{i > 0} ele nunca é comparado.\end{destaque}
\begin{destaque}[cexperimento]\texttt{A[i] > chave} (estrito) mantém a ordem dos iguais: o algoritmo é \textbf{estável}.\end{destaque}
\end{column}\end{columns}''')],
        arquivos=[('aula02_insercao.c', 'Ordenação por inserção em C')]),
    experimento=dict(
        programa='aula02_experimento.c', titulo='Quantas comparações a inserção faz?',
        pergunta='Quantas comparações a ordenação por inserção faz em entradas ordenadas, aleatórias e invertidas?',
        resumo=['Hipótese: $n-1$, $\\approx n^2/4$ e $n(n-1)/2$ comparações',
                'Contador instrumentado no teste $A[i] > \\mathit{chave}$', 'De $n = 500$ a $8000$, semente fixa'],
        hipotese=r'''Para $n$ elementos, o teste $A[i] > \mathit{chave}$ é feito
\begin{itemize}\item $n-1$ vezes se o vetor já está \textbf{ordenado} (melhor caso);
\item $n(n-1)/2$ vezes se está \textbf{invertido} (pior caso);
\item cerca de $n^2/4$ vezes numa ordem \textbf{aleatória}: cada par fora de ordem (inversão) custa uma comparação, e em média metade dos $\binom{n}{2}$ pares está invertida.\end{itemize}''',
        metodo=['Variável global \\texttt{comparacoes} incrementada dentro da condição do \\texttt{while}',
                '$n$ de 500 a 8000, passo 500',
                'Aleatório: média de 5 permutações (\\texttt{srand(2026)}, reproduzível)',
                'Saída em CSV: \\texttt{n,ordenado,aleatorio,invertido}'],
        graficos=[
            dict(titulo='Comparações medidas e previstas', ylabel='comparações',
                 series=[dict(col='invertido', rotulo='invertido'), dict(col='aleatorio', rotulo='aleatório'),
                         dict(col='ordenado', rotulo='ordenado')],
                 teoria=[dict(col='aleatorio', f='n*n/4', rotulo='$n^2/4$', ajustar=False, tolerancia=0.03),
                         dict(col='invertido', f='n*(n-1)/2', rotulo='$n(n-1)/2$', ajustar=False, tolerancia=0.0001),
                         dict(col='ordenado', f='n-1', rotulo='$n-1$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'A razão medido/$(n^2/4)$ fica colada em 1: a média de inversões de uma permutação aleatória é $n(n-1)/4$.'),
            dict(titulo='Em escala log-log, o expoente vira inclinação', ylabel='comparações', escala='log',
                 series=[dict(col='aleatorio', rotulo='aleatório'), dict(col='ordenado', rotulo='ordenado')],
                 teoria=[dict(col='aleatorio', f='n**2', rotulo='$n^2$', tolerancia=0.03),
                         dict(col='ordenado', f='n', rotulo='$n$', tolerancia=0.01)],
                 leitura=r'Se $T(n) = c\,n^k$, então $\log T = \log c + k \log n$: uma reta de inclinação $k$. Aleatório: inclinação 2. Ordenado: inclinação 1.'),
        ],
        conclusao=r'''As três previsões se confirmam: \textbf{exatamente} $n-1$ e $n(n-1)/2$ nos casos extremos, e $n^2/4$ com desvio abaixo de 3\% no caso aleatório.
A ordenação por inserção é \textbf{linear} em dados ordenados e \textbf{quadrática} em dados aleatórios: o tipo de entrada importa tanto quanto o tamanho.''',
        extra=r'Desafio: conte também os deslocamentos ($A[i+1] \atrib A[i]$) e compare com o número de inversões da entrada (problema 2-4).'),
    conexoes=[
        ('\\faPython', 'Bibliotecas de linguagens', 'O Timsort (\\texttt{sorted} do Python, \\texttt{Arrays.sort} de objetos no Java) ordena trechos curtos com inserção binária: para $n$ pequeno, ela vence algoritmos $n\\lg n$.'),
        ('\\faMicrochip', 'Sistemas embarcados', 'No lugar, sem recursão e com código minúsculo: cabe em microcontroladores com poucos KB de RAM, onde \\texttt{malloc} e pilha profunda são luxo.'),
        ('\\faStream', 'Fluxos de dados', 'É um algoritmo \\emph{online}: ordena à medida que os dados chegam. Manter um placar ao vivo ou as $k$ maiores leituras de um sensor é uma inserção por evento.'),
        ('\\faCheckDouble', 'Verificação formal', 'Invariantes de laço são a base de ferramentas como Dafny, Frama-C (ACSL) e Why3, que provam código real. Sem o invariante, o provador não consegue.'),
    ],
    exercicios=['(2.1-1) Ilustre a execução em $A = \\langle 31, 41, 59, 26, 41, 58\\rangle$, como na Figura 2.2.',
                '(2.1-2) Reescreva o pseudocódigo para ordenar em ordem \\textbf{decrescente}.',
                '(2.1-3) Escreva a busca linear e prove sua corretude com um invariante de laço.',
                'Altere o experimento para contar deslocamentos e verifique: deslocamentos = número de inversões.',
                'Meça o \\textbf{tempo} (com \\texttt{clock()}) além das comparações. A forma da curva muda?'],
    leitura='Cormen et al., seção 2.1 e problema 2-4 (inversões).',
)


AULA_04 = dict(
    n=4, bloco=1, tema='Dividir e conquistar: merge sort', curto='Merge sort',
    cormen='seção 2.3',
    objetivos=['Aplicar o paradigma dividir, conquistar e combinar',
               'Executar \\Nome{Merge} e provar sua corretude por invariante',
               'Escrever a recorrência do merge sort e resolvê-la pela árvore de recursão',
               'Medir $n\\lg n$ e achar o ponto em que a inserção deixa de valer a pena'],
    roteiro=['Paradigma, \\Nome{Merge} com sentinelas, recorrência e árvore de recursão',
             'Merge sort em C com vetores auxiliares',
             'Comparações $\\approx n\\lg n - 1{,}26\\,n$ e o cruzamento com a inserção',
             'Big Data, bancos de dados, LSM-trees e paralelismo'],
    teoria=[
        dict(titulo='Dividir, conquistar, combinar',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \textbf{Dividir} o problema em subproblemas menores do mesmo tipo.
\item \textbf{Conquistar} os subproblemas recursivamente; se forem pequenos, resolver direto.
\item \textbf{Combinar} as soluções dos subproblemas na solução do problema.
\end{itemize}
\medskip No merge sort: dividir o vetor ao meio ($\Theta(1)$), ordenar cada metade recursivamente, \textbf{intercalar} as duas metades ordenadas ($\Theta(n)$).''',
             fig='2.4', legenda='merge sort de baixo para cima em $\\langle 5,2,4,7,1,3,2,6\\rangle$.', largura_texto=0.46),
        dict(titulo='Intercalação com sentinelas', nome='Merge($A, p, q, r$)',
             pseudo=r'''\State $n_1 \atrib q - p + 1$;\quad $n_2 \atrib r - q$
\State crie $L[1..n_1+1]$ e $R[1..n_2+1]$
\For{$i \atrib 1$ \textbf{até} $n_1$} \State $L[i] \atrib A[p+i-1]$ \EndFor
\For{$j \atrib 1$ \textbf{até} $n_2$} \State $R[j] \atrib A[q+j]$ \EndFor
\State $L[n_1+1] \atrib \infty$;\quad $R[n_2+1] \atrib \infty$
\State $i \atrib 1$;\quad $j \atrib 1$
\For{$k \atrib p$ \textbf{até} $r$}
\If{$L[i] \le R[j]$}
\State $A[k] \atrib L[i]$;\quad $i \atrib i+1$
\Else
\State $A[k] \atrib R[j]$;\quad $j \atrib j+1$
\EndIf
\EndFor''',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Duas pilhas de cartas ordenadas, viradas para cima: a menor do topo vai para a saída.
\item As sentinelas $\infty$ evitam testar se uma pilha acabou.
\item Exatamente $n = r - p + 1$ passos: \textbf{$\Theta(n)$}.
\item Invariante: $A[p..k-1]$ tem os $k-p$ menores de $L$ e $R$, em ordem.
\end{itemize}''', largura_texto=0.38),
        dict(titulo='Intercalação passo a passo', fig='2.3', altura=0.58,
             legenda='(a)–(d) as primeiras iterações de \\Nome{Merge}($A$, 9, 12, 16); em cinza claro, o que já foi copiado.'),
        dict(titulo='O algoritmo e sua recorrência', nome='Merge-Sort($A, p, r$)',
             pseudo=r'''\If{$p < r$}
\State $q \atrib \lfloor (p + r)/2 \rfloor$
\State \Nome{Merge-Sort}($A, p, q$)
\State \Nome{Merge-Sort}($A, q+1, r$)
\State \Nome{Merge}($A, p, q, r$)
\EndIf''',
             texto=r'''Chamada inicial: \Nome{Merge-Sort}($A, 1, n$).

\medskip Para $n$ potência de 2:
\[T(n) = \begin{cases} c & n = 1\\ 2\,T(n/2) + c\,n & n > 1\end{cases}\]
Dividir custa $\Theta(1)$, conquistar custa $2T(n/2)$, combinar custa $\Theta(n)$.''', largura_texto=0.46),
        dict(titulo='Árvore de recursão: $T(n) = c\\,n\\lg n + c\\,n$', fig='2.5', altura=0.66, empilhar=True,
             legenda='cada nível soma $cn$; há $\\lg n + 1$ níveis.',
             texto=r'Cada nível da árvore custa $cn$ no total; com $\lg n + 1$ níveis, $T(n) = cn\lg n + cn = \Theta(n\lg n)$.'),
    ],
    pratica=dict(
        resumo=['\\texttt{intercala} sem sentinelas: testa o fim de \\texttt{L} e \\texttt{R}',
                '\\texttt{<=} na intercalação mantém o algoritmo \\textbf{estável}',
                'Teste com a entrada da Figura 2.4'],
        notas=[dict(titulo='Sentinelas $\\infty$ em C?',
                    texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.5\textwidth}
\begin{itemize}\setlength{\itemsep}{5pt}
\item O livro usa $\infty$ no fim de $L$ e $R$. Em C, \texttt{INT\_MAX} funciona só se nenhum dado for igual a \texttt{INT\_MAX}.
\item Solução robusta: testar o fim de cada lado.
\item \texttt{if (j >= n2 || (i < n1 \&\& L[i] <= R[j]))}: se $R$ acabou, ou se $L[i]$ é o menor, copia de $L$.
\end{itemize}\end{column}\begin{column}{0.45\textwidth}
\begin{destaque}[cpratica]\textbf{Memória:} o merge sort usa $\Theta(n)$ de memória extra; não é \emph{in place}. No experimento usamos um único vetor auxiliar para não chamar \texttt{malloc} a cada intercalação.\end{destaque}
\end{column}\end{columns}''')],
        arquivos=[('aula04_merge_sort.c', 'Merge sort em C')]),
    experimento=dict(
        programa='aula04_experimento.c', titulo='$n\\lg n$ na prática e o ponto de cruzamento',
        pergunta='O merge sort faz cerca de n lg n comparações? Para que n ele passa a vencer a inserção?',
        resumo=['Hipótese: comparações $\\approx n\\lg n - 1{,}26\\,n$', '$n$ de $2^{12}$ a $2^{20}$, média de 5 vetores',
                'Tempo de inserção e merge sort para $n \\le 500$'],
        hipotese=r'''Cada intercalação de $m$ elementos faz entre $m/2$ e $m-1$ comparações; em média, um pouco menos que $m$.
Somando os $\lg n$ níveis, o merge sort faz cerca de $n\lg n - 1{,}26\,n$ comparações em vetores aleatórios.
Para $n$ pequeno, porém, a inserção ($\approx n^2/4$, sem recursão nem cópias) deve ser \textbf{mais rápida}.''',
        metodo=['Contador de comparações entre chaves na intercalação',
                '$n = 2^{12}, 2^{13}, \\dots, 2^{20}$; média de 5 vetores aleatórios',
                'Tempo: 2.000 ordenações por ponto, melhor de 5 lotes',
                '$n$ de 10 a 500 para localizar o cruzamento'],
        graficos=[
            dict(titulo='Comparações do merge sort', ylabel='comparações', escala='log',
                 series=[dict(col='comparacoes', rotulo='medido')],
                 teoria=[dict(col='comparacoes', f='n*log2(n) - 1.2645*n', rotulo='$n\\lg n - 1{,}26n$', ajustar=False, tolerancia=0.01)],
                 leitura=r'Desvio abaixo de 1\% em toda a faixa: a constante 1,26 vem da análise de caso médio da intercalação.'),
            dict(titulo='Para $n$ pequeno, a inserção vence', tabela=1, ylabel='tempo por ordenação ($\\mu$s)',
                 series=[dict(col='insercao_us', rotulo='inserção'), dict(col='merge_us', rotulo='merge sort')],
                 leitura=r'As curvas se cruzam perto de $n \approx 400$ nesta máquina. Abaixo disso, a constante pequena da inserção compensa o $n^2$.'),
        ],
        conclusao=r'''O merge sort faz $n\lg n - 1{,}26\,n$ comparações, com desvio menor que 1\%.
Mas a ordem de crescimento não diz tudo: para $n$ até algumas centenas, a inserção é mais rápida.
\textbf{Algoritmos híbridos} (Timsort, introsort) usam inserção abaixo de um limiar e dividir e conquistar acima dele.''',
        extra=r'Desafio (problema 2-1): use inserção para subvetores com até $k$ elementos e encontre o melhor $k$ na sua máquina.'),
    conexoes=[
        ('\\faDatabase', 'Bancos de dados', 'O \\emph{sort-merge join} ordena duas tabelas pela chave e as intercala. A ordenação externa ordena arquivos maiores que a RAM em blocos e depois os intercala.'),
        ('\\faLayerGroup', 'Armazenamento (LSM-trees)', 'RocksDB, Cassandra e LevelDB escrevem em blocos ordenados e os \\emph{compactam} por intercalação: o \\Nome{Merge} em escala de terabytes.'),
        ('\\faServer', 'Big Data', 'MapReduce e Spark dividem os dados entre máquinas, processam em paralelo e combinam os resultados: o mesmo paradigma, num cluster.'),
        ('\\faMicrochip', 'Computação paralela', 'As duas metades são independentes: o merge sort paraleliza naturalmente em CPUs com vários núcleos e em GPUs.'),
    ],
    exercicios=['(2.3-1) Ilustre o merge sort em $A = \\langle 3, 41, 52, 26, 38, 57, 9, 49\\rangle$.',
                '(2.3-2) Reescreva \\Nome{Merge} sem sentinelas.',
                '(2.3-5) Escreva a busca binária e mostre que seu pior caso é $\\Theta(\\lg n)$.',
                '(Problema 2-1) Implemente o híbrido inserção + merge e meça o melhor limiar $k$.',
                'Implemente o merge sort de baixo para cima (iterativo), como na Figura 2.4.'],
    leitura='Cormen et al., seção 2.3 e problema 2-1.',
)

AULA_05 = dict(
    n=5, bloco=1, tema='Notação assintótica: $O$, $\\Omega$ e $\\Theta$', curto='Notação assintótica',
    cormen='capítulo 3',
    objetivos=['Definir $\\Theta$, $O$, $\\Omega$, $o$ e $\\omega$ e interpretá-las graficamente',
               'Provar relações assintóticas exibindo constantes $c$ e $n_0$',
               'Ordenar funções comuns pela taxa de crescimento',
               'Estimar a ordem de crescimento a partir de medições (log-log e razão de dobra)'],
    roteiro=['Definições, gráficos da Figura 3.1, propriedades e funções comuns',
             'Quanto cabe em 1 segundo para cada $f(n)$',
             'Quatro algoritmos, quatro ordens de crescimento num só gráfico',
             'Ciência de dados, complexidade, bioinformática e SLAs'],
    teoria=[
        dict(titulo='As três notações principais', fig='3.1', altura=0.42, empilhar=True,
             legenda='(a) $\\Theta$: $f$ entre $c_1 g$ e $c_2 g$. (b) $O$: $f$ abaixo de $cg$. (c) $\\Omega$: $f$ acima de $cg$. Sempre a partir de $n_0$.',
             texto=r'''\footnotesize $\Theta(g) = \{f : \exists\, c_1, c_2, n_0 > 0,\ 0 \le c_1 g(n) \le f(n) \le c_2 g(n)\ \forall n \ge n_0\}$\quad
$O(g)$: só o limite superior $f \le c\,g$.\quad $\Omega(g)$: só o limite inferior $f \ge c\,g$.'''),
        dict(titulo='Provando com constantes',
             texto=r'''\textbf{Exemplo:} $\frac12 n^2 - 3n = \Theta(n^2)$.

\medskip Precisamos de $c_1 n^2 \le \frac12 n^2 - 3n \le c_2 n^2$. Dividindo por $n^2$: $c_1 \le \frac12 - \frac3n \le c_2$.
\begin{itemize}\setlength{\itemsep}{3pt}
\item Lado direito: vale para todo $n \ge 1$ com $c_2 = \frac12$.
\item Lado esquerdo: para $n \ge 7$, $\frac12 - \frac37 = \frac1{14}$; basta $c_1 = \frac1{14}$.
\item Logo $c_1 = \frac1{14}$, $c_2 = \frac12$, $n_0 = 7$.
\end{itemize}
\textbf{Contraexemplo:} $6n^3 \ne \Theta(n^2)$: precisaríamos de $6n^3 \le c_2 n^2$, ou seja, $n \le c_2/6$, o que falha para $n$ grande.''',
             rodape=r'\textbf{Teorema 3.1:} $f = \Theta(g)$ se e somente se $f = O(g)$ e $f = \Omega(g)$.'),
        dict(titulo='Notação como ferramenta',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item $O$ no \textbf{pior caso} limita \emph{toda} entrada: ``a inserção é $O(n^2)$''.
\item $\Omega$ no \textbf{melhor caso} limita toda entrada por baixo: ``a inserção é $\Omega(n)$''.
\item ``A inserção é $\Theta(n^2)$'' é falso para toda entrada; vale para o \textbf{pior caso}.
\item $o$ e $\omega$ são limites \textbf{estritos}: $2n = o(n^2)$, mas $2n^2 \ne o(n^2)$. Formalmente, $f = o(g) \iff \lim f/g = 0$.
\item Em equações: $2n^2 + \Theta(n) = \Theta(n^2)$ significa ``alguma função anônima de $\Theta(n)$''.
\end{itemize}''',
             rodape=r'Propriedades: transitividade, reflexividade, simetria ($\Theta$) e simetria transposta ($f = O(g) \iff g = \Omega(f)$).'),
        dict(titulo='A escada das funções comuns',
             texto=r'''\[1 \;\prec\; \lg^* n \;\prec\; \lg\lg n \;\prec\; \lg n \;\prec\; \sqrt n \;\prec\; n \;\prec\; n\lg n \;\prec\; n^2 \;\prec\; n^3 \;\prec\; 2^n \;\prec\; n! \;\prec\; n^n\]
\begin{itemize}\setlength{\itemsep}{4pt}
\item Todo polinômio cresce mais devagar que toda exponencial: $n^b = o(a^n)$ para $a > 1$.
\item Todo polilogaritmo cresce mais devagar que todo polinômio: $\lg^b n = o(n^a)$ para $a > 0$.
\item A base do logaritmo não importa: $\log_a n = \Theta(\log_b n)$.
\item Stirling: $\lg(n!) = \Theta(n\lg n)$, resultado que voltará no limite inferior da ordenação.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Para $10^6$ operações por segundo: qual o maior $n$ para cada $f(n)$?',
                'Busca binária sobre o valor de $n$ (a função é crescente)',
                '\\texttt{tgamma(n+1)} calcula $n!$ para $n$ real'],
        arquivos=[('aula05_crescimento.c', 'Quanto cabe em 1 segundo')]),
    experimento=dict(
        programa='aula05_experimento.c', titulo='Descobrir a ordem de crescimento medindo',
        pergunta='Medindo operações de quatro algoritmos, conseguimos identificar lg n, n, n lg n e n²?',
        resumo=['Busca binária, busca linear, merge sort e todos os pares', '$n$ de 256 a 32.768, dobrando',
                'Em escala log-log, cada ordem é uma reta com inclinação própria'],
        hipotese=r'''Contando a operação básica de cada algoritmo:
busca binária $\approx \lg n$; busca linear (pior caso) $= n$; merge sort $= n\lg n$ (uma cópia por posição e nível);
todos os pares $= n(n-1)/2$.
Em log-log, as inclinações devem ser $\approx 0$, 1, um pouco acima de 1 e 2.''',
        metodo=['Contador global \\texttt{ops} na operação básica de cada algoritmo',
                '$n = 2^8, \\dots, 2^{15}$', 'Busca de um valor ausente (pior caso)',
                'Comparação com a fórmula exata de cada um'],
        graficos=[
            dict(titulo='Quatro ordens de crescimento em log-log', ylabel='operações', escala='log',
                 series=[dict(col='pares', rotulo='todos os pares'), dict(col='mergesort', rotulo='merge sort'),
                         dict(col='linear', rotulo='busca linear'), dict(col='binaria', rotulo='busca binária')],
                 teoria=[dict(col='pares', f='n*(n-1)/2', rotulo='$\\binom{n}{2}$', ajustar=False, tolerancia=0.001),
                         dict(col='mergesort', f='n*log2(n)', rotulo='$n\\lg n$', ajustar=False, tolerancia=0.001),
                         dict(col='linear', f='n', rotulo='$n$', ajustar=False, tolerancia=0.001),
                         dict(col='binaria', f='log2(n)', rotulo='$\\lg n$', ajustar=False, tolerancia=0.001)],
                 leitura=r'Retas paralelas têm a mesma ordem; inclinação maior, ordem maior. A busca binária é quase horizontal.'),
        ],
        conclusao=r'''As contagens batem \textbf{exatamente} com $n(n-1)/2$, $n\lg n$, $n$ e $\lg n$.
Em escala log-log, a ordem de crescimento aparece como inclinação. Para estimar $k$ a partir de duas medições:
$k \approx \lg\big(T(2n)/T(n)\big)$, a razão de dobra da aula 1.'''),
    conexoes=[
        ('\\faChartLine', 'Ciência de dados', 'O $k$-means custa $O(n\\,k\\,d\\,i)$; um algoritmo $O(n^2)$ inviabiliza bases com milhões de linhas. A notação assintótica decide o que escala.'),
        ('\\faInfinity', 'Teoria da complexidade', 'P contra NP pergunta se problemas verificáveis em tempo polinomial também são resolvíveis em tempo polinomial: um dos sete problemas do milênio.'),
        ('\\faDna', 'Bioinformática', 'Alinhar duas sequências custa $\\Theta(mn)$: para genomas de bilhões de bases, isso força heurísticas como BLAST.'),
        ('\\faHandshake', 'Contratos de serviço (SLA)', 'Garantir resposta em 100 ms para qualquer carga exige saber como o tempo cresce com os dados; a ordem de crescimento entra no planejamento de capacidade.'),
    ],
    exercicios=['(3.1-1) Prove que $\\max(f(n), g(n)) = \\Theta(f(n) + g(n))$.',
                '(3.1-2) Prove que $(n + a)^b = \\Theta(n^b)$ para constantes $a$ e $b > 0$.',
                '(3.1-4) $2^{n+1} = O(2^n)$? E $2^{2n} = O(2^n)$?',
                '(Problema 3-3) Ordene 10 funções da lista do livro por taxa de crescimento.',
                'Rode \\texttt{aula05\\_crescimento.c} com $10^9$ operações por segundo e compare com $10^6$.'],
    leitura='Cormen et al., seções 3.1 e 3.2.',
)

AULA_06 = dict(
    n=6, bloco=1, tema='Recorrências: árvore de recursão e teorema mestre', curto='Recorrências',
    cormen='seções 4.3 a 4.5',
    objetivos=['Modelar algoritmos recursivos por recorrências',
               'Resolver recorrências pela árvore de recursão e confirmar por substituição',
               'Aplicar os três casos do teorema mestre',
               'Conferir numericamente as previsões do teorema'],
    roteiro=['Substituição, árvore de recursão, teorema mestre',
             'Avaliar $T(n) = aT(n/b) + n^k$ e classificar o caso',
             'Quatro recorrências medidas contra suas soluções',
             'FFT, multiplicação de matrizes, paralelismo e pilhas de chamada'],
    teoria=[
        dict(titulo='Três métodos',
             texto=r'''\begin{itemize}\setlength{\itemsep}{6pt}
\item \textbf{Substituição:} chute a forma da solução e prove por indução, achando as constantes.
Ex.: $T(n) = 2T(\lfloor n/2\rfloor) + n$. Chute $T(n) \le c\,n\lg n$; então
$T(n) \le 2c\frac n2\lg\frac n2 + n = cn\lg n - cn + n \le cn\lg n$ para $c \ge 1$.
\item \textbf{Árvore de recursão:} desenhe as chamadas, some o custo de cada nível, some os níveis. Ótima para gerar o chute.
\item \textbf{Teorema mestre:} resolve de uma vez $T(n) = aT(n/b) + f(n)$, com $a \ge 1$, $b > 1$.
\end{itemize}''',
             rodape=r'Cuidado na substituição: provar $T(n) \le cn + n$ \textbf{não} prova $T(n) = O(n)$. É preciso a forma exata da hipótese.'),
        dict(titulo='Árvore de recursão de $T(n) = 3T(n/4) + cn^2$', fig='4.5', altura=0.62, empilhar=True,
             legenda='o custo por nível cai em progressão geométrica ($\\frac3{16}$): a raiz domina e $T(n) = \\Theta(n^2)$.'),
        dict(titulo='Árvore desbalanceada: $T(n) = T(n/3) + T(2n/3) + cn$', fig='4.6', altura=0.5,
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Todo nível completo custa $cn$.
\item O caminho mais longo, $n \to \frac23 n \to (\frac23)^2 n \to \dots$, tem $\log_{3/2} n$ níveis.
\item Chute: $O(n\lg n)$, confirmado por substituição.
\end{itemize}''', largura_texto=0.40),
        dict(titulo='O teorema mestre',
             texto=r'''Seja $T(n) = a\,T(n/b) + f(n)$. Compare $f(n)$ com $n^{\log_b a}$ (o custo das folhas):
\begin{enumerate}\setlength{\itemsep}{5pt}
\item Se $f(n) = O(n^{\log_b a - \varepsilon})$: as \textbf{folhas dominam}, $T(n) = \Theta(n^{\log_b a})$.
\item Se $f(n) = \Theta(n^{\log_b a})$: todos os níveis pesam igual, $T(n) = \Theta(n^{\log_b a}\lg n)$.
\item Se $f(n) = \Omega(n^{\log_b a + \varepsilon})$ e $a f(n/b) \le c f(n)$ para algum $c < 1$: a \textbf{raiz domina}, $T(n) = \Theta(f(n))$.
\end{enumerate}
\medskip\footnotesize\begin{tabular}{lccl}\toprule Recorrência & $n^{\log_b a}$ & Caso & Solução\\\midrule
$2T(n/2) + n$ (merge sort) & $n$ & 2 & $\Theta(n\lg n)$\\
$4T(n/2) + n$ & $n^2$ & 1 & $\Theta(n^2)$\\
$T(n/2) + 1$ (busca binária) & $1$ & 2 & $\Theta(\lg n)$\\
$7T(n/2) + n^2$ (Strassen) & $n^{2,81}$ & 1 & $\Theta(n^{\lg 7})$\\\bottomrule\end{tabular}'''),
    ],
    pratica=dict(
        resumo=['Avalia $T(n) = aT(\\lfloor n/b\\rfloor) + n^k$ recursivamente',
                'Calcula $\\log_b a$ e indica o caso do teorema mestre',
                'Testes: casos 1, 2 e 3'],
        arquivos=[('aula06_recorrencias.c', 'Calculando recorrências')]),
    experimento=dict(
        programa='aula06_experimento.c', titulo='O teorema mestre confere?',
        pergunta='Os valores exatos de quatro recorrências seguem as soluções do teorema mestre?',
        resumo=['$2T(n/2)+n$, $4T(n/2)+n$, $T(n/2)+1$, $7T(n/2)+n^2$', '$n = 2^4$ a $2^{24}$',
                'Soluções exatas e ajuste da constante de Strassen'],
        hipotese=r'''Com $T(1) = 1$ e $n$ potência de 2, as soluções exatas são
$2T(n/2)+n = n\lg n + n$, $4T(n/2)+n = 2n^2 - n$ e $T(n/2)+1 = \lg n + 1$.
Para Strassen, o teorema prevê $\Theta(n^{\lg 7})$, com $\lg 7 \approx 2{,}807$.''',
        metodo=['Recorrência avaliada diretamente (uma chamada por nível)',
                '$n = 2^4, \\dots, 2^{24}$',
                'Três soluções comparadas sem ajuste; Strassen com constante ajustada',
                'Gráfico em escala log-log'],
        graficos=[
            dict(titulo='Valores exatos e soluções previstas', ylabel='$T(n)$', escala='log',
                 series=[dict(col='sete', rotulo='$7T(n/2)+n^2$'), dict(col='quatro', rotulo='$4T(n/2)+n$'),
                         dict(col='dois', rotulo='$2T(n/2)+n$'), dict(col='um', rotulo='$T(n/2)+1$')],
                 teoria=[dict(col='sete', f='n**log2(7)', rotulo='$n^{\\lg 7}$', tolerancia=0.01),
                         dict(col='quatro', f='2*n*n - n', rotulo='$2n^2-n$', ajustar=False, tolerancia=0.0001),
                         dict(col='dois', f='n*log2(n) + n', rotulo='$n\\lg n + n$', ajustar=False, tolerancia=0.0001),
                         dict(col='um', f='log2(n) + 1', rotulo='$\\lg n + 1$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Strassen: a razão $T(n)/n^{\lg 7}$ converge para $7/3$. As outras três batem com a solução exata.'),
        ],
        conclusao=r'''As soluções exatas coincidem com os valores calculados, e a de Strassen converge para $\frac73\,n^{\lg 7}$.
O teorema mestre acerta a \textbf{ordem de crescimento}; para a constante, é preciso resolver a recorrência com mais cuidado (substituição ou árvore completa).''',
        extra=r'Desafio: inclua $3T(n/4) + n^2$ (caso 3) e $2T(n/2) + n\lg n$, que cai na lacuna entre os casos 2 e 3.'),
    conexoes=[
        ('\\faWaveSquare', 'Processamento de sinais', 'A FFT satisfaz $T(n) = 2T(n/2) + \\Theta(n)$: $n\\lg n$ em vez de $n^2$ viabiliza áudio digital, 4G/5G, ressonância magnética e compressão JPEG/MP3.'),
        ('\\faTh', 'Álgebra linear e IA', 'Strassen ($n^{2,81}$) e sucessores mostram que multiplicar matrizes, o núcleo das redes neurais, pode custar menos que $n^3$.'),
        ('\\faProjectDiagram', 'Computação paralela', 'Algoritmos paralelos são analisados por duas recorrências: trabalho total e \\emph{span} (caminho crítico). O paralelismo é a razão entre elas.'),
        ('\\faLayerGroup', 'Linguagens e sistemas', 'A profundidade da recursão é a altura da árvore: com $\\lg n$ níveis, a pilha de chamadas fica pequena; com $n$ níveis, ocorre estouro de pilha.'),
    ],
    exercicios=['(4.3-1) Mostre por substituição que $T(n) = T(n-1) + n$ é $O(n^2)$.',
                '(4.4-1) Use a árvore de recursão para estimar $T(n) = 3T(\\lfloor n/2\\rfloor) + n$.',
                '(4.5-1) Aplique o teorema mestre a $2T(n/4) + 1$, $2T(n/4) + \\sqrt n$, $2T(n/4) + n$, $2T(n/4) + n^2$.',
                '(4.5-3) Mostre que a busca binária, $T(n) = T(n/2) + \\Theta(1)$, é $\\Theta(\\lg n)$.',
                'Use \\texttt{aula06\\_recorrencias.c} com $b$ não potência de 2 ($b = 3$) e compare com a previsão.'],
    leitura='Cormen et al., seções 4.3, 4.4 e 4.5.',
)

AULA_07 = dict(
    n=7, bloco=1, tema='Subarranjo máximo: três algoritmos, três ordens', curto='Subarranjo máximo',
    cormen='seção 4.1',
    objetivos=['Reduzir o problema de compra e venda de ações ao subarranjo máximo',
               'Resolver por força bruta, por divisão e conquista e pelo algoritmo linear',
               'Analisar o algoritmo de divisão e conquista pela recorrência $2T(n/2) + \\Theta(n)$',
               'Medir $n^2/2$, $n\\lg n$ e $n$ operações'],
    roteiro=['O problema, a transformação, o subarranjo que cruza o meio',
             'Divisão e conquista em C com o vetor da Figura 4.3',
             'Força bruta, divisão e conquista e Kadane lado a lado',
             'Finanças, bioinformática, visão computacional e séries temporais'],
    teoria=[
        dict(titulo='Comprar barato, vender caro', fig='4.1', altura=0.55,
             legenda='preço de uma ação ao longo de 17 dias e a variação diária.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Escolher o dia de compra e o de venda para maximizar o lucro.
\item Nem sempre o mínimo global vem antes do máximo global.
\item \textbf{Transformação:} olhe as \textbf{variações} diárias $A[i] = \text{preço}_i - \text{preço}_{i-1}$.
\item O lucro de comprar no dia $i-1$ e vender no dia $j$ é $A[i] + \dots + A[j]$.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='O subarranjo máximo', fig='4.3', altura=0.25, empilhar=True,
             legenda='o subarranjo $A[8..11]$ tem a maior soma: 43.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Força bruta: testar os $\binom{n}{2} + n$ pares $(i, j)$, com somas acumuladas: $\Theta(n^2)$.
\item Só faz sentido se há valores negativos; se todos são positivos, a resposta é o vetor inteiro.
\item Divisão e conquista: o melhor subarranjo está \textbf{à esquerda} do meio, \textbf{à direita} ou \textbf{cruzando} o meio.
\end{itemize}'''),
        dict(titulo='O subarranjo que cruza o meio', fig='4.4', altura=0.32, empilhar=True,
             legenda='(a) as três posições possíveis. (b) quem cruza o meio é um sufixo de $A[\\mathit{low}..\\mathit{mid}]$ mais um prefixo de $A[\\mathit{mid}+1..\\mathit{high}]$.',
             texto=r'''O subarranjo que cruza é \textbf{melhor sufixo da esquerda} + \textbf{melhor prefixo da direita}: dois laços simples, $\Theta(n)$ no total.
É isso que torna a etapa de combinação linear.'''),
        dict(titulo='Divisão e conquista', nome='Max-Subarranjo($A, \\mathit{lo}, \\mathit{hi}$)',
             pseudo=r'''\If{$\mathit{hi} = \mathit{lo}$} \State \Return $(\mathit{lo}, \mathit{hi}, A[\mathit{lo}])$ \Comment{caso base}
\Else
\State $\mathit{mid} \atrib \lfloor(\mathit{lo} + \mathit{hi})/2\rfloor$
\State $(e_i, e_f, e_s) \atrib$ \Nome{Max-Subarranjo}($A, \mathit{lo}, \mathit{mid}$)
\State $(d_i, d_f, d_s) \atrib$ \Nome{Max-Subarranjo}($A, \mathit{mid}{+}1, \mathit{hi}$)
\State $(c_i, c_f, c_s) \atrib$ \Nome{Max-Cruzando}($A, \mathit{lo}, \mathit{mid}, \mathit{hi}$)
\If{$e_s \ge d_s$ \textbf{e} $e_s \ge c_s$} \State \Return $(e_i, e_f, e_s)$
\ElsIf{$d_s \ge e_s$ \textbf{e} $d_s \ge c_s$} \State \Return $(d_i, d_f, d_s)$
\Else \State \Return $(c_i, c_f, c_s)$
\EndIf
\EndIf''',
             texto=r'''\[T(n) = 2T(n/2) + \Theta(n)\]
A mesma recorrência do merge sort: caso 2 do teorema mestre, $\Theta(n\lg n)$.

\medskip\begin{destaque}[cteoria]\textbf{Exercício 4.1-5:} existe solução $\Theta(n)$. Guarde o melhor subarranjo que \emph{termina} em $j$: ou é $A[j]$ sozinho, ou é o melhor que termina em $j-1$ mais $A[j]$ (algoritmo de Kadane).\end{destaque}''', largura_texto=0.36),
    ],
    pratica=dict(
        resumo=['Função que devolve início, fim e soma (um \\texttt{struct})', 'Dois laços para o subarranjo que cruza o meio',
                'Teste com o vetor da Figura 4.3: soma 43 em $A[8..11]$'],
        arquivos=[('aula07_subarranjo.c', 'Subarranjo máximo por divisão e conquista')]),
    experimento=dict(
        programa='aula07_experimento.c', titulo='$n^2$, $n\\lg n$ ou $n$?',
        pergunta='Quantas somas fazem a força bruta, a divisão e conquista e o algoritmo de Kadane?',
        resumo=['Mesma resposta, custos muito diferentes', '$n = 256$ a $16.384$, valores em $[-100, 100]$',
                'O programa aborta se os três discordarem'],
        hipotese=r'''Contando somas de elementos:
força bruta $= n(n+1)/2$; divisão e conquista $= n\lg n$ (cada nível da recursão percorre o vetor uma vez);
Kadane $= n$. Os três devem dar a \textbf{mesma} soma máxima.''',
        metodo=['Vetores aleatórios com valores entre $-100$ e $100$', '$n = 2^8, \\dots, 2^{14}$',
                'Contador \\texttt{ops} em cada soma', 'Verificação cruzada das três respostas'],
        graficos=[
            dict(titulo='Três algoritmos, mesma resposta', ylabel='somas', escala='log',
                 series=[dict(col='forca_bruta', rotulo='força bruta'), dict(col='divisao', rotulo='divisão e conquista'),
                         dict(col='kadane', rotulo='Kadane')],
                 teoria=[dict(col='forca_bruta', f='n*(n+1)/2', rotulo='$\\frac{n(n+1)}{2}$', ajustar=False, tolerancia=0.0001),
                         dict(col='divisao', f='n*log2(n)', rotulo='$n\\lg n$', ajustar=False, tolerancia=0.0001),
                         dict(col='kadane', f='n', rotulo='$n$', ajustar=False, tolerancia=0.0001)],
                 leitura=r'Para $n = 16.384$: 134 milhões de somas na força bruta, 229 mil na divisão e conquista, 16 mil no Kadane.'),
        ],
        conclusao=r'''As contagens são \textbf{exatamente} $n(n+1)/2$, $n\lg n$ e $n$, e as três respostas coincidem em todos os testes.
Divisão e conquista melhora muito a força bruta, mas uma ideia melhor (programação dinâmica, aula 33) chega a $\Theta(n)$:
\textbf{nenhum paradigma é a última palavra}.'''),
    conexoes=[
        ('\\faChartLine', 'Finanças', 'Melhor janela de compra e venda, maior sequência de lucro ou de perda (\\emph{drawdown}) numa carteira: o problema desta aula com dados reais.'),
        ('\\faDna', 'Bioinformática', 'Atribuindo pesos a aminoácidos ou nucleotídeos, o segmento de soma máxima localiza regiões transmembranares em proteínas e ilhas CpG no DNA.'),
        ('\\faImage', 'Visão computacional', 'A versão 2D, o retângulo de soma máxima, encontra a região mais clara ou mais ``ativa'' de uma imagem em $O(n^3)$, com Kadane nas colunas.'),
        ('\\faHeartbeat', 'Monitoramento', 'Em séries temporais (CPU, batimentos, tráfego), subtrair a média e achar o subarranjo máximo localiza a janela de maior anomalia.'),
    ],
    exercicios=['(4.1-1) O que \\Nome{Max-Subarranjo} devolve se todos os elementos são negativos?',
                '(4.1-2) Escreva a força bruta e prove que é $\\Theta(n^2)$.',
                '(4.1-3) Implemente as duas versões e ache o $n_0$ em que a divisão e conquista passa a vencer.',
                '(4.1-5) Implemente o algoritmo linear e prove sua corretude com um invariante.',
                'Aplique o algoritmo às variações diárias de uma ação real (dados abertos da B3) e diga quando comprar e vender.'],
    leitura='Cormen et al., seção 4.1.',
)

AULA_08 = dict(
    n=8, bloco=1, tema='Heaps e heapsort', curto='Heapsort',
    cormen='capítulo 6 (seções 6.1 a 6.4)',
    objetivos=['Representar uma árvore binária quase completa em um vetor',
               'Manter a propriedade de heap com \\Nome{Max-Heapify}',
               'Mostrar que \\Nome{Build-Max-Heap} é $O(n)$, não $O(n\\lg n)$',
               'Medir comparações: $\\approx 2n$ na construção, $\\approx 2n\\lg n$ no heapsort'],
    roteiro=['Heap em vetor, \\Nome{Max-Heapify}, construção linear, heapsort',
             'Heapsort em C com índices a partir de 0',
             'Contar comparações da construção e da ordenação',
             'Sistemas operacionais, simulação, embarcados e jogos'],
    teoria=[
        dict(titulo='Um heap é uma árvore dentro de um vetor', fig='6.1', altura=0.48,
             legenda='(a) heap de máximo com 10 elementos; (b) o mesmo heap no vetor.',
             texto=r'''\begin{itemize}\setlength{\itemsep}{4pt}
\item Árvore binária \textbf{quase completa}: todos os níveis cheios, exceto talvez o último, preenchido da esquerda.
\item Pai de $i$: $\lfloor i/2\rfloor$; filhos: $2i$ e $2i+1$. Sem ponteiros.
\item \textbf{Propriedade de heap de máximo:} $A[\text{pai}(i)] \ge A[i]$. A raiz é o maior.
\item Altura: $\lfloor\lg n\rfloor$.
\end{itemize}''', largura_texto=0.42),
        dict(titulo='Mantendo a propriedade', nome='Max-Heapify($A, i$)',
             pseudo=r'''\State $l \atrib 2i$;\quad $r \atrib 2i + 1$
\If{$l \le A.\mathit{tamanho}$ \textbf{e} $A[l] > A[i]$} \State $\mathit{maior} \atrib l$
\Else \State $\mathit{maior} \atrib i$ \EndIf
\If{$r \le A.\mathit{tamanho}$ \textbf{e} $A[r] > A[\mathit{maior}]$} \State $\mathit{maior} \atrib r$ \EndIf
\If{$\mathit{maior} \ne i$}
\State troque $A[i]$ com $A[\mathit{maior}]$
\State \Nome{Max-Heapify}($A, \mathit{maior}$)
\EndIf''',
             fig='6.2', legenda='\\Nome{Max-Heapify}($A$, 2): o 4 desce até o lugar certo.', altura=0.42,
             texto=r'''Supõe que as subárvores de $i$ já são heaps. O elemento $A[i]$ ``desce'' trocando com o maior filho.

\medskip Custo: $O(h)$ = $O(\lg n)$. Pela recorrência, $T(n) \le T(2n/3) + \Theta(1)$.''', largura_texto=0.30),
        dict(titulo='Construir um heap custa $O(n)$', fig='6.3', altura=0.62,
             legenda='\\Nome{Build-Max-Heap} das últimas posições internas para a raiz.',
             texto=r'''\Nome{Build-Max-Heap}: para $i = \lfloor n/2\rfloor$ \textbf{descendo até} 1, \Nome{Max-Heapify}($A, i$).

\medskip Análise ingênua: $n/2$ chamadas $\times\ O(\lg n)$ = $O(n\lg n)$. Mas a maioria dos nós é baixa:
\[\sum_{h=0}^{\lfloor\lg n\rfloor} \left\lceil \frac{n}{2^{h+1}}\right\rceil O(h) = O\Big(n\sum_{h\ge0}\frac{h}{2^h}\Big) = O(2n) = O(n)\]''', largura_texto=0.48),
        dict(titulo='Heapsort', nome='Heapsort($A$)',
             pseudo=r'''\State \Nome{Build-Max-Heap}($A$)
\For{$i \atrib A.\mathit{comprimento}$ \textbf{descendo até} 2}
\State troque $A[1]$ com $A[i]$
\State $A.\mathit{tamanho} \atrib A.\mathit{tamanho} - 1$
\State \Nome{Max-Heapify}($A, 1$)
\EndFor''',
             fig='6.4', legenda='o máximo vai para o fim; o heap encolhe.', altura=0.55,
             texto=r'''$O(n) + (n-1)\cdot O(\lg n) = O(n\lg n)$, \textbf{no lugar} (sem vetor auxiliar), mas \textbf{não estável}.''', largura_texto=0.30),
    ],
    pratica=dict(
        resumo=['Índices de 0: filhos em $2i+1$ e $2i+2$', '\\Nome{Max-Heapify} recursivo, construção e ordenação',
                'Teste com o heap da Figura 6.1'],
        arquivos=[('aula08_heapsort.c', 'Heapsort em C')]),
    experimento=dict(
        programa='aula08_experimento.c', titulo='Construção linear, ordenação $n\\lg n$',
        pergunta='Construir um heap faz O(n) comparações e o heapsort faz cerca de 2 n lg n?',
        resumo=['Construção: $\\le 2n$ comparações', 'Heapsort completo: $\\approx 2n\\lg n$',
                '$n = 2^{12}$ a $2^{21}$, média de 3 vetores'],
        hipotese=r'''\Nome{Max-Heapify} faz até 2 comparações por nível descido. Como $\sum h/2^h = 2$, a \textbf{construção} faz no máximo cerca de $2n$ comparações: linear.
Cada uma das $n-1$ extrações desce até $\lg n$ níveis: o heapsort faz cerca de $2n\lg n$ comparações.''',
        metodo=['\\Nome{Max-Heapify} iterativo com contador de comparações',
                '$n = 2^{12}, \\dots, 2^{21}$; média de 3 vetores aleatórios',
                'Construção e ordenação medidas separadamente',
                'Ajuste de $c \\cdot n$ e $c \\cdot n\\lg n$'],
        graficos=[
            dict(titulo='Construir o heap é linear', ylabel='comparações',
                 series=[dict(col='construcao', rotulo='\\Nome{Build-Max-Heap}')],
                 teoria=[dict(col='construcao', f='n', rotulo='$n$', tolerancia=0.01)],
                 leitura=r'A constante fica perto de 1,88: abaixo do limite 2 da análise, porque nem todo nó desce até as folhas.'),
            dict(titulo='Heapsort completo', ylabel='comparações', escala='log',
                 series=[dict(col='heapsort', rotulo='heapsort')],
                 teoria=[dict(col='heapsort', f='n*log2(n)', rotulo='$n\\lg n$', tolerancia=0.04)],
                 leitura=r'Constante perto de 1,8: cada extração desce quase até o fundo, com 2 comparações por nível.'),
        ],
        conclusao=r'''A construção é \textbf{linear} (cerca de $1{,}9\,n$ comparações), confirmando que a análise ingênua $O(n\lg n)$ era pessimista.
O heapsort completo fica perto de $1{,}8\,n\lg n$: o dobro de comparações do merge sort, mas \textbf{no lugar}, sem memória extra.''',
        extra=r'Desafio: o heapsort com \emph{descida até a folha} (Floyd) reduz as comparações para perto de $n\lg n$. Implemente e meça.'),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'Temporizadores do kernel, filas de prioridade de processos e o temporizador do runtime de Go usam heaps para achar o próximo evento em $O(\\lg n)$.'),
        ('\\faNetworkWired', 'Simulação de redes', 'Simuladores de eventos discretos (ns-3, OMNeT++) mantêm uma fila de eventos ordenada por tempo: extrair o próximo é \\Nome{Extract-Min}.'),
        ('\\faMicrochip', 'Sistemas embarcados', 'Heapsort garante $O(n\\lg n)$ sem memória extra nem recursão profunda; o \\texttt{std::sort} do C++ (introsort) recorre a ele quando o quicksort degenera.'),
        ('\\faRoute', 'Jogos e mapas', 'Dijkstra e A*, usados em GPS e na movimentação de personagens, dependem de uma fila de prioridade em heap (aulas 17 e 31).'),
    ],
    exercicios=['(6.1-1) Quais o mínimo e o máximo de elementos num heap de altura $h$?',
                '(6.2-1) Ilustre \\Nome{Max-Heapify}($A$, 3) em $A = \\langle 27,17,3,16,13,10,1,5,7,12,4,8,9,0\\rangle$.',
                '(6.3-1) Ilustre \\Nome{Build-Max-Heap} em $A = \\langle 5,3,17,10,84,19,6,22,9\\rangle$.',
                '(6.4-3) Qual o tempo do heapsort num vetor já ordenado? E em ordem decrescente? Meça.',
                'Escreva \\Nome{Max-Heapify} iterativo e explique por que ele evita a pilha de chamadas.'],
    leitura='Cormen et al., seções 6.1 a 6.4.',
)

PROJETO_1 = dict(
    n=9, bloco=1, tipo='projeto', tema='Projeto 1: laboratório de ordenação',
    descricao='Apresentação dos projetos do Bloco 1. Cada equipe implementa, instrumenta e compara algoritmos de ordenação, e confronta as medições com a teoria.',
    entregas=['Implementação em C de inserção, merge sort, heapsort e um híbrido (inserção abaixo de um limiar $k$)',
              'Experimento com $n$ até $10^6$ em quatro tipos de entrada: aleatória, ordenada, invertida e quase ordenada (1% fora do lugar)',
              'Gráficos de comparações e de tempo com as curvas teóricas ajustadas e a razão medido/teórico',
              'O melhor limiar $k$ do híbrido na máquina da equipe, com justificativa',
              'Apresentação de 10 minutos: hipótese, método, resultados, o que não bateu com a teoria e por quê'],
)

AULAS_B1 = [AULA_01, AULA_02, AULA_03, AULA_04, AULA_05, AULA_06, AULA_07, AULA_08, PROJETO_1]
