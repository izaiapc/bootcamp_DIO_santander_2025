'''
DESCRIÇÃO
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
O sistema será desenvolvido para um banco que busca monetizar suas operações. 
Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação 
Python e criar um sistema funcional que simule as operações bancárias. 
Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver
soluções práticas e eficientes.

OBJETIVO:
Implementar três operações essenciais: depósito, saque e extrato. 

REGRAS:
01. Apenas valores positivos;
02. Limite de 3 saques diários;
03. Limite por saque: R$ 500,00;
04. Mensagem de saldo insuficiente;
05. Histórico de movimentação (saque/deposito) exibidos no extrato.
06. Valores exibidos no formato R$ 000.00
'''
from datetime import datetime,date

data_hoje = date.today()
nome = "Isaias"
numero_saque = 3
limite_valor_saque = 500
saldo = 100.00
extrato = []
abertura = '''
Seja bem vindo ao banco DIO, escolha uma opção abaixo:
[1] Saque
[2] Extrato
[3] Depósito
[4] Sair
'''

while True:
    escolha = float(input(abertura))
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
