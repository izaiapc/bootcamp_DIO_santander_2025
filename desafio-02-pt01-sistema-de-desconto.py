escontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input('Digite o valor da sua compra: ').strip())
cupom = input('Digite o seu cupom de desconto: ').strip()


if cupom in descontos.keys():
    novo_preco = preco-preco*descontos[cupom]
    print(f"R${novo_preco:.2f}")
else:
    print('Digite um cupom válido')