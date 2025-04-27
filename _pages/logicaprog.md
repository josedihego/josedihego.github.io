---
title: ""
mathjax: true 
layout: single
permalink: /logicaprog/
author_profile: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">


## INF027 - LÓGICA DE PROGRAMAÇÃO -  ADS

#### Github da disciplina com TODOS os códigos
 
 - <span class="education-title">[Github](https://github.com/josedihego/programacaoC)</span> 


###  Questões (variáveis, comandos de decisão)

## 1. Calculadora de operações básicas com validação

Escreva um programa que:
1. Solicite ao usuário dois números e uma operação matemática (`+`, `-`, `*`, `/`).
2. Use um bloco **if/else** para validar se a operação é válida.
3. Se for válida, use **switch** para realizar a operação e exibir o resultado.
4. Caso a operação seja divisão, verifique se o divisor é zero. Caso seja, exiba a mensagem **"Divisão por zero não permitida"** e termine o programa.

**Exemplo de execução**:
```bash
$ Digite o primeiro número: 10
$ Digite o segundo número: 5
$ Digite a operação (+, -, *, /): /
$ Resultado: 2.00
```

## 2. Classificação de triângulos

Escreva um programa que:
1. Solicite ao usuário três lados de um triângulo.
2. Verifique se os lados formam um triângulo válido (use a regra da desigualdade triangular: a soma de dois lados deve ser maior que o terceiro lado).
3. Se for válido, classifique o triângulo como:
   - **Equilátero**: todos os lados iguais.
   - **Isósceles**: dois lados iguais.
   - **Escaleno**: todos os lados diferentes.
4. Caso os lados não formem um triângulo, exiba **"Não é um triângulo válido"**.

**Exemplo de execução**:
```bash
$ Digite o lado 1: 5
$ Digite o lado 2: 5
$ Digite o lado 3: 8
$ O triângulo é Isósceles.
```

## 3. Menu de conversão de temperaturas

Crie um programa que:
1. Exiba um menu com as seguintes opções:  

```bash
$ Celsius para Fahrenheit
$ Fahrenheit para Celsius
$ Sair
```

2. Use um **switch** para processar a escolha do usuário.
3. Para as opções de conversão, solicite a temperatura correspondente e realize a operação usando as fórmulas:
- Celsius para Fahrenheit: $$ F = C \times \frac{9}{5} + 32 $$
- Fahrenheit para Celsius: $$ C = (F - 32) \times \frac{5}{9} $$
4. Caso o usuário escolha uma opção inválida, exiba **"Opção inválida"**.

**Exemplo de execução**:
```bash
$ Celsius para Fahrenheit
$ Fahrenheit para Celsius
$ Sair Escolha uma opção: 1
$ Digite a temperatura em Celsius: 25
$ Resultado: 77.00 °F
```

## 4. Jogo: Par ou Ímpar

Escreva um programa que:
1. Solicite ao usuário um número inteiro entre 1 e 100.
2. Valide se o número está no intervalo especificado.
3. Caso esteja, use um **if/else** para determinar se o número é **par** ou **ímpar** e exiba a mensagem correspondente.
4. Caso o número esteja fora do intervalo, exiba **"Número fora do intervalo permitido"**.

**Exemplo de execução**:
```bash
$ Digite um número entre 1 e 100: 42
$ O número é Par.
```

## 5. Cálculo do IMC com mensagens personalizadas

Crie um programa que:
1. Solicite ao usuário seu peso (em kg) e sua altura (em metros).
2. Calcule o IMC usando a fórmula $$ IMC = \frac{\text{peso}}{\text{altura}^2} $$.
3. Use **if/else** para classificar o IMC em categorias:
   - **Abaixo do peso**: IMC < 18.5
   - **Peso normal**: 18.5 ≤ IMC < 24.9
   - **Sobrepeso**: 25 ≤ IMC < 29.9
   - **Obesidade**: IMC ≥ 30
4. Exiba a categoria correspondente ao usuário.

**Exemplo de execução**:
```bash
$ Digite seu peso (kg): 70
$ Digite sua altura (m): 1.75
$ Seu IMC é 22.86. Categoria: Peso normal.
```

## 6. Validador de CPF

Escreva um programa que:
1. Solicite ao usuário um número de CPF com 11 dígitos.
2. Valide se o CPF é válido utilizando o cálculo dos dígitos verificadores:
   - Primeiro dígito verificador: considere os 9 primeiros dígitos e aplique a fórmula:
     $$
     DV1 = \left( \sum_{i=1}^{9} (CPF[i] \times (10-i)) \right) \mod 11
     $$
     Se o resto for menor que 2, o dígito é 0;
     caso contrário, é ($$ 11 - \text{resto} $$).
   - Segundo dígito verificador: aplique a fórmula acima aos 10 primeiros dígitos (incluindo o DV1).
3. Use **if/else** para verificar se o CPF é válido ou não.

**Exemplo de execução**:
```bash
$ Digite o CPF (apenas números): 12345678909 
$ CPF inválido.
```

## 7. Cálculo de raízes reais de uma equação quadrática

Crie um programa que:
1. Solicite ao usuário os coeficientes $$a$$, $$b$$, e $$c$$ de uma equação quadrática $$ ax^2 + bx + c = 0 $$.
2. Calcule o discriminante $$ \Delta = b^2 - 4ac $$.
3. Use **if/else** para classificar as raízes:
   - Se $$ \Delta < 0 $$: exiba **"Não existem raízes reais"**.
   - Se $$ \Delta = 0 $$: calcule a raiz única e exiba.
   - Se $$ \Delta > 0 $$: calcule as duas raízes e exiba.
4. Valide se $$a$$ é diferente de zero antes de realizar os cálculos.

**Exemplo de execução**:
```bash
$ Digite os coeficientes a, b e c: 1 -3 2 
$ Raízes reais: x1 = 2.00, x2 = 1.00
```


## 8. Classificação de números perfeitos, abundantes e deficientes

Escreva um programa que:
1. Solicite ao usuário um número inteiro positivo.
2. Calcule a soma de seus divisores próprios (excluindo o próprio número).
3. Classifique o número como:
   - **Perfeito**: soma dos divisores é igual ao número.
   - **Abundante**: soma dos divisores é maior que o número.
   - **Deficiente**: soma dos divisores é menor que o número.
4. Use **if/else** para exibir a classificação.

**Exemplo de execução**:
```bash
$ Digite um número: 28 
$ O número é Perfeito.
```

## 9. Verificar se um ponto está dentro de um triângulo

Escreva um programa que:
1. Solicite as coordenadas dos três vértices de um triângulo ($$A(x1, y1)$$, $$B(x2, y2)$$, $$C(x3, y3)$$).
2. Solicite as coordenadas de um ponto $$P(x, y)$$.
3. Use o método da área para verificar se o ponto está dentro do triângulo:
   - Calcule a área total do triângulo $$ABC$$.
   - Calcule as áreas $$ABP$$, $$BCP$$, e $$CAP$$.
   - Se a soma das áreas $$ABP + BCP + CAP$$ for igual à área $$ABC$$, o ponto está dentro.
4. Exiba o resultado com mensagens apropriadas.

**Exemplo de execução**:
```bash
$ Digite os vértices do triângulo (x1 y1 x2 y2 x3 y3): 0 0 5 0 0 5
$ Digite o ponto (x y): 2 2 
$ O ponto está dentro do triângulo.
```

## 10. Detectar interseção entre dois círculos
Crie um programa que:
1. Solicite os centros e os raios de dois círculos $$C1(x1, y1, r1)$$ e $$C2(x2, y2, r2)$$.
2. Calcule a distância entre os centros.
3. Use **if/else** para determinar:
   - Se os círculos se intersectam.
   - Se um círculo está completamente dentro do outro.
   - Se eles são tangentes.
   - Ou se estão separados.
4. Exiba mensagens apropriadas.

**Exemplo de execução**:
```bash
$ Digite o centro e raio do primeiro círculo (x1 y1 r1): 0 0 5 
$ Digite o centro e raio do segundo círculo (x2 y2 r2): 7 0 3 
$ Os círculos são tangentes.
```

## 11. Verificar colinearidade de três pontos

Escreva um programa que:
1. Solicite as coordenadas de três pontos $$P1(x1, y1)$$, $$P2(x2, y2)$$, $$P3(x3, y3)$$.
2. Use o determinante da matriz para verificar se os pontos são colineares:
   $$
   \text{Det} =
   \begin{vmatrix}
   x1 & y1 & 1 \\
   x2 & y2 & 1 \\
   x3 & y3 & 1 \\
   \end{vmatrix}
   $$
   - Se o determinante for $$0$$, os pontos são colineares.
3. Exiba o resultado.

**Exemplo de execução**:
```bash
$ Digite as coordenadas dos pontos (x1 y1 x2 y2 x3 y3): 0 0 2 2 4 4 
$ Os pontos são colineares.
```


## 12. Verificar se um ponto está dentro de um círculo e fora de um quadrado

Crie um programa que:
1. Solicite as coordenadas do centro e o raio de um círculo $$C(x, y, r)$$.
2. Solicite as coordenadas dos vértices de um quadrado $$Q(x1, y1, x2, y2)$$.
3. Solicite as coordenadas de um ponto $$P(x, y)$$.
4. Verifique se o ponto:
   - Está dentro do círculo.
   - Está fora do quadrado.
   - Exiba mensagens apropriadas.

**Exemplo de execução**:
```bash
$ Digite o círculo (centro x y raio): 0 0 5 
$ Digite os vértices opostos do quadrado (x1 y1 x2 y2): -2 -2 2 2 
$ Digite o ponto (x y): 3 3 
$ O ponto está dentro do círculo e fora do quadrado.
```


## 13. Determinar o tipo de quadrilátero dado pelos vértices

Escreva um programa que:
1. Solicite as coordenadas dos quatro vértices de um quadrilátero ($$A, B, C, D$$).
2. Calcule as distâncias entre os vértices consecutivos.
3. Use **if/else** para determinar se o quadrilátero é:
   - **Quadrado**: todos os lados têm o mesmo comprimento e as diagonais são iguais.
   - **Retângulo**: lados opostos iguais e diagonais iguais.
   - **Losango**: lados iguais, mas diagonais diferentes.
   - **Trapézio**: pelo menos um par de lados opostos paralelos (dica: use o coeficiente angular).
4. Exiba o tipo do quadrilátero.

**Exemplo de execução**:

```bash
$  Digite os vértices do quadrilátero (x1 y1 x2 y2 x3 y3 x4 y4): 0 0 4 0 4 3 0 3 
$ O quadrilátero é um Retângulo.
```


## 14. Verificar se dois retângulos se sobrepõem

Escreva um programa que:
1. Solicite as coordenadas dos vértices opostos de dois retângulos $$R1(x1, y1, x2, y2)$$ e $$R2(x3, y3, x4, y4)$$.
2. Use **if/else** para verificar se os retângulos se sobrepõem.
   - Dois retângulos se sobrepõem se as seguintes condições não forem atendidas:
     - Um retângulo está completamente à esquerda do outro.
     - Um retângulo está completamente acima do outro.
3. Exiba mensagens apropriadas indicando se eles se sobrepõem ou não.

**Exemplo de execução**:

```bash 
$ Digite os vértices opostos do primeiro retângulo (x1 y1 x2 y2): 0 0 4 4 
$ Digite os vértices opostos do segundo retângulo (x3 y3 x4 y4): 3 3 6 6 
$ Os retângulos se sobrepõem.
```

## 15. Determinar o ângulo entre dois vetores

Escreva um programa que:
1. Solicite as coordenadas de dois vetores no plano 2D: $$ v1(x1, y1)$$ e $$v2(x2, y2)$$.
2. Calcule o produto escalar $$ dot = x1 \cdot x2 + y1 \cdot y2 $$.
3. Calcule os módulos dos vetores
    $$ |v1| = \sqrt{x1^2 + y1^2} $$
    
    $$ |v2| = \sqrt{x2^2 + y2^2} $$
4. Use a fórmula do ângulo:
   $$
   \theta = \arccos\left(\frac{\text{dot}}{|v1| \cdot |v2|}\right)
   $$
5. Exiba o ângulo em graus.

**Exemplo de execução**:

```bash 
$ Digite as coordenadas do vetor 1 (x1 y1): 1 0 
$ Digite as coordenadas do vetor 2 (x2 y2): 0 1 
$ O ângulo entre os vetores é 90.00 graus.
```