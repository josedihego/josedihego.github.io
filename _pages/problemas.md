---
title: "Python – Problemas e Soluções"
layout: single
permalink: /problemas/
author_profile: true
classes: course-page
---
[← Cursos](/courses/){: .back-link}

<a class="repo-card" href="https://github.com/josedihego/selecao_problemas_resolvidos"><i class="fab fa-github" aria-hidden="true"></i><span><strong>Soluções</strong><small>github.com/josedihego/selecao_problemas_resolvidos</small></span></a>

## Parte 1

1. Em uma empresa de transporte de mercadorias trabalham diversos funcionários.
   - Cada funcionário tem um nome, CPF e um salário bruto mensal.
   - Cada veículo da frota possui placa, número de quilômetros rodados e modelo.

2. É preciso ordenar os funcionários por salário bruto, em ordem crescente e ordenar os veículos por quilômetros rodados em ordem decrescente.

3. Um loja guarda as entradas e saídas de valores financeiros do dia em um arquivo de texto chamado <code>entrada_saida.txt</code>.
   - Uma linha deste arquivo se parece com: <code>25/10/2022 300 -100 -45.56 250 180 -980 300 400 420 -1520</code>
   - É preciso que cada linha destas seja processada e armazenada em um outro arquivo chamado <code>compilado.txt</code> onde cada linha se parece com: <code>25/10/2022 −795.56</code>

4. Calcular o determinante de uma matriz 3x3.

5. É preciso produzir n-elementos da sequência de Fibonacci como mostrado abaixo.

6. É preciso calcular o fatorial de n, para n >= 0.

7. Um jogo deve mostrar uma sequência com 10 números aleatórios, recebendo em no máximo 30 segundos a resposta correta.

8. Um gráfico em pizza deve ser gerado com dados em uma planilha.

9. Uma planilha em formato .xlsx deve ser lida e seus dados compilados e armazenados em outra planilha.

10. [IME/USP] Dados dois naturais m e n, determinar, entre todos os pares de números naturais (x,y) tais que x < m e y < n, um par para o qual o valor da expressão xy - x²+ y seja máximo e calcular também esse máximo.

11. É preciso decidir se um número é primo.

12. [IME/USP] Dado um número inteiro positivo n, determinar todos os inteiros entre 1 e n que são comprimento da hipotenusa de um triângulo retângulo com catetos inteiros.

13. É preciso implementar o encriptador de César. Para César-ROT13 temos:
    - texto: abcdefghijklmnopqrstuvwxyz
    - cifrado: nopqrstuvwxyzabcdefghijklm

## Parte 2

1. Em uma casa de apostas online, clientes podem apostar quantias monetárias informando um palpite sobre um evento futuro.
   - A casa de apostas tem nome, CNPJ e link de acesso.
   - Clientes possuem nome, CPF, saldo e conta bancária.
   - Uma conta bancária possui código do banco, agência e número.
   - Um evento futuro pode ter possibilidades teoricamente infinitas, como o placar de um jogo de futebol, ou ter possibilidades finitas, como o resultado de uma eleição entre dois candidatos.
   - É preciso modelar esse sistema.

2. Considerando o sistema anterior e as operações de cadastro padrão, é preciso uma solução de persistência, de preferência via banco de dados local.

3. Na sede física da casa de apostas, um sistema local com interface gráfica é necessário para gerenciar os funcionários da empresa.

4. A sede física da casa de apostas possui um sistema de monitoramento.
   - A sala de comando é um ambiente especial onde as pessoas que lá estão devem ser monitoradas.
   - O sistema deve capturar todas as faces que entrem/saiam da sala e usem quaisquer computadores, cujas câmeras ficam ligadas ininterruptamente.

5. Periodicamente, a casa de apostas envia a 10% de seus clientes mais fiéis uma cesta de amenities.
   - O endereço de cada cliente é conhecido e as distâncias entre eles são calculadas.
   - É preciso calcular a melhor rota de entrega considerando a sede como ponto de partida e (depois de todas as entregas) chegada.

6. [IME/USP] Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.

7. [IME/USP] Faça uma função angulo que recebe um ponto de coordenadas cartesianas reais (x,y), com x > 0 e y > 0 e devolve o ângulo formado pelo vetor (x,y) e o eixo horizontal.
