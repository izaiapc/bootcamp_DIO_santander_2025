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
'''
import textwrap


def menu():
    menu = "\nBem vindo ao banco DIO, escolha uma opção:".center(50,"=") + """\n
    [1]\tSaque
    [2]\tDepósito
    [3]\tExtrato
    [4]\tAbrir nova conta
    [5]\tMinhas contas
    [6]\tCadastrar novo usuário
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação não autorizada: Você não tem saldo suficiente.".center(55,"="))

    elif excedeu_limite:
        print("\nOperação não autorizada: O valor do saque excede o limite.".center(55,"="))

    elif excedeu_saques:
        print("\nOperação não autorizada: Número máximo de saques excedido.".center(55,"="))

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n==Saque autorizado==\nRetire R${valor:.2f} abaixo.")

    else:
        print("\nOperação não autorizada: O valor informado é inválido.".center(55,"="))

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nOperação não autorizada: O valor informado é inválido.".center(55,"="))

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

 
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()