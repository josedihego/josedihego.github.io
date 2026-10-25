"""Base Prática em C (anexo, antes do bloco 1): memória, ponteiros, structs, funções e arquivos.
Não repete o básico de C (tipos, laços, vetores, funções simples): parte do que o curso de estruturas exige."""

KR = 'Kernighan e Ritchie, \\emph{C: a linguagem de programação}'

BASE_1 = dict(
    n='B1', id='base1', rotulo='Base 1', bloco=0, tema='Memória: pilha, heap e alocação dinâmica', curto='Memória',
    fonte=KR + ', seções 5.4 e 8.7; Cormen et al., seção 10.3', cormen='',
    objetivos=['Distinguir a pilha (variáveis locais) do heap (alocação dinâmica)',
               'Usar \\texttt{malloc}, \\texttt{calloc}, \\texttt{realloc} e \\texttt{free} corretamente',
               'Reconhecer vazamentos, ponteiros soltos e liberações duplas',
               'Medir quanto um \\texttt{malloc} pequeno custa em bytes e em tempo'],
    roteiro=['O mapa da memória de um processo e as quatro funções de alocação',
             'Vetor no heap, \\texttt{calloc} e crescimento com \\texttt{realloc}',
             'Bytes e nanossegundos por \\texttt{malloc} de 16 bytes',
             'Sistemas operacionais, segurança, linguagens e sistemas embarcados'],
    teoria=[
        dict(titulo='O mapa da memória de um processo',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.46\textwidth}
\begin{itemize}\setlength{\itemsep}{4pt}
\item \textbf{Código} e \textbf{dados estáticos}: o programa e as variáveis globais.
\item \textbf{Heap}: cresce para cima; é de onde vem o \texttt{malloc}. A memória fica até o \texttt{free}.
\item \textbf{Pilha}: cresce para baixo; guarda variáveis locais e endereços de retorno. Some quando a função retorna.
\end{itemize}\end{column}\begin{column}{0.48\textwidth}
\begin{tikzpicture}[x=1cm,y=0.62cm,font=\footnotesize]
\foreach \y/\t/\c in {0/código/csurface,1/dados estáticos (globais)/csurface,2/heap $\uparrow$/cpratica!20,4/livre/white,5/pilha $\downarrow$/cteoria!20}
  \filldraw[fill=\c,draw=cmuted] (0,\y) rectangle (4.2,\y+1) node[midway] {\t};
\filldraw[fill=white,draw=cmuted] (0,3) rectangle (4.2,4) node[midway] {\dots};
\node[anchor=west,text=cmuted] at (4.3,0.2) {endereços baixos};
\node[anchor=west,text=cmuted] at (4.3,5.8) {endereços altos};
\end{tikzpicture}\end{column}\end{columns}''',
             rodape=r'Estruturas de dados que crescem (listas, árvores, tabelas) vivem no heap: o tamanho só é conhecido durante a execução.'),
        dict(titulo='As quatro funções',
             texto=r'''\renewcommand{\arraystretch}{1.35}\begin{tabular}{ll}\toprule \textbf{Chamada} & \textbf{O que faz}\\\midrule
\texttt{p = malloc(n * sizeof *p)} & reserva $n$ elementos, conteúdo indefinido; \texttt{NULL} se falhar\\
\texttt{p = calloc(n, sizeof *p)} & reserva e \textbf{zera}\\
\texttt{q = realloc(p, m * sizeof *p)} & muda o tamanho, preservando o conteúdo (pode mudar o endereço)\\
\texttt{free(p)} & devolve a memória; \texttt{p} continua apontando para lá (``solto'')\\\bottomrule\end{tabular}

\medskip\begin{itemize}\setlength{\itemsep}{3pt}
\item \texttt{sizeof *p} em vez de \texttt{sizeof(int)}: continua certo se o tipo de \texttt{p} mudar.
\item Nunca \texttt{p = realloc(p, \dots)}: se falhar, o \texttt{NULL} sobrescreve o único ponteiro para o bloco antigo.
\end{itemize}'''),
        dict(titulo='Os erros clássicos',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \textbf{Vazamento}: perder o último ponteiro para um bloco sem chamar \texttt{free}. O programa cresce até acabar a memória.
\item \textbf{Ponteiro solto} (\emph{dangling}): usar um bloco depois do \texttt{free}, ou o endereço de uma variável local depois que a função retornou.
\item \textbf{Liberação dupla}: \texttt{free} duas vezes no mesmo bloco corrompe o alocador.
\item \textbf{Estouro}: escrever além do tamanho pedido (\texttt{v[n]} num vetor de $n$).
\end{itemize}
\medskip Ferramentas: \texttt{valgrind ./prog} aponta vazamentos e acessos inválidos; \texttt{gcc -fsanitize=address} faz o mesmo ao executar.''',
             rodape=r'Cerca de 70\% das falhas de segurança graves em produtos da Microsoft e do Chrome vêm desses erros de memória.'),
    ],
    pratica=dict(
        resumo=['Por que não devolver o endereço de uma local', 'Vetor no heap, \\texttt{calloc} que zera',
                '\\texttt{realloc} seguro com ponteiro temporário'],
        arquivos=[('base1_memoria.c', 'Alocação dinâmica em C')]),
    experimento=dict(
        programa='base1_experimento.c', titulo='O preço de um \\texttt{malloc} pequeno',
        pergunta='Quantos bytes de heap e quantos nanossegundos custa cada malloc de 16 bytes?',
        resumo=['$n$ blocos de 16 bytes, $n$ de 4 mil a 4 milhões', 'Bytes em uso medidos com \\texttt{mallinfo2}',
                'Tempo por \\texttt{malloc}'],
        hipotese=r'''Cada bloco do alocador do glibc carrega um \textbf{cabeçalho} (8 bytes) e é alinhado a 16 bytes: um pedido de 16 bytes deve ocupar 32.
O custo deve ser \textbf{constante} por bloco, em bytes e em tempo: alocar um milhão de nós de lista custa o dobro da memória dos dados.''',
        metodo=['\\texttt{mallinfo2().uordblks}: bytes do heap em uso, antes e depois', '$n = 2^{12}, \\dots, 2^{22}$ blocos',
                'Tempo total das $n$ chamadas dividido por $n$', 'Todos os blocos liberados a cada rodada'],
        graficos=[
            dict(titulo='Bytes por bloco de 16 bytes', ylabel='bytes por bloco', escala='logx', opcoes='ymin=0,ymax=40',
                 series=[dict(col='bytes_por_bloco', rotulo='medido')],
                 teoria=[dict(col='bytes_por_bloco', f='1', rotulo='constante', tolerancia=0.01)],
                 leitura=r'Exatamente 32 bytes: 16 de dados, 8 de cabeçalho e 8 de alinhamento.'),
            dict(titulo='Tempo por \\texttt{malloc}', ylabel='ns por chamada', escala='logx', opcoes='ymin=0',
                 series=[dict(col='ns_por_malloc', rotulo='medido')],
                 leitura=r'Dezenas de nanossegundos: 50 a 100 vezes o custo de uma soma. Alocar um nó por elemento tem preço.'),
        ],
        conclusao=r'''Cada \texttt{malloc} de 16 bytes ocupa \textbf{32 bytes} e custa dezenas de nanossegundos. Uma lista ligada de inteiros gasta muito mais memória e tempo que um vetor com os mesmos dados.
É por isso que estruturas de alto desempenho alocam em blocos (\emph{pools}) e por isso a aula 16 mostra listas guardadas em vetores.'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', '\\texttt{malloc} pede páginas ao kernel com \\texttt{brk} e \\texttt{mmap}; a memória virtual e a paginação ficam por trás de cada ponteiro.'),
        ('\\faShieldAlt', 'Segurança', 'Estouros de buffer e uso após \\texttt{free} são as falhas mais exploradas da história; linguagens como Rust impedem esses erros já na compilação.'),
        ('\\faRecycle', 'Linguagens com coleta de lixo', 'Java, Python e Go liberam a memória sozinhas (coletor de lixo); C dá controle total, e a responsabilidade junto.'),
        ('\\faMicrochip', 'Sistemas embarcados', 'Em microcontroladores com poucos KB, o heap fragmenta: por isso o padrão MISRA C proíbe \\texttt{malloc} depois da inicialização.'),
    ],
    exercicios=['Escreva \\texttt{int *copia(const int *v, int n)} que devolve uma cópia de \\texttt{v} no heap.',
                'Rode \\texttt{base1\\_memoria.c} com \\texttt{valgrind} e depois remova um \\texttt{free}. O que ele relata?',
                'Leia números até o fim da entrada num vetor que cresce com \\texttt{realloc} (dobrando).',
                'Repita o experimento com blocos de 8, 24, 32 e 100 bytes e tabele os bytes realmente usados.',
                'Compile com \\texttt{-fsanitize=address} um programa que acessa \\texttt{v[n]} e leia a mensagem.'],
    leitura=KR + ', seções 5.4 e 8.7 (alocador); Cormen et al., seção 10.3.',
)

BASE_2 = dict(
    n='B2', id='base2', rotulo='Base 2', bloco=0, tema='Ponteiros: endereços, aritmética e ponteiro para ponteiro', curto='Ponteiros',
    fonte=KR + ', capítulo 5; Cormen et al., seção 10.3', cormen='',
    objetivos=['Usar \\texttt{\\&} e \\texttt{*} e entender o que um ponteiro guarda',
               'Relacionar vetores e ponteiros pela aritmética de ponteiros',
               'Passar parâmetros por referência e alterar um ponteiro dentro de uma função (\\texttt{int **})',
               'Alocar matrizes dinâmicas e medir o efeito da ordem de percurso'],
    roteiro=['Endereços, aritmética, vetores, referência e ponteiro duplo',
             'Troca por referência, matriz dinâmica e vetor alocado via \\texttt{int **}',
             'Percorrer uma matriz por linhas ou por colunas',
             'Sistemas operacionais, compiladores, hardware e bancos de dados'],
    teoria=[
        dict(titulo='Endereços e indireção',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Toda variável mora num \textbf{endereço}. \texttt{\&x} é o endereço de \texttt{x}; um ponteiro é uma variável que guarda um endereço.
\item \texttt{int *p = \&x;} \quad então \texttt{*p} \textbf{é} \texttt{x}: ler e escrever \texttt{*p} lê e escreve \texttt{x}.
\item \texttt{NULL}: ``não aponta para nada''. Desreferenciar \texttt{NULL} derruba o programa (\emph{segmentation fault}).
\item C passa tudo \textbf{por valor}: para uma função alterar \texttt{x}, ela recebe \texttt{\&x} (\texttt{void troca(int *a, int *b)}).
\end{itemize}''',
             rodape=r'No Cormen, ``$x.\mathit{prox}$'' é um ponteiro; ``\textsc{nil}'' é \texttt{NULL}. Toda estrutura ligada do curso é feita disto.'),
        dict(titulo='Vetores e aritmética de ponteiros',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item O nome de um vetor é o endereço do primeiro elemento: \texttt{v == \&v[0]}.
\item \texttt{p + i} anda $i$ \textbf{elementos} (não bytes): \texttt{*(p + i)} é \texttt{p[i]}.
\item \texttt{p2 - p1} dá quantos elementos há entre dois ponteiros do mesmo vetor.
\item Ao passar um vetor para uma função, passa-se só o endereço: a função não sabe o tamanho; passe \texttt{n} junto.
\end{itemize}
\medskip\begin{tabular}{lll}\toprule \textbf{Expressão} & \textbf{Tipo} & \textbf{Significado}\\\midrule
\texttt{v[i]}, \texttt{*(v+i)} & \texttt{int} & o elemento $i$\\
\texttt{\&v[i]}, \texttt{v+i} & \texttt{int *} & o endereço dele\\
\texttt{m[i][j]} & \texttt{int} & com \texttt{int **m}: \texttt{*(*(m+i)+j)}\\\bottomrule\end{tabular}'''),
        dict(titulo='Ponteiro para ponteiro',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \textbf{Alterar um ponteiro do chamador}: se \texttt{aloca(int *p)} faz \texttt{p = malloc(...)}, o chamador nunca vê. É preciso \texttt{void aloca(int **p)} e \texttt{*p = malloc(...)}, chamada como \texttt{aloca(\&v)}.
\item \textbf{Matriz dinâmica}: \texttt{int **m} é um vetor de ponteiros para linhas. Alocar as linhas num bloco contíguo (\texttt{m[i] = m[0] + i*col}) torna a matriz amiga do cache.
\item \textbf{Inserir no início de uma lista sem cabeçalho}: \texttt{insere(No **cabeca, int k)} pode mudar a cabeça.
\item Em C, uma matriz é guardada \textbf{linha por linha} (\emph{row-major}): \texttt{m[i][j]} e \texttt{m[i][j+1]} são vizinhos na memória; \texttt{m[i+1][j]}, não.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['\\texttt{troca} por referência', 'Matriz dinâmica com um bloco contíguo', '\\texttt{aloca\\_vetor(int **p, n)} altera o ponteiro do chamador'],
        arquivos=[('base2_ponteiros.c', 'Ponteiros em C')]),
    experimento=dict(
        programa='base2_experimento.c', titulo='Linhas ou colunas?',
        pergunta='Percorrer uma matriz por linhas e por colunas custa o mesmo tempo por elemento?',
        resumo=['Matriz $n \\times n$ de inteiros, $n$ de 256 a 4.096', 'Mesma soma, duas ordens de percurso', 'Tempo por elemento, melhor de 3'],
        hipotese=r'''No modelo RAM, as duas ordens fazem as mesmas $n^2$ somas: o mesmo tempo.
Na máquina real, a matriz está guardada por linhas: percorrer por linhas lê endereços vizinhos (aproveita cada linha de cache de 64 bytes); por colunas, salta $4n$ bytes a cada acesso. Esperamos linhas com custo \textbf{constante} e colunas cada vez piores.''',
        metodo=['Matriz em bloco contíguo (\\texttt{m[i] = m[0] + i*n})', '$n = 256, 512, \\dots, 4096$ (até 64 MB)',
                'Mínimo de 3 repetições', 'Tempo dividido por $n^2$'],
        graficos=[
            dict(titulo='Tempo por elemento', ylabel='ns por elemento', escala='log',
                 series=[dict(col='colunas_ns', rotulo='por colunas'), dict(col='linhas_ns', rotulo='por linhas')],
                 teoria=[dict(col='linhas_ns', f='1', rotulo='constante', tolerancia=0.3)],
                 leitura=r'Por linhas: cerca de 0,3 ns, constante. Por colunas: de 1 ns a 10 ns quando a matriz deixa de caber no cache.'),
        ],
        conclusao=r'''A mesma conta, na ordem errada, fica \textbf{30 vezes} mais lenta para $n = 4096$. Ponteiros dão acesso direto à memória, e a memória tem geografia: vizinhos são baratos, saltos são caros.
Nas próximas aulas, a mesma lição aparece em listas ligadas (aula 14) e em grafos (aula 29).'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'O kernel manipula páginas, processos e dispositivos por ponteiros; um ponteiro inválido no kernel derruba a máquina inteira.'),
        ('\\faCogs', 'Compiladores', 'Otimizadores trocam a ordem de laços (\\emph{loop interchange}) para percorrer matrizes por linhas; a análise de \\emph{aliasing} decide se dois ponteiros podem se sobrepor.'),
        ('\\faMicrochip', 'Hardware e GPUs', 'Bibliotecas de álgebra linear (BLAS) e GPUs dividem matrizes em blocos que cabem no cache: o mesmo efeito do experimento, explorado ao máximo.'),
        ('\\faDatabase', 'Bancos de dados', 'Bancos orientados a linhas (OLTP) e a colunas (OLAP, como DuckDB) são as duas ordens do experimento: cada um vence num tipo de consulta.'),
    ],
    exercicios=['Escreva \\texttt{void minmax(const int *v, int n, int *mn, int *mx)} que devolve mínimo e máximo pelos ponteiros.',
                'Implemente \\texttt{strlen} só com aritmética de ponteiros (sem índices).',
                'Escreva \\texttt{int **le\\_matriz(int *lin, int *col)} que lê as dimensões e os valores e devolve a matriz.',
                'Implemente a inserção na cabeça de uma lista com \\texttt{void insere(No **cabeca, int k)}.',
                'Transponha uma matriz $n \\times n$ ``no lugar'' e meça o tempo: o acesso por colunas aparece de novo?'],
    leitura=KR + ', capítulo 5 (ponteiros e vetores).',
)

BASE_3 = dict(
    n='B3', id='base3', rotulo='Base 3', bloco=0, tema='Structs: registros, ponteiros para structs e nós', curto='Structs',
    fonte=KR + ', capítulo 6; Cormen et al., seção 10.3', cormen='',
    objetivos=['Declarar structs com \\texttt{typedef} e acessar campos com \\texttt{.} e \\texttt{->}',
               'Construir vetores de structs e structs autorreferentes (nós)',
               'Entender alinhamento e preenchimento (\\texttt{sizeof}, \\texttt{offsetof})',
               'Medir vetor de structs (AoS) contra struct de vetores (SoA)'],
    roteiro=['Registros, \\texttt{->}, structs dentro de structs, nós e alinhamento',
             'Turma de alunos: vetor de structs e lista de nós',
             'Somar um campo: AoS contra SoA',
             'Redes, sistemas de arquivos, jogos e ciência de dados'],
    teoria=[
        dict(titulo='Registros',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Uma \texttt{struct} agrupa campos de tipos diferentes: os ``dados satélite'' do Cormen ficam juntos da chave.
\item \texttt{typedef struct \{ char nome[32]; double nota; \} Aluno;} cria o tipo \texttt{Aluno}.
\item \texttt{a.nota} acessa o campo; com um ponteiro, \texttt{p->nota} é o mesmo que \texttt{(*p).nota}.
\item Atribuir uma struct a outra copia \textbf{todos} os bytes; passar por valor também. Para structs grandes, passe \texttt{const Aluno *}.
\item Structs podem conter vetores, outras structs e ponteiros.
\end{itemize}'''),
        dict(titulo='O nó: uma struct que aponta para si mesma',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \texttt{typedef struct No \{ int chave; struct No *prox; \} No;}
\item Dentro da declaração, o nome \texttt{No} do \texttt{typedef} ainda não existe: por isso \texttt{struct No *}.
\item Uma struct não pode conter a si mesma (tamanho infinito), mas pode conter um \textbf{ponteiro} para si.
\item Todo nó do curso é assim: listas (\texttt{prox}, \texttt{ant}), árvores (\texttt{esq}, \texttt{dir}, \texttt{pai}), grafos (listas de adjacência).
\item Criar: \texttt{No *x = malloc(sizeof *x); x->chave = k; x->prox = NULL;}
\end{itemize}''',
             rodape=r'No Cormen, $x.\mathit{chave}$ e $x.\mathit{prox}$ são exatamente \texttt{x->chave} e \texttt{x->prox} quando $x$ é um ponteiro para nó.'),
        dict(titulo='Alinhamento e preenchimento',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.5\textwidth}
\begin{itemize}\setlength{\itemsep}{4pt}
\item O processador lê um \texttt{int} mais rápido (ou só consegue ler) num endereço múltiplo de 4.
\item O compilador insere \textbf{buracos} entre os campos e no fim.
\item \texttt{struct \{ char a; int b; char c; \}}: 12 bytes. Reordenada como \texttt{\{ int b; char a; char c; \}}: 8 bytes.
\item \texttt{offsetof(T, campo)} dá a posição do campo.
\end{itemize}\end{column}\begin{column}{0.46\textwidth}
\begin{tikzpicture}[x=0.5cm,y=0.62cm,font=\footnotesize]
\foreach \i/\c/\t in {0/cteoria!30/a,1/csurface/,2/csurface/,3/csurface/,4/cpratica!30/b,5/cpratica!30/,6/cpratica!30/,7/cpratica!30/,8/cexperimento!30/c,9/csurface/,10/csurface/,11/csurface/}
  \filldraw[fill=\c,draw=cmuted] (\i,1.4) rectangle +(1,1) node[midway]{\t};
\node[anchor=west] at (0,0.9) {12 bytes (cinza = preenchimento)};
\foreach \i/\c/\t in {0/cpratica!30/b,1/cpratica!30/,2/cpratica!30/,3/cpratica!30/,4/cteoria!30/a,5/cexperimento!30/c,6/csurface/,7/csurface/}
  \filldraw[fill=\c,draw=cmuted] (\i,-1) rectangle +(1,1) node[midway]{\t};
\node[anchor=west] at (0,-1.5) {8 bytes};
\end{tikzpicture}\end{column}\end{columns}''',
             rodape=r'Num milhão de registros, 4 bytes a menos por registro são 4 MB a menos para o cache carregar.'),
    ],
    pratica=dict(
        resumo=['Vetor de structs no heap e a melhor nota', 'Lista de nós com uma struct dentro do nó',
                '\\texttt{sizeof} e \\texttt{offsetof} das duas ordens de campos'],
        arquivos=[('base3_structs.c', 'Structs em C')]),
    experimento=dict(
        programa='base3_experimento.c', titulo='Vetor de structs ou struct de vetores?',
        pergunta='Somar um único campo de n registros custa o mesmo num vetor de structs (AoS) e num vetor só com aquele campo (SoA)?',
        resumo=['Registro de 64 bytes; soma do campo \\texttt{nota} (8 bytes)', 'AoS: \\texttt{aos[i].nota}; SoA: \\texttt{notas[i]}',
                '$n$ de 4 mil a 8 milhões de registros'],
        hipotese=r'''No modelo RAM, os dois fazem $n$ somas. Mas cada linha de cache traz 64 bytes: no AoS, só 8 deles são a nota (1/8 aproveitado); no SoA, todos.
Enquanto tudo cabe no cache, empate; depois, o AoS deve ficar várias vezes mais lento, e o SoA, constante.''',
        metodo=['Registro: \\texttt{double nota; char nome[48]; int idade, turma;} (64 bytes)', 'Cerca de 33 milhões de leituras por medida',
                'Tempo por registro', '$n = 2^{12}, \\dots, 2^{23}$'],
        graficos=[
            dict(titulo='Tempo por registro', ylabel='ns por registro', escala='logx', opcoes='ymin=0',
                 series=[dict(col='aos_ns', rotulo='vetor de structs (AoS)'), dict(col='soa_ns', rotulo='struct de vetores (SoA)')],
                 teoria=[dict(col='soa_ns', f='1', rotulo='constante', tolerancia=0.3)],
                 leitura=r'Até cerca de 100 mil registros (6 MB), empate. Fora do cache, o AoS fica cerca de 5 vezes mais lento; o SoA quase não muda.'),
        ],
        conclusao=r'''A organização dos dados na memória muda o desempenho em \textbf{5 vezes}, com o mesmo algoritmo. Agrupar em structs é o natural para programar; separar em vetores é o natural para o hardware.
Bancos colunares, motores de jogos e bibliotecas de ciência de dados escolhem SoA pelo mesmo motivo.'''),
    conexoes=[
        ('\\faNetworkWired', 'Redes', 'Cabeçalhos IP, TCP e Ethernet são structs com campos em posições fixas; o preenchimento errado corrompe pacotes (\\texttt{\\_\\_attribute\\_\\_((packed))}).'),
        ('\\faHdd', 'Sistemas de arquivos', 'O \\emph{inode} do Linux e as entradas de diretório são structs gravadas no disco byte a byte.'),
        ('\\faGamepad', 'Motores de jogos', 'Arquiteturas \\emph{entity component system} guardam cada componente (posição, velocidade) num vetor próprio: SoA para atualizar milhões de objetos por quadro.'),
        ('\\faChartBar', 'Ciência de dados', 'NumPy, pandas e Apache Arrow guardam cada coluna num vetor contíguo: é o SoA do experimento, e a razão de serem tão rápidos.'),
    ],
    exercicios=['Defina \\texttt{Ponto} e \\texttt{Retangulo} (dois pontos) e escreva \\texttt{double area(const Retangulo *r)}.',
                'Ordene um vetor de \\texttt{Aluno} por nota com \\texttt{qsort} (veja Base 4).',
                'Use \\texttt{offsetof} para imprimir a posição de cada campo de uma struct com \\texttt{char}, \\texttt{double} e \\texttt{short}.',
                'Implemente uma pilha de \\texttt{Aluno} com nós (\\texttt{struct No \\{ Aluno dado; struct No *prox; \\}}).',
                'Reduza o registro do experimento para 16 bytes. A diferença entre AoS e SoA diminui? Por quê?'],
    leitura=KR + ', capítulo 6 (estruturas).',
)

BASE_4 = dict(
    n='B4', id='base4', rotulo='Base 4', bloco=0, tema='Funções: recursão, ponteiros para funções e código genérico', curto='Funções',
    fonte=KR + ', seções 4.10, 5.11 e B.5', cormen='',
    objetivos=['Entender a pilha de chamadas e o custo de memória da recursão',
               'Declarar e usar ponteiros para funções',
               'Escrever código genérico com \\texttt{void *} e \\texttt{qsort}',
               'Medir os bytes de pilha por chamada e as comparações do \\texttt{qsort}'],
    roteiro=['Quadros de pilha, ponteiros para funções, \\texttt{void *} e \\texttt{qsort}',
             'Comparadores, tabela de funções, troca genérica e fatorial',
             'Pilha por chamada recursiva; chamadas do comparador',
             'Sistemas operacionais, interfaces gráficas, bibliotecas e IA'],
    teoria=[
        dict(titulo='A pilha de chamadas',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item Cada chamada empilha um \textbf{quadro} (\emph{stack frame}): parâmetros, variáveis locais, endereço de retorno.
\item Na recursão, há um quadro \textbf{por nível}: \texttt{fatorial(10000)} tem 10.000 quadros vivos ao mesmo tempo.
\item A pilha é pequena (8 MB no Linux, por padrão): recursão de profundidade $n$ com $n$ de milhões causa \emph{stack overflow}.
\item Recursão de profundidade $O(\lg n)$ (merge sort, busca binária, árvores balanceadas) é segura; de profundidade $O(n)$ (quicksort no pior caso, DFS) pede cuidado.
\end{itemize}''',
             rodape=r'Por isso o quicksort do complemento 1 recorre no lado menor, e a DFS da aula 29 usa uma pilha explícita.'),
        dict(titulo='Ponteiros para funções',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item O nome de uma função é o endereço do seu código: pode ir para uma variável.
\item \texttt{int (*cmp)(const void *, const void *) = crescente;} \quad depois, \texttt{cmp(\&a, \&b)}.
\item Com \texttt{typedef int (*Comparador)(const void *, const void *);} a declaração fica legível.
\item Usos: \textbf{callbacks} (o \texttt{qsort} chama a sua função de comparação), \textbf{tabelas de despacho} (\texttt{op[k](x, y)}), estratégias trocáveis.
\end{itemize}''',
             rodape=r'É assim que se escreve ``uma ordenação que ordena qualquer coisa'': o algoritmo é fixo, a comparação é um parâmetro.'),
        dict(titulo='Código genérico com \\texttt{void *}',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \texttt{void *} é ``ponteiro para qualquer coisa''; não pode ser desreferenciado sem conversão.
\item \texttt{qsort(base, n, tamanho, cmp)} ordena $n$ elementos de \texttt{tamanho} bytes: não sabe o tipo, só chama \texttt{cmp}.
\item Dentro do comparador: \texttt{int x = *(const int *)a;}.
\item \texttt{memcpy(destino, origem, bytes)} copia qualquer tipo: com ela se escreve uma troca genérica.
\item Cuidado: o compilador já não confere os tipos. Um comparador de \texttt{double} usado num vetor de \texttt{int} compila e dá lixo.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Comparadores crescente e decrescente para o \\texttt{qsort}', 'Tabela de ponteiros para funções',
                'Troca genérica com \\texttt{memcpy} e fatorial recursivo'],
        arquivos=[('base4_funcoes.c', 'Funções e ponteiros para funções')]),
    experimento=dict(
        programa='base4_experimento.c', titulo='Recursão e callbacks, medidos',
        pergunta='Quantos bytes de pilha cada chamada recursiva usa? Quantas vezes o qsort chama o comparador?',
        resumo=['Recursão de profundidade $n$: endereço da local mais funda', 'Contador dentro do comparador do \\texttt{qsort}',
                '$n$ até 16 mil (pilha) e até um milhão (\\texttt{qsort})'],
        hipotese=r'''Cada nível da recursão ocupa um quadro de tamanho fixo: a pilha usada deve ser \textbf{exatamente linear} em $n$.
O \texttt{qsort} do glibc é, na verdade, um merge sort: deve chamar o comparador $\approx n\lg n - 1{,}26\,n$ vezes, como o merge sort da aula 4.''',
        metodo=['Função recursiva com 40 bytes de locais (\\texttt{noinline})', 'Pilha = endereço inicial $-$ endereço mais fundo',
                '\\texttt{qsort} de $n$ inteiros aleatórios', 'Contagem exata'],
        graficos=[
            dict(titulo='Bytes de pilha na recursão', ylabel='bytes', xlabel='profundidade $n$',
                 series=[dict(col='bytes_pilha', rotulo='medido')],
                 teoria=[dict(col='bytes_pilha', f='n', rotulo='$n$', tolerancia=0.001)],
                 leitura=r'Uma reta perfeita: o coeficiente é o tamanho do quadro (64 bytes neste compilador). Com 8 MB de pilha, cabem cerca de 130 mil níveis.'),
            dict(titulo='Chamadas do comparador', tabela=1, ylabel='chamadas', escala='log',
                 series=[dict(col='chamadas', rotulo='medido')],
                 teoria=[dict(col='chamadas', f='n*log2(n) - 1.2645*n', rotulo='$n\\lg n - 1{,}26n$', ajustar=False, tolerancia=0.01)],
                 leitura=r'Exatamente a fórmula do merge sort da aula 4: o \texttt{qsort} do glibc intercala.'),
        ],
        conclusao=r'''A pilha cresce exatamente em linha reta com a profundidade (um quadro de tamanho fixo por chamada), e o \texttt{qsort} chama o comparador $n\lg n - 1{,}26\,n$ vezes: a fórmula do merge sort.
Medir revela o que a biblioteca faz por dentro: o nome diz ``quick'', mas o comportamento é de merge sort.'''),
    conexoes=[
        ('\\faDesktop', 'Sistemas operacionais', 'Tratadores de sinais e de interrupções, \\texttt{pthread\\_create} e os drivers de dispositivo (\\texttt{struct file\\_operations}) são tabelas de ponteiros para funções.'),
        ('\\faMousePointer', 'Interfaces gráficas', 'Botões e eventos chamam funções registradas (\\emph{callbacks}): GTK, o DOM do navegador e o Android funcionam assim.'),
        ('\\faCode', 'Programação orientada a objetos', 'Métodos virtuais do C++ são ponteiros para funções numa tabela (\\emph{vtable}); o mesmo padrão aparece no kernel escrito em C.'),
        ('\\faBrain', 'Inteligência artificial', 'Funções de ativação, de perda e otimizadores são passados como parâmetros: um treinador genérico recebe ``qual função usar''.'),
    ],
    exercicios=['Escreva um comparador que ordene \\texttt{Aluno} por nota decrescente e, no empate, por nome.',
                'Implemente \\texttt{void aplica(int *v, int n, int (*f)(int))} que substitui cada elemento por \\texttt{f(v[i])}.',
                'Faça uma calculadora com uma tabela \\texttt{double (*op[4])(double, double)} indexada pelo operador.',
                'Escreva \\texttt{void *busca\\_linear(void *base, size\\_t n, size\\_t tam, const void *chave, Comparador cmp)}.',
                'Descubra, aumentando $n$, a profundidade em que a recursão do experimento estoura a pilha. Bate com 8 MB / 64 bytes?'],
    leitura=KR + ', seções 4.10 (recursão), 5.11 (ponteiros para funções) e B.5 (\\texttt{qsort}).',
)

BASE_5 = dict(
    n='B5', id='base5', rotulo='Base 5', bloco=0, tema='Arquivos, argumentos e erros', curto='Arquivos e erros',
    fonte=KR + ', capítulo 7 e seção 5.10', cormen='',
    objetivos=['Ler e escrever arquivos texto e binários',
               'Receber parâmetros pela linha de comando (\\texttt{argc}, \\texttt{argv})',
               'Tratar erros com valores de retorno, \\texttt{perror} e \\texttt{assert}',
               'Medir o tamanho e o tempo de arquivos texto contra binários'],
    roteiro=['\\texttt{FILE *}, modos de abertura, texto contra binário, \\texttt{argc}/\\texttt{argv}, erros',
             'Gravar e reler números em texto e em binário',
             'Bytes e nanossegundos por número nos dois formatos',
             'Bancos de dados, redes, ciência de dados e ferramentas de linha de comando'],
    teoria=[
        dict(titulo='Arquivos em C',
             texto=r'''\renewcommand{\arraystretch}{1.3}\begin{tabular}{ll}\toprule \textbf{Chamada} & \textbf{Uso}\\\midrule
\texttt{FILE *f = fopen("x.txt", "r")} & abre; modos \texttt{"r"}, \texttt{"w"}, \texttt{"a"}, e \texttt{"rb"}/\texttt{"wb"} para binário\\
\texttt{fprintf(f, ...)}, \texttt{fscanf(f, ...)} & texto formatado (como \texttt{printf}/\texttt{scanf})\\
\texttt{fgets(s, tam, f)} & uma linha inteira, com limite de tamanho\\
\texttt{fwrite(v, tam, n, f)}, \texttt{fread(...)} & bytes da memória, sem conversão\\
\texttt{fseek}, \texttt{ftell} & posicionar e consultar a posição\\
\texttt{fclose(f)} & fecha e grava o que estava no buffer\\\bottomrule\end{tabular}

\medskip \texttt{stdin}, \texttt{stdout} e \texttt{stderr} são \texttt{FILE *} já abertos: \texttt{./prog < entrada.txt > saida.csv} redireciona sem mudar o código.'''),
        dict(titulo='Texto ou binário?',
             texto=r'''\begin{columns}[T,onlytextwidth]\begin{column}{0.48\textwidth}
\begin{cartao}{cteoria}\textbf{Texto}\par\footnotesize
\begin{itemize}\item Legível e portável (CSV, JSON).\item Converter número $\leftrightarrow$ dígitos custa caro.\item Tamanho variável: 123456 ocupa 7 bytes com o \texttt{\textbackslash n}.\end{itemize}\end{cartao}
\end{column}\begin{column}{0.48\textwidth}
\begin{cartao}{cpratica}\textbf{Binário}\par\footnotesize
\begin{itemize}\item Os bytes da memória, como estão: \texttt{fwrite} de um vetor inteiro de uma vez.\item Rápido e de tamanho fixo (4 bytes por \texttt{int}).\item Depende da máquina (tamanho dos tipos, ordem dos bytes).\end{itemize}\end{cartao}
\end{column}\end{columns}''',
             rodape=r'Os experimentos do curso imprimem CSV em texto: lento, mas qualquer ferramenta (planilha, Python, o gerador destes slides) consegue ler.'),
        dict(titulo='Argumentos e erros',
             texto=r'''\begin{itemize}\setlength{\itemsep}{5pt}
\item \texttt{int main(int argc, char *argv[])}: \texttt{argv[0]} é o nome do programa, \texttt{argv[1]} o primeiro argumento. Ex.: \texttt{./ordena 1000000 aleatorio}.
\item \texttt{atoi}, \texttt{strtol}: de texto para número (\texttt{strtol} detecta erros).
\item \textbf{Toda} chamada de E/S pode falhar: \texttt{fopen} devolve \texttt{NULL}, \texttt{fscanf} devolve quantos itens leu. Teste sempre.
\item \texttt{perror("x.txt")} imprime o motivo (``No such file or directory'') a partir de \texttt{errno}.
\item \texttt{assert(cond)} aborta se \texttt{cond} for falsa: para erros \textbf{de programação}, não para entrada do usuário. Some com \texttt{-DNDEBUG}.
\item Devolva \texttt{0} de \texttt{main} em caso de sucesso e outro valor em caso de erro: scripts e o \texttt{make} dependem disso.
\end{itemize}'''),
    ],
    pratica=dict(
        resumo=['Nome do arquivo opcional em \\texttt{argv[1]}', 'Grava em texto e em binário; relê e confere',
                '\\texttt{perror}, \\texttt{assert} e tamanho com \\texttt{fseek}/\\texttt{ftell}'],
        arquivos=[('base5_arquivos.c', 'Arquivos e erros em C')]),
    experimento=dict(
        programa='base5_experimento.c', titulo='Texto contra binário',
        pergunta='Quantos bytes e quantos nanossegundos custa cada número gravado e relido em texto e em binário?',
        resumo=['$n$ inteiros de 0 a 999.999', 'Tamanho dos dois arquivos', 'Tempo de gravar e reler, por número'],
        hipotese=r'''O binário ocupa \textbf{exatamente} $4n$ bytes. O texto ocupa em média $\approx 6{,}9$ bytes por número (quase todos têm 6 dígitos, mais o \texttt{\textbackslash n}).
O tempo do texto deve ser bem maior: \texttt{fprintf} e \texttt{fscanf} convertem dígitos um a um; \texttt{fwrite} e \texttt{fread} copiam blocos.''',
        metodo=['$n = 2^{14}, \\dots, 2^{21}$ números aleatórios', 'Gravação e leitura completas em cada formato',
                'Tamanho com \\texttt{fseek}/\\texttt{ftell}', 'Tempo por número'],
        graficos=[
            dict(titulo='Tamanho dos arquivos', ylabel='bytes', escala='log',
                 series=[dict(col='bytes_texto', rotulo='texto'), dict(col='bytes_binario', rotulo='binário')],
                 teoria=[dict(col='bytes_binario', f='4*n', rotulo='$4n$', ajustar=False, tolerancia=0.0001),
                         dict(col='bytes_texto', f='n', rotulo='$n$', tolerancia=0.01)],
                 leitura=r'Binário: exatamente $4n$. Texto: cerca de $6{,}9\,n$, 72\% maior.'),
            dict(titulo='Tempo por número', ylabel='ns por número', escala='log',
                 series=[dict(col='texto_ns', rotulo='texto'), dict(col='binario_ns', rotulo='binário')],
                 teoria=[dict(col='texto_ns', f='1', rotulo='constante', tolerancia=0.3),
                         dict(col='binario_ns', f='1', rotulo='constante', tolerancia=0.3)],
                 leitura=r'Os dois são lineares (custo constante por número), mas o texto custa cerca de 85 ns e o binário, 2,5 ns: 35 vezes mais.'),
        ],
        conclusao=r'''Os dois formatos são lineares, mas com constantes muito diferentes: o texto é \textbf{72\% maior} e \textbf{35 vezes mais lento}. O binário é exatamente $4n$ bytes.
Por isso bancos de dados, imagens e modelos de IA são guardados em binário, e dados para trocar com pessoas e outras ferramentas, em texto.'''),
    conexoes=[
        ('\\faDatabase', 'Bancos de dados', 'Tabelas e índices ficam em arquivos binários de páginas de tamanho fixo (4 a 16 KB); \\texttt{fseek} para a página $k$ é \\texttt{k * tamanho}.'),
        ('\\faNetworkWired', 'Redes', 'Protocolos binários (TCP/IP, gRPC/Protobuf) são compactos e rápidos; protocolos de texto (HTTP/1.1, JSON) são legíveis. A escolha é a mesma do experimento.'),
        ('\\faChartBar', 'Ciência de dados', 'CSV é universal, mas Parquet e Arrow (binários e colunares) são até dezenas de vezes menores e mais rápidos para grandes volumes.'),
        ('\\faTerminal', 'Ferramentas de linha de comando', '\\texttt{grep}, \\texttt{sort} e \\texttt{gcc} leem \\texttt{argv}, leem \\texttt{stdin}, escrevem \\texttt{stdout} e devolvem um código de saída: é o que permite encadeá-los com \\texttt{|}.'),
    ],
    exercicios=['Leia um CSV \\texttt{nome,nota} com \\texttt{fgets} e \\texttt{sscanf} e imprima a média.',
                'Faça \\texttt{./gera N tipo} que imprime $N$ números (aleatório, ordenado ou invertido): use-o nos experimentos de ordenação.',
                'Grave um vetor de \\texttt{Aluno} em binário e leia o $k$-ésimo registro com \\texttt{fseek}, sem ler os anteriores.',
                'Abra um arquivo inexistente e mostre a mensagem do \\texttt{perror}; depois trate o erro sem abortar.',
                'No experimento, grave com \\texttt{fprintf} para \\texttt{/dev/null}: quanto do tempo é conversão e quanto é disco?'],
    leitura=KR + ', capítulo 7 (entrada e saída) e seção 5.10 (argumentos).',
)

AULAS_BASE = [BASE_1, BASE_2, BASE_3, BASE_4, BASE_5]
