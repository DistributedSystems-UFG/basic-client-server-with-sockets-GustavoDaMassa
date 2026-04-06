[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

# Processador de Lotes Distribuído (Client-Server Basics)

## Descrição do Sistema
Este projeto expande a arquitetura cliente-servidor básica ao introduzir um modelo de Processamento em Lotes utilizando serialização de dados em formato JSON. 

o sistema permite que o cliente envie um payload estruturado contendo múltiplas requisições de diferentes funcionalidades em uma única transação de rede. O servidor recebe o pacote, atua como um roteador de comandos, delega o processamento para as funções específicas de regra de negócio, consolida os resultados e os devolve formatados ao cliente.

## Funcionalidades Implementadas

1. analyze_text: Recebe uma string e realiza varredura algorítmica para retornar uma estrutura com o número de palavras, caracteres totais e contagem de vogais.
2. calculate_stats: Recebe um array numérico e processa operações de estatística descritiva, retornando a Média, Mediana, Valor Máximo e Valor Mínimo do conjunto de dados.
3. generate_fibonacci: Calcula e retorna a sequência matemática de Fibonacci até a posição *N* informada pelo cliente.


