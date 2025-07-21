'''
DESCRIÇÃO
OBS: estamos reaproveitando o mesmo codigo do desafio bancário anterior.

Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário 
previamente desenvolvido com o uso de funções Python. O objetivo é 
aprimorar a estrutura e a eficiência do sistema, implementando as 
operações de depósito, saque e extrato em funções específicas. 
Você terá a chance de refatorar o código existente, dividindo-o em 
funções reutilizáveis, facilitando a manutenção e o entendimento do 
sistema como um todo. Prepare-se para aplicar conceitos avançados de 
programação e demonstrar sua habilidade em criar soluções mais elegantes 
e eficientes utilizando Python.

OBJETIVO:
Implementar operações: criar usuário, criar nova conta 

REGRAS:
01. Função saque kwd only;
02. Função usuário: lista com nome, nascimento, cpf e endereço;
    02.1. Endereço no formato: logradouro-numero-bairro-cidade/sigla do estado.
    02.2. CPF somente numeros, nao pode haver dois usuarios com o mesmo cpf.
03. Criar conta: Armazenadas em listas;
    03.1. Uma conta deve ter:agencia, numero da conta e usuário;
    03.2. O numero da conta é sequencial, iniciando em 1;
    03.3. Numero da agencia é fixo: 0001
04. Função saldo positional only: saldo, valor, extrato -> retorna: saldo, extrato;
05. Função extrato: positional only: saldo, kwd only:extrato.


nome = "Isaias"
numero_saque = 3
limite_valor_saque = 500
saldo = 100.00
extrato = []
'''
from datetime import datetime,date

data_hoje = date.today()

def menu():  
    '''
    Seja bem vindo ao banco DIO, escolha uma opção abaixo:
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair\n
    =>
    '''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

while True:
    escolha = float(input(menu))
    if escolha == 1:
        if numero_saque == 0:
            print("Você alcançou seu limite de saques diários. Por favbor, volte amanhã.")
            continue

        valor = float(input('Digite o valor do saque: '))
        if valor <= 0 or valor > saldo or valor > limite_valor_saque:
            print('Valor fornecido inválido, tente novamente')
            
        else:
            saldo = saldo - valor
            extrato.append(f'Saque de R${valor:.2f}')
            print(f'''
                Transação aprovada.
                valor do saque: R${valor:.2f}
                Saldo atual: R${saldo:.2f}
                Contando cédulas..
                Retire o valor abaixo.
                  ''')
            numero_saque = numero_saque-1
    elif escolha == 2:
        print(f'''
---- Terminal de atendimento banco DIO ----
Data:{data_hoje}
Cliente: {nome}
Transações:
''')
        
        if not extrato:                      
            print("Sem movimentações.")        
        else:
            for item in extrato:
                print(item)

        print(f'Saldo: R$ {saldo:.2f}')                

    elif escolha == 3:
        deposito = float(input('Digite o valor a ser depositado: '))
        if deposito > 0:
            saldo = saldo + deposito
            extrato.append(f'Deposito de R${deposito}')
            print(
            f'R${deposito:.2f} foram adicionados a sua conta\nSaldo atual:R$ {saldo:.2f}.')
            
        else:
            print('Transação recusada, o valor a ser depositado deve ser maior que zero.')
    
    elif escolha > 4:
        print('Opção inexistente, por favor escolha uma das opções de [1] a [4]:')
                
    else:
        print('''
            Obrigado por utilizar os terminais de autoatendimento DIO
            Encerrando...
              ''')
        break
