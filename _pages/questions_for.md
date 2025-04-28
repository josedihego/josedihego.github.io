---
title: ""
mathjax: true 
layout: single
permalink: /questions_for/
author_profile: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">


<span class="education-title">[VOLTAR](/logicaprog/)</span>


##  Questões (comandos de repetição)

### 1. Decidir primalidade

Escreva um programa que:
1. Solicite ao usuário que informe um número inteiro
2. Valide se o número é maior que 0
3. Sendo maior que zero, informe se este é primo

**Exemplo de execução**:
```bash
$ Digite um número: 9
$ Resultado: 9 não é primo
```

**Exemplo de execução**:
```bash
$ Digite um número: 11
$ Resultado: 11 é primo
```

### 2. Tabuada
Escreva um programa que:
1. Solicite ao usuário um número inteiro $$N$$
2. Exiba a tabuada de $$N$$ (de 1 até 10)
3. 
**Exemplo de execução**:
```bash
$ Digite um número: 3
$ Resultado:
$ 3 x 1 = 3
$ 3 x 2 = 6
$ 3 x 3 = 9
$ 3 x 4 = 12
$ 3 x 5 = 15
$ 3 x 6 = 18
$ 3 x 7 = 21
$ 3 x 8 = 24
$ 3 x 9 = 27
$ 3 x 10 = 30
```

### 3. Soma de números pares

Escreva um programa que:
1. Solicite ao usuário que informe um número inteiro positivo $$N$$
2. Calcule a soma de todos os números pares de 1 até $$N$$ (inclusive)
3. Exiba o resultado

**Exemplo de execução**:
```bash
$ Digite um número positivo: 10  
$ Soma dos pares até 10: 30  
```


### 4. Fatorial

Solicite ao usuário que informe um número inteiro não negativo ($$N \geq 0$$)

1. Teste se o número é válido (não negativo)
2 . Calcule e exiba o fatorial de $$N$$ (usando um laço de repetição)

**Lembrete**:
- \( 0! = 1 \)
- \( N! = N \times (N-1) \times (N-2) \times \cdots \times 1 \)

**Exemplo de execução**:
```bash
$ Digite um número não negativo: 5  
$ 5! = 120  
```

**Exemplo de execução**:
```bash
$ Digite um número não negativo: -3  
$ Erro: O número deve ser não negativo!  
```