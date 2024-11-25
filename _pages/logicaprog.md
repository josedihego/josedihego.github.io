---
title: ""
layout: single
permalink: /logicaprog/
author_profile: true
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">


## INF027 - LÓGICA DE PROGRAMAÇÃO -  ADS

#### Github da disciplina com TODOS os códigos
 
 - <span class="education-title">[Github](https://github.com/josedihego/programacaoC)</span> 
   
#### Questões
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
- Celsius para Fahrenheit: \( F = C \times \frac{9}{5} + 32 \)
- Fahrenheit para Celsius: \( C = (F - 32) \times \frac{5}{9} \)
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
2. Calcule o IMC usando a fórmula \( IMC = \frac{\text{peso}}{\text{altura}^2} \).
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
