"""Course plan for /logica/ (Lógica de Programação – Superior): 3 blocks, 36 classes.
Each content class: the theme, the question solved in class and the one proposed (ids from questoes.json), plus the
material of the slide deck. Markup in the texts: `code` and **bold**.
mesa = desk-check: C snippet run by the generator; each MESA(...) line prints one table row and is hidden on the slide."""

BLOCOS = [
    {'n': 1, 'titulo': 'Sequência, aritmética e decisão',
     'resumo': 'Entrada e saída, tipos, `/` e `%`, dígitos, bases, `if`/`else`, `switch` e bits. Termina com a Avaliação I.'},
    {'n': 2, 'titulo': 'Repetição, funções e vetores',
     'resumo': '`while` e `for`, acumuladores, laços aninhados, funções, vetores, janelas e simulação. Termina com a Avaliação II.'},
    {'n': 3, 'titulo': 'Strings, matrizes e structs',
     'resumo': 'Strings e a tabela ASCII, vetores de contagem, matrizes, simulação em grade e `struct`. Termina com a Avaliação III e a Reavaliação.'},
]

AULAS = [
    # ---------------------------------------------------------------- Bloco 1
    dict(n=1, tema='Primeiro programa: entrada, fórmula e saída',
         objetivo='Escrever um programa completo que lê dados, aplica uma fórmula da prova e imprime o resultado formatado.',
         resolvida='A1-2014.2-QI', proposta='A1-2024.2-QI',
         conceitos=['Esqueleto de todo programa: `#include <stdio.h>`, `int main(void) { ... return 0; }`',
                    '`int` guarda inteiros; `double` guarda reais. Na dúvida numa fórmula, use `double`',
                    'Leitura: `%d` para `int`, `%lf` para `double`. Impressão: `%d` e `%f` (`%.2f` = 2 casas)',
                    '`scanf` precisa do `&` antes da variável: ele recebe o **endereço** onde guardar',
                    'Cada fórmula do enunciado vira uma linha `variavel = expressão;`'],
         padrao='''#include <stdio.h>

int main(void) {
    double a, b;                      // 1. declarar
    printf("Digite a e b: ");
    scanf("%lf %lf", &a, &b);         // 2. ler (com &)
    double r = a * b;                 // 3. calcular
    printf("Resultado: %.4f\\n", r);  // 4. imprimir
    return 0;
}''',
         erros=[('scanf("%d", x);', 'scanf("%d", &x);', 'sem `&` o programa escreve num endereço qualquer'),
                ('scanf("%f", &d); /* double */', 'scanf("%lf", &d);', '`double` se lê com `%lf`'),
                ('int m = (a + b) / 2;', 'double m = (a + b) / 2.0;', 'inteiro / inteiro descarta a fração'),
                ('printf("%d", 2.5);', 'printf("%.1f", 2.5);', 'o formato tem que bater com o tipo')],
         mesa=dict(cab=['linha', 'pa', 'pb', 'ambos', 'algum'], codigo='''double pa = 0.5, pb = 0.4, ambos = 0, algum = 0;
MESA("1 & %.2f & %.2f & -- & --", pa, pb);
ambos = pa * pb;
MESA("2 & %.2f & %.2f & %.2f & --", pa, pb, ambos);
algum = pa + pb - ambos;
MESA("3 & %.2f & %.2f & %.2f & %.2f", pa, pb, ambos, algum);'''),
         passos=['Dados: P(A) e P(B), dois `double` lidos com `%lf`',
                 'Duas fórmulas, na ordem: primeiro P(A e B), depois P(A ou B), que usa a primeira',
                 'Saída com casas fixas (`%.4f`) para conferir com a calculadora'],
         dica=['Círculo inscrito: o lado do quadrado é o diâmetro, `2 * r`',
               'Área sombreada = área do quadrado − área do círculo',
               'Use π = 3,14 como manda o enunciado (`#define PI 3.14`) e `double`']),
    dict(n=2, tema='Aritmética em C: divisão inteira, resto e conversões',
         objetivo='Usar `/`, `%` e a conversão para `double` para transformar unidades sem erros de truncamento.',
         resolvida='A1-2014.2-QII', proposta='A1-2012.2-QII',
         conceitos=['`7 / 2` vale `3` (divisão inteira); `7 % 2` vale `1` (resto)',
                    'Basta um operando real para a conta ser real: `7 / 2.0` vale `3.5`',
                    'Conversão de unidades: total = maior × fator + menor (ex.: minutos = h × 60 + min)',
                    'Volta: `h = total / 60` e `min = total % 60`',
                    'Cast explícito: `(double)soma / n`'],
         padrao='''int h1, m1, h2, m2;
scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);  // lê 13:30 15:10
int ini = h1 * 60 + m1;                     // tudo em minutos
int fim = h2 * 60 + m2;
int dur = fim - ini;
printf("%d:%02d\\n", dur / 60, dur % 60);    // volta para h:min''',
         erros=[('double x = 30 / 60;', 'double x = 30 / 60.0;', '`30 / 60` é `0` antes de virar `double`'),
                ('printf("%d:%d", h, m); /* 1:5 */', 'printf("%d:%02d", h, m);', '`%02d` completa com zero: `1:05`'),
                ('m = total / 60 % 60; /* ? */', 'h = total / 60; m = total % 60;', 'escreva uma conversão por linha')],
         mesa=dict(cab=['expressão', 'valor'], codigo='''int g = 30, m = 15, s = 50;
MESA("\\\\texttt{m / 60} & %d", m / 60);
MESA("\\\\texttt{m / 60.0} & %.4f", m / 60.0);
MESA("\\\\texttt{s / 3600.0} & %.4f", s / 3600.0);
MESA("\\\\texttt{g + m / 60.0 + s / 3600.0} & %.4f", g + m / 60.0 + s / 3600.0);
MESA("\\\\texttt{100 \\\\%% 60} & %d", 100 % 60);'''),
         passos=['Entradas inteiras: graus, minutos, segundos',
                 '1 grau = 60 minutos = 3600 segundos',
                 'Dividir por `60.0` e `3600.0` (reais!) e somar aos graus'],
         dica=['Converta início e fim para minutos desde 0:00',
               'Se o fim for menor que o início, a aula passou da meia-noite: some 24 × 60',
               'Volte para horas e minutos com `/ 60` e `% 60`']),
    dict(n=3, tema='Extraindo dígitos com / e %',
         objetivo='Separar os dígitos de um número com divisões por 10 e usar o resto para contas circulares.',
         resolvida='A1-2015.2-QI', proposta='A1-2026.2-QIa',
         conceitos=['`n % 10` é o último dígito; `n / 10` remove o último dígito',
                    'Dígito da posição k (da direita, começando em 0): `(n / 10^k) % 10`',
                    'O resto também serve para "dar a volta": posição circular = `(inicio + passos) % tamanho`',
                    'Teste com um número em que todos os dígitos são diferentes, ex.: 1234'],
         padrao='''int n = 4721;
int unidade = n % 10;          // 1
int dezena  = (n / 10) % 10;   // 2
int centena = (n / 100) % 10;  // 7
int milhar  = n / 1000;        // 4''',
         erros=[('d = n / 10 % 100;', 'd = (n / 10) % 10;', 'o resto por 10 isola **um** dígito'),
                ('pos = inicio + passos;', 'pos = (inicio + passos) % tam;', 'sem `%` a posição sai da pista'),
                ('/* testar só com 1111 */', '/* testar com 1234 */', 'dígitos iguais escondem a troca de posição')],
         mesa=dict(cab=['n', 'n \\% 10', 'n / 10'], codigo='''int n = 4721;
while (n > 0) {
    MESA("%d & %d & %d", n, n % 10, n / 10);
    n = n / 10;
}'''),
         passos=['Número de 4 dígitos: os centrais são o 2º e o 3º',
                 '2º dígito: `(n / 100) % 10`; 3º dígito: `(n / 10) % 10`',
                 'Somar e imprimir'],
         dica=['Quantas voltas completas não importam: só o resto',
               'Distância da partida = treino % comprimento da pista',
               'Faça o teste de mesa com uma distância maior que a pista']),
    dict(n=4, tema='Bases numéricas: octal e binário',
         objetivo='Converter entre bases usando dígitos e potências, validando a entrada.',
         resolvida='A1-2012.2-QI', proposta='A1-2018.2-QI',
         conceitos=['Na base b, o número d₂d₁d₀ vale `d2*b*b + d1*b + d0`',
                    'Octal só tem dígitos de 0 a 7: valide cada dígito antes de converter',
                    'Para obter os dígitos binários de n: `n % 2`, depois `n = n / 2`, e repita',
                    'Os dígitos saem do menos significativo para o mais significativo'],
         padrao='''int n = 157;                 // lido como "octal"
int d2 = n / 100, d1 = (n / 10) % 10, d0 = n % 10;
if (d2 > 7 || d1 > 7 || d0 > 7)
    printf("inválido\\n");
else
    printf("%d\\n", d2 * 64 + d1 * 8 + d0);   // 111''',
         erros=[('dec = d2 * 100 + d1 * 10 + d0;', 'dec = d2 * 64 + d1 * 8 + d0;', 'os pesos são potências da base'),
                ('/* não valida dígito 8 ou 9 */', 'if (d0 > 7) ...', 'a prova cobra a validação'),
                ('printf("%o", n);', '/* faça a conta */', 'usar formato pronto não demonstra o algoritmo')],
         mesa=dict(cab=['n', 'n \\% 2', 'uns'], codigo='''int n = 13, uns = 0;
while (n > 0) {
    uns += n % 2;
    MESA("%d & %d & %d", n, n % 2, uns);
    n = n / 2;
}'''),
         passos=['Separar os 3 dígitos com `/` e `%`',
                 'Validar: entre 0 e 777 e todos os dígitos ≤ 7',
                 'Aplicar os pesos 64, 8 e 1'],
         dica=['O número vai de 0 a 32: no máximo 6 dígitos binários',
               'Cada `n % 2` é um bit; some os bits iguais a 1',
               'Sem laço: repita o par `n % 2` / `n / 2` seis vezes (ou adiante-se com `while`)']),
    dict(n=5, tema='Decisão: if/else e operadores lógicos',
         objetivo='Traduzir condições do enunciado em expressões com `&&`, `||` e `!`.',
         resolvida='A1-2014.2-QIII', proposta='A1-2015.2-QI-B',
         conceitos=['Comparação: `==` (igual), `!=`, `<`, `<=`, `>`, `>=`',
                    '`&&` (e): todas verdadeiras; `||` (ou): basta uma; `!` nega',
                    'Faixas de valores: `if ... else if ... else` em ordem, do menor para o maior',
                    'Sempre use chaves `{ }` quando o bloco tiver mais de uma linha'],
         padrao='''if (salario <= 1000) {
    desconto = salario * 0.08;
} else if (salario <= 2000) {
    desconto = salario * 0.09;
} else {
    desconto = 2000 * 0.11;      // teto
}''',
         erros=[('if (x = 0)', 'if (x == 0)', '`=` atribui; `==` compara'),
                ('if (0 < x < 10)', 'if (x > 0 && x < 10)', 'em C a comparação dupla não funciona'),
                ('if (x > 5); { ... }', 'if (x > 5) { ... }', 'o `;` encerra o `if` vazio'),
                ('if (a < b + c || b < a + c)', 'if (a < b + c && b < a + c ...)', 'as três condições valem ao mesmo tempo')],
         mesa=dict(cab=['a, b, c', 'a<b+c', 'b<a+c', 'c<a+b', 'triângulo?'], codigo='''int t[3][3] = {{3, 4, 5}, {1, 2, 3}, {2, 2, 9}};
for (int i = 0; i < 3; i++) {
    int a = t[i][0], b = t[i][1], c = t[i][2];
    MESA("%d, %d, %d & %d & %d & %d & %s", a, b, c, a < b + c, b < a + c, c < a + b, (a < b + c && b < a + c && c < a + b) ? "sim" : "não");
}'''),
         passos=['Desigualdade triangular: cada lado menor que a soma dos outros dois',
                 'As três condições juntas com `&&`',
                 'Testar um caso degenerado: 1, 2, 3 (não forma)'],
         dica=['Desconto = 11% do salário',
               'Teto: `if (desconto > TETO) desconto = TETO;`',
               'Teste um salário baixo e um bem alto (que bate no teto)']),
    dict(n=6, tema='Decisões encadeadas e arredondamento',
         objetivo='Escolher um valor por faixa ou categoria e arredondar para cima com `ceil`.',
         resolvida='A1-2015.2-QIII-B', proposta='A1-2026.2-QIb',
         conceitos=['Categoria → valor: `if (c == 1) v = ...; else if (c == 2) ...`',
                    '`ceil(x)` (de `<math.h>`) arredonda para cima: `ceil(2.1)` = 3',
                    'Compile com `-lm` quando usar `<math.h>` no Linux',
                    'Trate a categoria inválida no `else` final'],
         padrao='''#include <math.h>
double potencia = area * watts_m2;
int lampadas = (int)ceil(potencia / 60);  // nunca falta luz''',
         erros=[('int q = potencia / 60;', 'int q = (int)ceil(potencia / 60);', 'truncar deixa o cômodo escuro'),
                ('ceil(450 / 60)', 'ceil(450 / 60.0)', 'a divisão inteira acontece antes do `ceil`'),
                ('/* sem else final */', 'else printf("inválido");', 'entrada fora das opções')],
         mesa=dict(cab=['potência', 'potência/60', 'truncado', 'ceil'], codigo='''double p[3] = {360, 450, 600};
for (int i = 0; i < 3; i++)
    MESA("%.0f & %.2f & %d & %.0f", p[i], p[i] / 60, (int)(p[i] / 60), ceil(p[i] / 60));'''),
         passos=['Classe do cômodo → potência por m² (12, 15 ou 20 W)',
                 'Potência total = largura × comprimento × W/m²',
                 'Lâmpadas = `ceil(total / 60)`'],
         dica=['Pontuação = soma das duas cartas; iguais dobra, consecutivas (`abs(a - b) == 1`) triplica',
               'Calcule a pontuação de cada jogadora numa variável',
               'Compare: Lia, Mia ou empate (teste o empate de propósito)']),
    dict(n=7, tema='Comparações em vários níveis',
         objetivo='Decidir comparando critérios em ordem de prioridade (anos, depois meses, depois dias).',
         resolvida='A1-2015.2-QIV', proposta='A1-2017.1-QIII',
         conceitos=['Compare o critério mais importante; só se empatar, passe ao próximo',
                    'Truque: guardar a diferença e trocar de critério se ela for 0',
                    'Três saídas possíveis: maior, menor, igual. Teste as três',
                    'Alternativa: converter tudo para uma unidade (dias) e comparar uma vez'],
         padrao='''int dif = a1 - a2;          // anos
if (dif == 0) dif = m1 - m2; // empate: meses
if (dif == 0) dif = d1 - d2; // empate: dias
if (dif > 0)      printf("primeira\\n");
else if (dif < 0) printf("segunda\\n");
else              printf("iguais\\n");''',
         erros=[('if (a1 > a2 || m1 > m2)', '/* critério em ordem */', 'mês só importa se os anos empatarem'),
                ('/* esqueceu o empate */', 'else printf("iguais");', 'a terceira saída também vale ponto')],
         mesa=dict(cab=['pessoa 1', 'pessoa 2', 'dif final', 'saída'], codigo='''int c[3][6] = {{20, 3, 1, 19, 11, 30}, {20, 3, 1, 20, 5, 0}, {20, 3, 1, 20, 3, 1}};
for (int i = 0; i < 3; i++) {
    int *v = c[i];
    int dif = v[0] - v[3];
    if (dif == 0) dif = v[1] - v[4];
    if (dif == 0) dif = v[2] - v[5];
    MESA("%da %dm %dd & %da %dm %dd & %d & %s", v[0], v[1], v[2], v[3], v[4], v[5], dif, dif > 0 ? "primeira" : dif < 0 ? "segunda" : "iguais");
}'''),
         passos=['Ler anos, meses e dias das duas pessoas',
                 'Diferença dos anos; se zero, dos meses; se zero, dos dias',
                 'Sinal da diferença decide a mensagem'],
         dica=['Momento de cada lado = peso × comprimento',
               'Compare os dois momentos: três resultados possíveis',
               'Escreva a mensagem exata de cada caso']),
    dict(n=8, tema='switch: escolha entre muitos casos',
         objetivo='Usar `switch` para mapear valores a textos e combinar com `/` e `%`.',
         resolvida='A1-2012.2-QIV', proposta='A1-2017.1-QII',
         conceitos=['`switch (x) { case 1: ...; break; default: ...; }` compara `x` com constantes',
                    'Sem `break`, a execução "cai" no próximo `case`',
                    '`default` trata todos os valores não listados',
                    'Combine: `dia / 10` dá a dezena, `dia % 10` a unidade'],
         padrao='''switch (mes) {
    case 1: printf("janeiro"); break;
    case 2: printf("fevereiro"); break;
    /* ... */
    default: printf("dezembro"); break;
}''',
         erros=[('case 1: printf("um");', 'case 1: printf("um"); break;', 'sem `break` imprime "umdoistrês..."'),
                ('case x > 10:', 'if (x > 10)', '`case` só aceita constantes, não condições'),
                ('/* sem validar */', 'if (mes < 1 || mes > 12)', 'valide antes do `switch`')],
         mesa=dict(cab=['dia', 'dia / 10', 'dia \\% 10', 'por extenso'], oculto=True, legenda='Separando dezena e unidade com `/` e `%`:', codigo='''const char *u[] = {"", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"};
int d[3] = {21, 30, 7};
for (int i = 0; i < 3; i++)
    MESA("%d & %d & %d & %s%s%s", d[i], d[i] / 10, d[i] % 10, d[i] / 10 == 2 ? "vinte" : d[i] / 10 == 3 ? "trinta" : "", d[i] >= 20 && d[i] % 10 ? " e " : "", u[d[i] % 10]);'''),
         passos=['Validar dia e mês',
                 'Dia: casos especiais (1 e 10 a 19), senão dezena + " e " + unidade',
                 'Mês: um `switch` com 12 casos'],
         dica=['Finais iguais: `n % 10000` (milhar), `n % 1000` (centena), `n % 100` (dezena)',
               'Grupo do bicho: `(dezena - 1) / 4`, com 00 valendo 100',
               '`else if` do maior prêmio para o menor: só o maior é pago']),
    dict(n=9, tema='Geometria com condições: pontos e regiões',
         objetivo='Decidir se pontos estão dentro de regiões e calcular sobreposições com `max`/`min`.',
         resolvida='A1-2025.2-QI', proposta='A1-2023.1-QI',
         conceitos=['Ponto dentro de um retângulo: `x >= xmin && x <= xmax && y >= ymin && y <= ymax`',
                    'Faça o desenho com eixos e teste os pontos da borda',
                    'Sobreposição de intervalos [a1, b1] e [a2, b2]: de `max(a1, a2)` até `min(b1, b2)`',
                    'Se `max(a1, a2) >= min(b1, b2)`, não há sobreposição'],
         padrao='''int ini = a1 > a2 ? a1 : a2;   // max
int fim = b1 < b2 ? b1 : b2;   // min
int sobreposto = fim > ini ? fim - ini : 0;''',
         erros=[('if (x < k && y < k)', 'if (x >= -k && x <= k && ...)', 'esqueceu o lado negativo'),
                ('x > -k', 'x >= -k', 'bola na linha: dentro ou fora? leia o enunciado'),
                ('/* sem desenho */', '/* desenhe os eixos */', 'erro de sinal some com o desenho')],
         mesa=dict(cab=['k', 'x', 'y', 'resultado'], codigo='''int c[4][3] = {{5, 3, 2}, {5, -5, 5}, {5, 6, 1}, {5, 0, -1}};
for (int i = 0; i < 4; i++) {
    int k = c[i][0], x = c[i][1], y = c[i][2];
    MESA("%d & %d & %d & %s", k, x, y, (x >= -k && x <= k && y >= 0 && y <= k) ? "dentro" : "fora");
}'''),
         passos=['Desenhar a quadra: x vai de −k a k, y de 0 a k',
                 'Uma única condição com quatro comparações e `&&`',
                 'Testar os cantos e um ponto de cada lado de fora'],
         dica=['Cada terreno: canto superior esquerdo + dimensões (o y cresce para baixo)',
               'Esquerda = maior dos x; direita = menor das bordas direitas (o mesmo em y)',
               'Só existe área se largura e altura forem positivas']),
    dict(n=10, tema='Modelagem: do enunciado à conta',
         objetivo='Transformar uma situação do dia a dia em contas com `/` e `%` e decisões simples.',
         resolvida='A1-2025.2-QII', proposta='A1-2024.1-QI',
         conceitos=['Leia o enunciado duas vezes e liste: dados, o que imprimir, restrições',
                    'Faça 2 exemplos à mão **antes** de programar',
                    'Pontos igualmente espaçados: ponto anterior = `d / p`, distância até ele = `d % p`',
                    'Escolher o mais próximo: comparar `resto` com `p - resto`'],
         padrao='''int antes = d / p;      // pontos completos antes de d
int resto = d % p;      // metros depois do ponto anterior
if (resto * 2 <= p)     // mais perto do anterior
    printf("ponto %d, anda %d\\n", antes + 1, resto);
else
    printf("ponto %d, volta %d\\n", antes + 2, p - resto);''',
         erros=[('if (resto <= p / 2)', 'if (resto * 2 <= p)', '`p / 2` trunca quando `p` é ímpar'),
                ('/* ponto 0 ou 1? */', '/* confira a numeração */', 'o primeiro ponto é o 1 ou o 0?')],
         mesa=dict(cab=['d', 'd / p', 'd \\% p', 'saída (p = 100)'], codigo='''int p = 100, d[3] = {250, 380, 40};
for (int i = 0; i < 3; i++) {
    int antes = d[i] / p, resto = d[i] % p;
    if (resto * 2 <= p) MESA("%d & %d & %d & ponto %d, anda %d", d[i], antes, resto, antes + 1, resto);
    else MESA("%d & %d & %d & ponto %d, volta %d", d[i], antes, resto, antes + 2, p - resto);
}'''),
         passos=['Pontos a cada P metros, o 1º no início da avenida',
                 'Ponto anterior = `D / P + 1`; distância = `D % P`',
                 'Se passar da metade, desce no próximo e anda para trás'],
         dica=['A partícula percorre a distância e os sensores se repetem a cada 8 metros',
               'Posição relativa ao ciclo = `(d - 5) % 8`',
               'Decida qual sensor (1 a 3) ou nenhum']),
    dict(n=11, tema='Bits: XOR, AND e deslocamento',
         objetivo='Manipular os bits de um inteiro com `^`, `&` e `>>`.',
         resolvida='A1-2026.1-QII', proposta='A1-2023.2-QII',
         conceitos=['`a ^ b` (XOR): bit 1 onde `a` e `b` diferem',
                    '`x & 1` é o último bit; `x >> k` desloca k casas para a direita',
                    'Bit k de x: `(x >> k) & 1`',
                    'Inverter o bit k: `x ^ (1 << k)`',
                    'Equivalente sem bits: `% 2` e `/ 2`'],
         padrao='''int x = a ^ b;                 // bits diferentes
int dif = 0;
for (int k = 0; k < 4; k++)
    dif += (x >> k) & 1;       // conta os 1''',
         erros=[('if (x & 1 == 1)', 'if ((x & 1) == 1)', '`==` tem prioridade maior que `&`'),
                ('a ^ 2  /* "a ao quadrado" */', 'a * a', '`^` é XOR, não potência')],
         mesa=dict(cab=['k', '(x >> k) \\& 1', 'dif'], codigo='''int a = 9, b = 3, x = a ^ b, dif = 0;
for (int k = 0; k < 4; k++) {
    dif += (x >> k) & 1;
    MESA("%d & %d & %d", k, (x >> k) & 1, dif);
}'''),
         passos=['XOR marca os bits diferentes entre a e b',
                 'Contar os bits 1 do XOR (4 bits)',
                 'Comparar a contagem com n'],
         dica=['Inverter um bit: XOR com `1 << k`',
               'Cuidado com a numeração das posições (da direita, a partir de 0 ou 1?)',
               'Imprima em binário para conferir']),
    dict(n=12, tipo='avaliacao', tema='Avaliação I', questoes=['A1-2024.1-QII', 'A1-2026.1-QI'],
         objetivo='Prova do Bloco 1, no formato das avaliações anteriores. Abaixo, uma prova-modelo com duas questões de provas passadas.'),
    # ---------------------------------------------------------------- Bloco 2
    dict(n=13, tema='while: repetir até uma condição',
         objetivo='Repetir enquanto a condição for verdadeira e contar quantas vezes repetiu.',
         resolvida='A2-2016.1-QI', proposta='A2-2024.2-QI',
         conceitos=['`while (condição) { ... }` testa **antes** de cada repetição',
                    'Algo dentro do laço precisa mudar a condição, senão é laço infinito',
                    'Contador: `anos = 0` antes, `anos++` dentro',
                    'A condição do `while` é o **contrário** da condição de parada'],
         padrao='''int anos = 0;
while (ze <= chico) {   // para quando ze > chico
    chico += 2;
    ze += 3;
    anos++;
}''',
         erros=[('while (ze > chico)', 'while (ze <= chico)', 'o `while` repete enquanto **não** parou'),
                ('while (x > 0) { y--; }', 'while (x > 0) { x--; }', 'a variável da condição não muda'),
                ('int anos; anos++;', 'int anos = 0;', 'contador sem valor inicial')],
         mesa=dict(cab=['anos', 'chico', 'zé', 'zé <= chico?'], codigo='''int chico = 150, ze = 110, anos = 0;
MESA("%d & %d & %d & %s", anos, chico, ze, ze <= chico ? "sim" : "não");
while (ze <= chico && anos < 3) {
    chico += 2; ze += 3; anos++;
    MESA("%d & %d & %d & %s", anos, chico, ze, ze <= chico ? "sim" : "não");
}
MESA("\\\\dots & \\\\dots & \\\\dots & \\\\dots");
while (ze <= chico) { chico += 2; ze += 3; anos++; }
MESA("%d & %d & %d & %s", anos, chico, ze, ze <= chico ? "sim" : "não");'''),
         passos=['Alturas em centímetros (inteiros): 150 e 110',
                 'Repetir enquanto Zé ≤ Chico: soma 2 e 3, conta um ano',
                 'Resposta: 41 anos'],
         dica=['A cada minuto sobram 90% da massa: `massa = massa * 0.9`',
               'Repetir enquanto a massa for maior que a massa final',
               'Contar os minutos']),
    dict(n=14, tema='for e acumuladores: somatórios',
         objetivo='Calcular somas de séries com `for` e um acumulador.',
         resolvida='A2-2014.2-QIII', proposta='A2-2014.2-QI',
         conceitos=['`for (int k = 1; k <= n; k++)`: início, condição, passo',
                    'Acumulador: `soma = 0` antes; `soma += termo` dentro',
                    'Um termo que depende do anterior: guarde-o numa variável (ex.: triangular += k)',
                    'Frações: `1.0 / t`, nunca `1 / t`'],
         padrao='''double soma = 0;
long t = 0;                 // número triangular
for (int k = 1; k <= n; k++) {
    t += k;                 // 1, 3, 6, 10, ...
    soma += 1.0 / t;
}''',
         erros=[('soma += 1 / t;', 'soma += 1.0 / t;', '`1 / 3` vale 0'),
                ('for (k = 1; k < n; k++)', 'for (k = 1; k <= n; k++)', 'esqueceu o último termo'),
                ('for (...) { double soma = 0; ... }', 'double soma = 0; for (...)', 'zerou a soma a cada volta')],
         mesa=dict(cab=['k', 't', '1.0 / t', 'soma'], codigo='''double soma = 0; long t = 0;
for (int k = 1; k <= 4; k++) {
    t += k; soma += 1.0 / t;
    MESA("%d & %ld & %.4f & %.4f", k, t, 1.0 / t, soma);
}'''),
         passos=['Termo k = 1 / (k-ésimo triangular)',
                 'Triangular k = triangular anterior + k',
                 '`for` de 1 a n acumulando'],
         dica=['Subtraia 1, 3, 5, 7, ... enquanto der',
               'O número de subtrações é a raiz inteira',
               'Ímpar seguinte: `impar += 2`']),
    dict(n=15, tema='Laço sobre os dígitos',
         objetivo='Percorrer os dígitos de um número de tamanho qualquer com `while (n > 0)`.',
         resolvida='A1-2014.2-QIV', proposta='A1-2018.2-QII',
         conceitos=['`while (n > 0) { d = n % 10; ...; n = n / 10; }` visita todos os dígitos',
                    'A ordem é da direita para a esquerda (unidade primeiro)',
                    'Posição do dígito: um contador que começa em 1',
                    'Em outra base b: troque 10 por b'],
         padrao='''int soma = 0, pos = 1;
while (n > 0) {
    int d = n % 10;
    if (pos % 2 == 0) {      // posições pares dobram
        d = d * 2;
        if (d > 9) d -= 9;
    }
    soma += d;
    n /= 10;
    pos++;
}''',
         erros=[('while (n != 0) /* n negativo */', 'while (n > 0)', 'trate a entrada antes'),
                ('/* usou n depois do laço */', 'int copia = n;', 'o laço destrói o número')],
         mesa=dict(cab=['n', 'pos', 'd', 'soma'], codigo='''int n = 4539, soma = 0, pos = 1;
while (n > 0) {
    int d = n % 10;
    if (pos % 2 == 0) { d = d * 2; if (d > 9) d -= 9; }
    soma += d;
    MESA("%d & %d & %d & %d", n, pos, d, soma);
    n /= 10; pos++;
}'''),
         passos=['Percorrer os dígitos da direita para a esquerda',
                 'Dígitos em posição par: dobrar; se > 9, subtrair 9',
                 'Válido se a soma for múltipla de 10'],
         dica=['Mesmo laço, mas com base 7: `% 7` e `/ 7`',
               'Some os algarismos na base 7; DV = soma % 7',
               'Imprima o número seguido do DV']),
    dict(n=16, tema='Laços com condição de parada incerta',
         objetivo='Simular processos que param em um número desconhecido de passos.',
         resolvida='A1-2024.1-QI-B', proposta='A2-2026.1-QI',
         conceitos=['Quando não se sabe quantas repetições, use `while`',
                    'Cada repetição aplica a regra **uma** vez',
                    'Conte os passos ou os termos (inclua o primeiro, se o enunciado pedir)',
                    'Valores que crescem muito: `long`'],
         padrao='''int termos = 1;            // o próprio n conta
while (n != 1) {
    if (n % 2 == 0) n = n / 2;
    else            n = 3 * n + 1;
    termos++;
}''',
         erros=[('if (n % 2 == 0) n /= 2; if (n % 2 != 0) ...', 'if ... else ...', 'dois `if` aplicam a regra duas vezes'),
                ('int termos = 0;', 'int termos = 1;', 'confira se o primeiro número conta')],
         mesa=dict(cab=['passo', 'n', 'termos'], codigo='''long n = 6; int termos = 1, passo = 0;
MESA("%d & %ld & %d", passo, n, termos);
while (n != 1) {
    if (n % 2 == 0) n = n / 2; else n = 3 * n + 1;
    termos++; passo++;
    MESA("%d & %ld & %d", passo, n, termos);
}'''),
         passos=['Regra: par → n/2; ímpar → 3n+1',
                 'Repetir até chegar a 1',
                 'Contar os números da sequência, incluindo o primeiro e o 1'],
         dica=['A cada 6 horas: `teor = teor / 2 + dose`',
               'Repita enquanto o teor não passar do limite',
               'Some 6 horas a cada repetição']),
    dict(n=17, tema='Laços aninhados: primos e divisores',
         objetivo='Usar um laço dentro de outro para testar divisibilidade.',
         resolvida='A2-2014.2-QII', proposta='A2-2019.2-QIII',
         conceitos=['n é primo se nenhum d de 2 até √n divide n',
                    'Condição `d * d <= n` evita `sqrt`',
                    'Laço externo escolhe candidatos; interno testa cada um',
                    'Bandeira (flag): `primo = 1` antes, `primo = 0` ao achar divisor'],
         padrao='''int primo = (n >= 2);
for (int d = 2; d * d <= n; d++)
    if (n % d == 0) {
        primo = 0;
        break;
    }''',
         erros=[('for (d = 1; ...)', 'for (d = 2; ...)', 'todo número é divisível por 1'),
                ('else primo = 1;', '/* só zera */', 'a flag não pode voltar a 1 no laço'),
                ('/* 1 é primo? */', 'primo = (n >= 2);', '1 não é primo')],
         mesa=dict(cab=['p', 'p primo?', 'p+2 primo?', 'achados'], codigo='''int achados = 0;
for (int p = 3; p <= 13; p += 2) {
    int a = 1, b = 1;
    for (int d = 3; d * d <= p + 2; d += 2) {
        if (p % d == 0 && d < p) a = 0;
        if ((p + 2) % d == 0 && d < p + 2) b = 0;
    }
    if (a && b) achados++;
    MESA("%d & %s & %s & %d", p, a ? "sim" : "não", b ? "sim" : "não", achados);
}'''),
         passos=['Primos gêmeos: p e p + 2 primos',
                 'Candidatos ímpares a partir de 3; parar ao achar N pares',
                 'Testar os dois com o mesmo laço de divisores'],
         dica=['σ(n) = soma de todos os divisores de n (inclui 1 e n)',
               'Laço externo: n de 1 a N; interno: d de 1 a n',
               'Zere a soma a cada novo n']),
    dict(n=18, tema='Funções: dividir para conquistar',
         objetivo='Escrever funções com parâmetros e retorno e reutilizá-las.',
         resolvida='A2-2016.2-QI', proposta='A2-2016.1-QII',
         conceitos=['`int nome(int x) { ... return valor; }`',
                    'Declare a função **antes** do `main` (ou o protótipo)',
                    'Uma função = uma pergunta: `e_primo(n)` responde 1 ou 0',
                    'Variáveis dentro da função são locais'],
         padrao='''int e_primo(int n) {
    if (n < 2) return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0) return 0;
    return 1;
}
/* no main */
if (e_primo(p) && e_primo(p + 2)) ...''',
         erros=[('int f(int n) { if (...) return 1; }', '... return 0; }', 'falta retorno em algum caminho'),
                ('printf dentro de e_primo', 'return 1 / return 0', 'função de teste não imprime'),
                ('e_primo(n);  /* sozinho */', 'if (e_primo(n))', 'o valor devolvido foi descartado')],
         mesa=dict(cab=['p', 'e\\_primo(p)', 'e\\_primo(p+2)', 'semiprimo(p+2)', 'Chen?'], oculto=True, legenda='O que cada função responde para alguns valores de p:', codigo='''int c[4] = {7, 13, 43, 3};
for (int i = 0; i < 4; i++) {
    int p = c[i], q = p + 2, a = 1, b = 1, s = 0;
    for (int d = 2; d * d <= p; d++) if (p % d == 0) a = 0;
    for (int d = 2; d * d <= q; d++) if (q % d == 0) b = 0;
    for (int d = 2; d * d <= q; d++) if (q % d == 0) { int x = d, y = q / d, px = 1, py = 1;
        for (int e = 2; e * e <= x; e++) if (x % e == 0) px = 0;
        for (int e = 2; e * e <= y; e++) if (y % e == 0) py = 0;
        s = px && py; break; }
    MESA("%d & %d & %d & %d & %s", p, a, b, s, a && (b || s) ? "sim" : "não");
}'''),
         passos=['Primo de Chen: p primo e p + 2 primo ou semiprimo',
                 'Duas funções: `e_primo` e `e_semiprimo`',
                 'O `main` só lê, pergunta às funções e imprime'],
         dica=['Função que testa se n é "brasileiro" numa base b',
               'Escreva n na base b (laço com `% b` e `/ b`) e veja se os dígitos são iguais',
               'Teste todas as bases de 2 a n − 2']),
    dict(n=19, tema='Vetores: guardar para comparar',
         objetivo='Ler valores em um vetor e comparar cada elemento com o anterior.',
         resolvida='A2-2025.2-QII', proposta='A1-2022.1-QII-B',
         conceitos=['`int v[N];` reserva N inteiros: `v[0]` a `v[N-1]`',
                    'Ler: `for (i = 0; i < N; i++) scanf("%d", &v[i]);`',
                    'Comparar com o anterior: comece o laço em 1 e use `v[i - 1]`',
                    'Vetor de contagem: `cont[d]++` conta quantas vezes d aparece'],
         padrao='''int atual = 1, maior = 1;
for (int i = 1; i < N; i++) {
    if (v[i] == v[i - 1]) atual++;
    else atual = 1;
    if (atual > maior) maior = atual;
}''',
         erros=[('for (i = 0; i <= N; i++)', 'for (i = 0; i < N; i++)', '`v[N]` não existe'),
                ('for (i = 0; ...) v[i] == v[i-1]', 'for (i = 1; ...)', '`v[-1]` não existe'),
                ('int cont[10];', 'int cont[10] = {0};', 'contadores sem zerar')],
         mesa=dict(cab=['i', 'v[i]', 'atual', 'maior'], codigo='''int v[8] = {3, 3, 5, 5, 5, 2, 5, 5}, atual = 1, maior = 1;
MESA("0 & %d & %d & %d", v[0], atual, maior);
for (int i = 1; i < 8; i++) {
    if (v[i] == v[i - 1]) atual++; else atual = 1;
    if (atual > maior) maior = atual;
    MESA("%d & %d & %d & %d", i, v[i], atual, maior);
}'''),
         passos=['Ler os N valores no vetor',
                 'Sequência atual cresce se igual ao anterior; senão volta a 1',
                 'Guardar o maior tamanho visto'],
         dica=['Vetor `cont[10] = {0}`',
               'Para cada número de A a B, percorra seus dígitos e faça `cont[d]++`',
               'Imprima os 10 contadores']),
    dict(n=20, tema='Janelas deslizantes',
         objetivo='Calcular algo (soma, média, máximo) em todos os blocos de tamanho fixo de um vetor.',
         resolvida='A2-2025.2-QI', proposta='A1-2024.2-QII-D',
         conceitos=['Janela de tamanho J começando em `ini`: posições `ini` a `ini + J - 1`',
                    'Inícios válidos: `ini + J <= N`',
                    'Laço externo: início; interno: percorre a janela',
                    'Maior/menor: inicialize com um valor impossível ou com a primeira janela'],
         padrao='''for (int ini = 0; ini + J <= N; ini++) {
    int soma = 0;
    for (int k = ini; k < ini + J; k++)
        soma += t[k];
    double media = (double)soma / J;
    /* atualizar maior e menor */
}''',
         erros=[('for (ini = 0; ini < N; ini++)', 'ini + J <= N', 'a última janela sairia do vetor'),
                ('double maior = 0;', 'double maior = -500;', 'temperaturas negativas'),
                ('media = soma / J;', 'media = (double)soma / J;', 'divisão inteira')],
         mesa=dict(cab=['ini', 'janela', 'soma', 'média'], codigo='''int t[6] = {20, 24, 22, 30, 18, 16}, J = 3;
for (int ini = 0; ini + J <= 6; ini++) {
    int soma = 0;
    for (int k = ini; k < ini + J; k++) soma += t[k];
    MESA("%d & %d, %d, %d & %d & %.2f", ini, t[ini], t[ini + 1], t[ini + 2], soma, (double)soma / J);
}'''),
         passos=['Ler as temperaturas e o tamanho da janela',
                 'Para cada início válido, média da janela',
                 'Guardar maior e menor média'],
         dica=['Mesma estrutura de janelas',
               'Em cada janela, ache o mínimo e o máximo',
               'Pontos da janela = mínimo + máximo; acumule']),
    dict(n=21, tema='Subsequências: dois índices',
         objetivo='Examinar todos os pares (início, fim) de um vetor de forma eficiente.',
         resolvida='A2-2019.2-QI', proposta='A2-2016.1-QIII',
         conceitos=['Subsequência consecutiva = trecho `v[ini..fim]`',
                    'Fixe `ini`; ao avançar `fim`, a soma só ganha `v[fim]` (não recalcule tudo)',
                    'São N(N+1)/2 trechos: para N = 1000, 500 mil, tranquilo',
                    'Com valores não negativos, pode-se parar quando a soma passar do alvo'],
         padrao='''int quantas = 0;
for (int ini = 0; ini < n; ini++) {
    int soma = 0;
    for (int fim = ini; fim < n; fim++) {
        soma += v[fim];
        if (soma == x) quantas++;
    }
}''',
         erros=[('int soma = 0; for (ini ...)', 'for (ini ...) { int soma = 0;', 'a soma tem que recomeçar a cada início'),
                ('for (fim = ini + 1; ...)', 'for (fim = ini; ...)', 'trechos de um elemento também contam')],
         mesa=dict(cab=['ini', 'fim', 'soma', 'quantas'], codigo='''int v[4] = {2, 1, 3, 1}, x = 4, quantas = 0;
for (int ini = 0; ini < 4; ini++) {
    int soma = 0;
    for (int fim = ini; fim < 4; fim++) {
        soma += v[fim];
        if (soma == x) quantas++;
        MESA("%d & %d & %d & %d", ini, fim, soma, quantas);
    }
}'''),
         passos=['Ler N, os valores e X',
                 'Para cada início, estender o fim somando',
                 'Contar quando a soma for exatamente X'],
         dica=['Entrar numa sala e sair por outra = trecho consecutivo `v[ini..fim]`',
               'Mesma estrutura de dois índices, mas guardando a **maior** soma',
               'Inicie o recorde com `v[0]` (pode haver salas negativas)']),
    dict(n=22, tema='Vetor como memória: detectar repetição',
         objetivo='Usar um vetor de marcação para saber se um valor já apareceu.',
         resolvida='A1-2024.2-QI-D', proposta='A2-2016.2-QII',
         conceitos=['`int visto[MAX] = {0};` e `visto[x] = 1` ao encontrar x',
                    '`if (visto[x])` responde em um passo se x já apareceu',
                    'Guarde a sequência num segundo vetor para imprimir depois',
                    'O tamanho do vetor tem que cobrir o maior valor possível'],
         padrao='''int visto[200] = {0}, seq[200], tam = 0;
while (!visto[n]) {
    visto[n] = 1;
    seq[tam++] = n;
    n = proximo(n);
}''',
         erros=[('int visto[200];', 'int visto[200] = {0};', 'lixo de memória parece "já visto"'),
                ('visto[n] com n = 500', '/* garanta n < 200 */', 'acesso fora do vetor')],
         mesa=dict(cab=['n', 'já visto?', 'próximo'], codigo='''int visto[200] = {0}, n = 4;
while (1) {
    int soma = 0;
    for (int x = n; x > 0; x /= 10) soma += (x % 10) * (x % 10);
    if (soma >= 100) soma /= 2;
    MESA("%d & %s & %d", n, visto[n] ? "sim" : "não", visto[n] ? 0 : soma);
    if (visto[n]) break;
    visto[n] = 1; n = soma;
}'''),
         passos=['Próximo termo = soma dos quadrados dos dígitos (regra do enunciado)',
                 'Marcar cada termo; parar quando repetir',
                 'Imprimir a sequência guardada'],
         dica=['Recamán: a(n) = a(n−1) − n se for positivo e ainda não usado; senão a(n−1) + n',
               'Vetor `usado[]` para a pergunta "já apareceu?"',
               'Imprima os 20 primeiros']),
    dict(n=23, tema='Simulação: posições circulares e pilha',
         objetivo='Simular movimentos numa pista circular e operações de empilhar/desempilhar.',
         resolvida='A2-2025.1-QII', proposta='A2-2023.2-QI',
         conceitos=['Posições 1..N circulares: `pos = (pos - 1 + passo + N) % N + 1`',
                    'O `+ N` evita resto negativo quando o passo é negativo',
                    'Pilha num vetor: `v[topo++] = x` empilha; `topo--` desempilha',
                    'Simule exatamente os comandos, um por vez'],
         padrao='''int pilha[100], topo = 0;
scanf("%d", &x);
while (x != -1) {
    if (x == 0) topo--;          // apaga o último
    else pilha[topo++] = x;      // guarda
    scanf("%d", &x);
}''',
         erros=[('pos = (pos + passo) % N;', 'pos = (pos - 1 + passo + N) % N + 1;', 'posições começam em 1'),
                ('(-3) % 10 /* = 7? */', '(-3 + 10) % 10', 'em C, `-3 % 10` vale −3'),
                ('topo-- com topo == 0', 'if (topo > 0) topo--;', 'pilha vazia')],
         mesa=dict(cab=['comando', 'estação', 'vezes (alvo 2)'], codigo='''int n = 5, est = 1, alvo = 2, vezes = 0, cmd[5] = {3, -2, 4, -4, 1};
MESA("-- & %d & %d", est, vezes);
for (int i = 0; i < 5; i++) {
    est = (est - 1 + cmd[i] + n) % n + 1;
    if (est == alvo) vezes++;
    MESA("%+d & %d & %d", cmd[i], est, vezes);
}'''),
         passos=['Robô começa na estação 1 (ela conta, se for o alvo)',
                 'Cada comando anda para frente (+) ou para trás (−), circular',
                 'Contar as paradas na estação devastada'],
         dica=['Cada número é empilhado; "zero" remove o último',
               'Um número negativo encerra a leitura',
               'No fim, some o que ficou na pilha']),
    dict(n=24, tipo='avaliacao', tema='Avaliação II', questoes=['A2-2025.1-QI', 'A2-2026.1-QII'],
         objetivo='Prova do Bloco 2, no formato das avaliações anteriores. Abaixo, uma prova-modelo com duas questões de provas passadas.'),
    # ---------------------------------------------------------------- Bloco 3
    dict(n=25, tema='Strings: vetor de char terminado em \\0',
         objetivo='Ler, percorrer e comparar caracteres de uma string.',
         resolvida='A3-2023.2-QII', proposta='A3-2014.2-QII',
         conceitos=['`char s[100];` guarda até 99 letras + o `\'\\0\'` final',
                    'Uma palavra: `scanf("%99s", s)`; uma linha: `fgets(s, sizeof s, stdin)`',
                    'Percorrer: `for (i = 0; s[i] != \'\\0\'; i++)`',
                    'Caracteres são números (ASCII): `\'a\' < \'b\'`; `tolower`, `isalpha` em `<ctype.h>`'],
         padrao='''#include <ctype.h>
int ordenada = 1;
for (int i = 1; s[i] != '\\0'; i++)
    if (tolower(s[i - 1]) > tolower(s[i]))
        ordenada = 0;''',
         erros=[('if (s == "sim")', 'if (strcmp(s, "sim") == 0)', '`==` compara endereços, não textos'),
                ('scanf("%s", &s);', 'scanf("%99s", s);', 'o vetor já é um endereço'),
                ('char s[5] = "maçãs";', 'char s[20];', 'faltou espaço para o `\\0` (e acentos ocupam 2 bytes)')],
         mesa=dict(cab=['i', 's[i-1]', 's[i]', 'ordenada'], codigo='''char s[] = "FLoRa"; int ordenada = 1;
for (int i = 1; s[i] != '\\0'; i++) {
    if (tolower(s[i - 1]) > tolower(s[i])) ordenada = 0;
    MESA("%d & %c & %c & %d", i, s[i - 1], s[i], ordenada);
}'''),
         passos=['Ler a palavra com `scanf("%99s", p)`',
                 'Comparar cada letra com a anterior, sem diferenciar maiúsculas',
                 'Uma inversão basta para "não ordenada"'],
         dica=['Leia a frase inteira com `fgets`',
               'Função `consoante(c)`: letra que não está em "aeiou"',
               'Conte consoantes seguidas; a 2ª do grupo forma um encontro']),
    dict(n=26, tema='Vetor de contagem por letra',
         objetivo='Indexar um vetor de 26 posições pela letra (`c - \'A\'`).',
         resolvida='A3-2024.2-QII', proposta='A3-2026.1-QII',
         conceitos=['Índice da letra: `toupper(c) - \'A\'` vai de 0 (A) a 25 (Z)',
                    'Volta: `\'A\' + k` é a letra de índice k',
                    'Contagem: `cont[k]++`; primeira posição: guardar só se ainda for −1',
                    'Inicialize com um laço quando o valor inicial não for 0'],
         padrao='''int primeira[26];
for (int k = 0; k < 26; k++) primeira[k] = -1;
for (int i = 0; s[i] != '\\0'; i++)
    if (isalpha(s[i])) {
        int k = toupper(s[i]) - 'A';
        if (primeira[k] == -1) primeira[k] = i;
    }''',
         erros=[('cont[s[i]]++;', 'cont[toupper(s[i]) - \'A\']++;', 'índice 97 não existe num vetor de 26'),
                ('int primeira[26] = {-1};', 'laço preenchendo -1', 'só a posição 0 recebe −1'),
                ('/* conta espaço e pontuação */', 'if (isalpha(s[i]))', 'só letras têm índice')],
         mesa=dict(cab=['i', 's[i]', 'k', 'primeira[k]'], codigo='''char s[] = "Oba, boa"; int primeira[26];
for (int k = 0; k < 26; k++) primeira[k] = -1;
for (int i = 0; s[i] != '\\0'; i++)
    if (isalpha((unsigned char)s[i])) {
        int k = toupper((unsigned char)s[i]) - 'A';
        if (primeira[k] == -1) primeira[k] = i;
        MESA("%d & %c & %d & %d", i, s[i], k, primeira[k]);
    }'''),
         passos=['Ler a linha com `fgets`',
                 'Para cada letra, guardar a posição só na primeira vez',
                 'Imprimir em ordem alfabética as letras que apareceram'],
         dica=['Conte as letras da palavra num vetor de 26',
               'A fórmula vem em pares dígito + letra: `exigido[letra - \'A\'] = dígito - \'0\'`',
               'Todas as letras precisam bater']),
    dict(n=27, tema='Validação de strings',
         objetivo='Verificar se uma string obedece a regras usando `strchr` e laços.',
         resolvida='A3-2025.2-QI', proposta='A3-2019.1-QI',
         conceitos=['`strchr(s, c)` devolve NULL se `c` não está em `s` (`<string.h>`)',
                    '`fgets` guarda o `\'\\n\'`; remova com `s[strcspn(s, "\\n")] = \'\\0\'`',
                    'Validação: começa válido; qualquer violação torna inválido',
                    'Pode parar no primeiro erro (`break`)'],
         padrao='''fgets(msg, sizeof msg, stdin);
msg[strcspn(msg, "\\n")] = '\\0';     // tira o Enter
int pode = 1;
for (int i = 0; msg[i] != '\\0'; i++)
    if (strchr(alfabeto, msg[i]) == NULL)
        pode = 0;''',
         erros=[('fgets(...); /* e o \\n? */', 's[strcspn(s, "\\n")] = \'\\0\';', 'o Enter vira um caractere inválido'),
                ('scanf("%d", &n); fgets(s, ...);', 'getchar(); antes do fgets', 'o Enter do número fica no buffer')],
         mesa=dict(cab=['msg[i]', 'está no alfabeto?', 'pode'], codigo='''const char *alf = "!1ob"; const char *msg = "ob1!x!"; int pode = 1;
for (int i = 0; msg[i] != '\\0'; i++) {
    if (strchr(alf, msg[i]) == NULL) pode = 0;
    MESA("%c & %s & %d", msg[i], strchr(alf, msg[i]) ? "sim" : "não", pode);
}'''),
         passos=['Ler o alfabeto e a mensagem com `fgets` (podem ter espaços)',
                 'Cada caractere da mensagem tem que estar no alfabeto',
                 'Imprimir a mensagem correspondente'],
         dica=['Marque as letras presentes: `tem[s[i] - \'a\'] = 1`',
               'Faixa começa numa letra presente cuja anterior não está presente',
               'Estenda a faixa enquanto a próxima letra existir e imprima `início:fim`']),
    dict(n=28, tema='Mapear caracteres: tabelas e conversões',
         objetivo='Converter caracteres usando uma tabela indexada e a aritmética de `char`.',
         resolvida='A3-2019.1-QII', proposta='A4-2024.2-QI',
         conceitos=['Tabela como string: `"22233344455566677778889999"[c - \'A\']`',
                    'Dígito → número: `c - \'0\'`',
                    'Letra hexadecimal → valor: `c - \'A\' + 10`',
                    'Conversão de base com string: `valor = valor * base + digito` (da esquerda para a direita)'],
         padrao='''int valor = 0;
for (int i = 0; s[i] != '\\0'; i++) {
    int d;
    if (isdigit(s[i])) d = s[i] - '0';
    else d = toupper(s[i]) - 'A' + 10;
    valor = valor * 16 + d;
}''',
         erros=[('d = s[i];', 'd = s[i] - \'0\';', '`\'7\'` vale 55 na tabela ASCII'),
                ('valor += d * 16;', 'valor = valor * 16 + d;', 'regra de Horner')],
         mesa=dict(cab=['s[i]', 'd', 'valor'], codigo='''const char *s = "1F4"; int valor = 0;
for (int i = 0; s[i] != '\\0'; i++) {
    int d = isdigit((unsigned char)s[i]) ? s[i] - '0' : toupper((unsigned char)s[i]) - 'A' + 10;
    valor = valor * 16 + d;
    MESA("%c & %d & %d", s[i], d, valor);
}'''),
         passos=['Tabela com o dígito de cada letra do teclado do telefone',
                 'Letra → `tabela[letra - \'A\']`; o resto (dígitos e hífens) fica igual',
                 'Imprimir a string convertida'],
         dica=['Leia o hexadecimal como string',
               'Converta cada caractere em 0..15',
               'Horner: `valor = valor * 16 + d`']),
    dict(n=29, tema='Palavras numa frase',
         objetivo='Separar as palavras de uma frase com uma variável de estado (dentro/fora de palavra).',
         resolvida='A4-2026.1-QI', proposta='A3-2025.1-QI',
         conceitos=['Estado `dentro`: 1 quando o caractere anterior era letra',
                    'Começo de palavra: letra com `dentro == 0`',
                    'Fim de palavra: não-letra (ou `\'\\0\'`) com `dentro == 1`',
                    'Trate o fim da string como separador'],
         padrao='''int palavras = 0, dentro = 0;
for (int i = 0; ; i++) {
    if (isalpha(s[i])) {
        dentro = 1;
    } else {
        if (dentro) palavras++;   // terminou uma palavra
        dentro = 0;
        if (s[i] == '\\0') break;
    }
}''',
         erros=[('palavras = espacos + 1;', '/* estado dentro/fora */', 'espaços duplos e pontuação quebram a conta'),
                ('for (...; s[i] != \'\\0\'; ...)', '/* conte a última palavra */', 'a última palavra não tem espaço depois')],
         mesa=dict(cab=['i', 's[i]', 'dentro', 'palavras'], oculto=True, legenda='Frase "Ser ou  nao!" (dois espaços seguidos e pontuação no fim):', codigo='''const char *s = "Ser ou  nao!"; int palavras = 0, dentro = 0;
for (int i = 0; ; i++) {
    if (isalpha((unsigned char)s[i])) dentro = 1;
    else { if (dentro) palavras++; dentro = 0; }
    MESA("%d & %s & %d & %d", i, s[i] == ' ' ? "\\\\textvisiblespace" : s[i] ? (char[]){s[i], 0} : "\\\\textbackslash 0", dentro, palavras);
    if (s[i] == '\\0') break;
}'''),
         passos=['Ler a letra e a frase (atenção ao `\'\\n\'` entre elas)',
                 'Percorrer com o estado dentro/fora; ao fechar uma palavra, contar',
                 'Marcar se a palavra atual contém a letra; imprimir a razão'],
         dica=['Separe as palavras com o mesmo estado dentro/fora',
               'A i-ésima letra de "cobol" deve estar no início ou no fim da i-ésima palavra',
               'Guarde o início de cada palavra para olhar a primeira e a última letra']),
    dict(n=30, tema='Matrizes: linhas, colunas e percursos',
         objetivo='Declarar, ler e percorrer matrizes; trocar o papel de linha e coluna.',
         resolvida='A3-2014.2-QI', proposta='A3-2026.1-QI',
         conceitos=['`int m[L][C];` e acesso `m[i][j]` (linha i, coluna j)',
                    'Dois laços: externo nas linhas, interno nas colunas',
                    '`m[i][j]` percorre a linha i; `m[j][i]` percorre a coluna i',
                    'Rotação horária: `nova[i][j] = m[n - 1 - j][i]`'],
         padrao='''for (int i = 0; i < n; i++) {
    int soma_linha = 0, soma_coluna = 0;
    for (int j = 0; j < n; j++) {
        soma_linha  += m[i][j];
        soma_coluna += m[j][i];
    }
}''',
         erros=[('scanf("%d", m[i][j]);', 'scanf("%d", &m[i][j]);', 'o `&` continua necessário'),
                ('for (j = 0; j < n; i++)', 'for (j = 0; j < n; j++)', 'incremento da variável errada'),
                ('int m[10][10]; /* sem limite */', '#define N 10', 'use uma constante para recompilar fácil')],
         mesa=dict(cab=['i', 'linha i', 'uns linha', 'uns coluna'], codigo='''int m[3][3] = {{0, 1, 0}, {1, 0, 0}, {0, 0, 1}};
for (int i = 0; i < 3; i++) {
    int ul = 0, uc = 0;
    for (int j = 0; j < 3; j++) { ul += m[i][j]; uc += m[j][i]; }
    MESA("%d & %d %d %d & %d & %d", i, m[i][0], m[i][1], m[i][2], ul, uc);
}'''),
         passos=['Permutação: só 0 e 1, e exatamente um 1 por linha e por coluna',
                 'Para cada i, somar a linha i e a coluna i no mesmo laço',
                 'Qualquer soma diferente de 1 (ou valor fora de 0/1) reprova'],
         dica=['Desenhe uma matriz 3 × 3 e a girada: de onde vem cada elemento?',
               'Linha i da nova = coluna i da original, lida de baixo para cima',
               'Imprima direto, sem segunda matriz, ou use uma auxiliar']),
    dict(n=31, tema='Matrizes em blocos e em 3 dimensões',
         objetivo='Percorrer sub-blocos de uma matriz e trabalhar com uma terceira dimensão (canais).',
         resolvida='A3-2024.2-QI', proposta='A3-2025.1-QII',
         conceitos=['Bloco F × F começando em (bi, bj): `i` de `bi` a `bi + F - 1`',
                    'Inícios de bloco andam de F em F: `bi += F`',
                    'Quatro laços: dois para os blocos, dois dentro do bloco',
                    'Imagem colorida: `img[i][j][c]`, c = 0 (R), 1 (G), 2 (B)'],
         padrao='''for (int bi = 0; bi < n; bi += f)
    for (int bj = 0; bj < n; bj += f) {
        int maior = img[bi][bj];
        for (int i = bi; i < bi + f; i++)
            for (int j = bj; j < bj + f; j++)
                if (img[i][j] > maior) maior = img[i][j];
        printf("%d ", maior);
    }''',
         erros=[('for (bi = 0; bi < n; bi++)', 'bi += f', 'blocos sobrepostos'),
                ('int maior = 0;', 'int maior = img[bi][bj];', 'funciona aqui, mas falha com negativos'),
                ('int img[100][100][3]; /* no main */', '/* global */', 'matrizes grandes podem estourar a pilha')],
         mesa=dict(cab=['bloco (bi, bj)', 'valores', 'máximo'], codigo='''int img[4][4] = {{1, 3, 2, 1}, {4, 6, 5, 0}, {7, 2, 9, 8}, {3, 1, 4, 4}}, f = 2;
for (int bi = 0; bi < 4; bi += f)
    for (int bj = 0; bj < 4; bj += f) {
        int maior = img[bi][bj];
        for (int i = bi; i < bi + f; i++) for (int j = bj; j < bj + f; j++) if (img[i][j] > maior) maior = img[i][j];
        MESA("(%d, %d) & %d %d %d %d & %d", bi, bj, img[bi][bj], img[bi][bj + 1], img[bi + 1][bj], img[bi + 1][bj + 1], maior);
    }'''),
         passos=['Ler N, F e a imagem',
                 'Para cada bloco F × F (passo F), achar o máximo',
                 'Imprimir uma linha de máximos por linha de blocos'],
         dica=['Matriz `img[100][100][3]` (global)',
               'Cinza = 0,299 R + 0,587 G + 0,114 B',
               'Arredonde: `(int)(cinza + 0.5)`']),
    dict(n=32, tema='Simulação em grade',
         objetivo='Simular movimentos ou propagação numa matriz de caracteres.',
         resolvida='A3-2025.2-QII', proposta='A3-2023.2-QI',
         conceitos=['Cada linha da grade é uma string: `char g[N][M + 1]`',
                    'Andar: N → linha−1, S → linha+1, L → coluna+1, O → coluna−1',
                    'Antes de acessar, teste os limites: `0 <= l < N` e `0 <= c < M`',
                    'Ciclo: matriz `visitado`; voltar a uma casa visitada = laço infinito'],
         padrao='''while (1) {
    if (l < 0 || l >= m || c < 0 || c >= m) { /* saiu */ break; }
    if (mapa[l][c] == 'X')  { /* chegou */ break; }
    if (visitado[l][c])     { /* ciclo */ break; }
    visitado[l][c] = 1;
    /* anda conforme mapa[l][c] */
}''',
         erros=[('if (mapa[l][c] == ... ) /* antes do limite */', '/* teste os limites primeiro */', 'acesso fora da matriz'),
                ('/* sem detectar ciclo */', 'int visitado[N][N] = {{0}};', 'o programa nunca termina')],
         mesa=dict(cab=['minuto', '(l, c)', 'casa', 'próximo'], codigo='''const char *g[4] = {"SSOS", "SLLS", "OXOO", "NSSN"};
int l = 0, c = 2, t = 0;
while (g[l][c] != 'X') {
    char d = g[l][c]; int nl = l + (d == 'S') - (d == 'N'), nc = c + (d == 'L') - (d == 'O');
    MESA("%d & (%d, %d) & %c & (%d, %d)", t, l, c, d, nl, nc);
    l = nl; c = nc; t++;
}
MESA("%d & (%d, %d) & X & tesouro", t, l, c);'''),
         passos=['Ler a arena (linhas como strings) e o ponto de pouso',
                 'Seguir as setas minuto a minuto',
                 'Três finais: fora dos limites, tesouro (tempo) ou preso (ciclo)'],
         dica=['Regras: água cai para baixo; sobre prateleira escorre para os lados',
               'Repita varreduras da matriz até nenhuma casa mudar',
               'Teste com o exemplo do enunciado']),
    dict(n=33, tema='Busca em grade de caracteres',
         objetivo='Procurar padrões em linhas e colunas de uma grade.',
         resolvida='A3-2023.1-QI', proposta='A3-2023.1-QII',
         conceitos=['Para cada posição inicial, compare a palavra letra a letra',
                    'Horizontal: `g[i][j + k]`; vertical: `g[i + k][j]`',
                    'Cheque antes se a palavra cabe: `j + t <= n` e `i + t <= m`',
                    'Por colunas: percorra `k` nas linhas fixando a coluna'],
         padrao='''int h = (j + t <= n), v = (i + t <= m);
for (int k = 0; k < t; k++) {
    if (h && g[i][j + k] != p[k]) h = 0;
    if (v && g[i + k][j] != p[k]) v = 0;
}
if (h || v) achou = 1;''',
         erros=[('g[i][j + k] sem testar j + t <= n', 'h = (j + t <= n)', 'leitura fora da linha'),
                ('achou = (g[i][j] == p[0]);', '/* compare todas as letras */', 'só a primeira letra não basta')],
         mesa=dict(cab=['(i, j)', 'horizontal', 'vertical'], codigo='''const char *g[3] = {"GATO", "AXIS", "SOLO"}; const char *p = "GAS"; int t = 3;
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 4; j++) {
        if (g[i][j] != p[0]) continue;
        int h = j + t <= 4, v = i + t <= 3;
        for (int k = 0; k < t; k++) { if (h && g[i][j + k] != p[k]) h = 0; if (v && g[i + k][j] != p[k]) v = 0; }
        MESA("(%d, %d) & %s & %s", i, j, h ? "sim" : "não", v ? "sim" : "não");
    }'''),
         passos=['Ler a grade e a palavra',
                 'Tentar cada posição em horizontal e vertical',
                 'Pontuação: tamanho da palavra ou −5'],
         dica=['As 5 fitas formam uma matriz 5 × 8',
               'Para cada coluna, conte A, C, G e T',
               'A mais frequente vence; empate vira `?`']),
    dict(n=34, tema='struct: registros',
         objetivo='Agrupar dados de um item com `struct` e processar um vetor de registros.',
         resolvida='A3-2014.2-QIII', proposta='A4-2026.1-QII',
         conceitos=['`typedef struct { char nome[50]; double preco; } Produto;`',
                    'Vetor de structs: `Produto p[100];` e acesso `p[i].preco`',
                    'Duas passadas: a primeira calcula a média, a segunda aplica a regra',
                    'Guarde o **índice** do melhor, não só o valor'],
         padrao='''typedef struct {
    char nome[50];
    double preco;
} Produto;

Produto p[100];
scanf("%49s %lf", p[i].nome, &p[i].preco);''',
         erros=[('scanf("%s", &p[i].nome);', 'scanf("%49s", p[i].nome);', 'string não leva `&`'),
                ('if (p[i].preco < media) /* média parcial */', '/* média antes */', 'a média precisa de todos os preços'),
                ('double menor = p[i].preco;', 'int barato = i;', 'sem o índice, perde-se o nome')],
         mesa=dict(cab=['nome', 'preço', '< média?', 'novo preço'], codigo='''const char *nome[3] = {"arroz", "feijao", "cafe"}; double preco[3] = {10, 8, 20}, media = (10 + 8 + 20) / 3.0;
for (int i = 0; i < 3; i++)
    MESA("%s & %.2f & %s & %.2f", nome[i], preco[i], preco[i] < media ? "sim" : "não", preco[i] < media ? preco[i] * 1.10 : preco[i]);
MESA("\\\\multicolumn{4}{c}{média = %.2f}", media);'''),
         passos=['Struct com nome e preço; vetor de 100',
                 '1ª passada: ler e somar; média',
                 '2ª passada: +10% nos abaixo da média e procurar o mais barato'],
         dica=['Cada paciente: pressão, glicemia, risco (+1 ou −1)',
               'Distância de Manhattan: |Δpressão| + |Δglicemia|',
               'Vizinhos votam; empate (inclusive nenhum vizinho) é INCONCLUSIVO']),
    dict(n=35, tipo='avaliacao', tema='Avaliação III', questoes=['A4-2025.1-QI', 'A4-2024.2-QII'],
         objetivo='Prova do Bloco 3, no formato das avaliações anteriores. Abaixo, uma prova-modelo com duas questões de provas passadas.'),
    dict(n=36, tipo='reavaliacao', tema='Reavaliação', questoes=['A1-2022.1-QII', 'A4-2025.1-QII'],
         objetivo='Reavaliação: substitui a menor nota. Abaixo, uma prova-modelo com duas questões de provas passadas.'),
]
