# REPOSITÓRIO DEDICADO ÀS ATIVIDADES DO BOOTCAMP DIO SANTANDER BACKEND 2025!

## Desafio 01 - sistema bancário v1
Nessa atividade foi proposto um desafio de criar um sistema bancário simples onde são efetuadas três tipos de interações com o usuário: saque, extrato e depósito.
Além disso, o sistema deve obedecer as seguintes regras:
01. Apenas valores positivos;
02. Limite de 3 saques diários;
03. Limite por saque: R$ 500,00;
04. Mensagem de saldo insuficiente;
05. Histórico de movimentação (saque/deposito) exibidos no extrato.
06. Valores exibidos no formato R$ 000.00
#### Veja o codigo completo clicando [aqui](https://github.com/izaiapc/bootcamp_DIO_santander_2025/blob/main/desafio-sistema-bancario.py)

## Desafio 02 - Explorando Operadores e Manipulação de Strings
### 1 / 2 - Cálculo de Descontos em Loja

Descrição
Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

📌 Regras de desconto:

"DESCONTO10": 10% de desconto.
"DESCONTO20": 20% de desconto.
"SEM_DESCONTO": Sem desconto.
Entrada
Preço original do produto.
Código do cupom digitado.
Saída
Preço final após aplicar o desconto. Com duas casas decimais.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada   | Saída |
| ------------- | ------------- |
|100                 |
|DESCONTO10|	90.00|
|200|
|DESCONTO20|	160.00|
|50|
|SEM_DESCONTO|	50.00|

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”.

### 2 / 2 - Validador de Formato de E-mails

Descrição
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

📌 Regras para um e-mail válido:

Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
Não pode começar ou terminar com "@".
Não pode conter espaços.
Entrada
Uma string contendo o e-mail a ser validado.
Saída
"E-mail válido" se o e-mail estiver no formato correto.
"E-mail inválido" caso contrário.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada	|Saída|
------------|------
|usuario@gmail.com|E-mail válido|
|user@outlook.com|E-mail válido|
|usuario gmail.com|E-mail inválido|
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

## Desafio 03:Aplicando Estruturas de Dados e Listas
### 1 / 2 - Simulador de Carrinho de Compras

Descrição
Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).
Saída
Lista dos produtos adicionados e o total da compra.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada|	Saída|
--------|--------|
|2|Pão: R$3.50|
|Pão 3.50|Leite: R$4.00|
|Leite 4.00	|Total: R$7.50|
|||
|3|Arroz 2.50|
|Arroz 2.50|Brigadeiro 3.00|
|Brigadeiro: R$3.00
|Sorvete 14.50

|Sorvete: R$14.50
|Total: R$20.00
|3
|Maçã 2.00
|Pera 3.50
|Biscoito 5.50	Maçã: R$2.00
|Pera: R$3.50
|Biscoito: R$5.50
|Total: R$11.00

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”.

'''
    linha = input().strip()
'''