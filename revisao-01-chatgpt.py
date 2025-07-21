'''
Revisão chatgpt
9. Corrija o código abaixo para que ele acumule nomes por tema corretamente:

dados = {}
n = int(input('Digite a quantidade de pessoas: '))
for _ in range(n):
    entrada = input('Digite o nome e tema (pessoa,tema): ')
    nome, tema = entrada.split(",")
    dados[nome]=[]
    dados[nome].append(tema)

print(dados)
'''
'''
10. Escreva um programa que leia n linhas no formato Tema: pessoa1, pessoa2, pessoa3
e converta isso para um dicionário no formato {pessoa: [temas]}.
Ou seja, você deve inverter o mapeamento e permitir que uma pessoa esteja em mais de um tema.**
'''
dados = {}
n = int(input('Digite a quantidade de temas: '))
for _ in range(n):
    entrada = input('Digite o tema e as pessoas participantes (Tema: pessoa1, pessoa2 etc): ')
    indice = entrada.find(":")
    tema=entrada[:indice]
    pessoas=entrada[indice+1:]
    participante=pessoas.split(',')
    dados[tema]=participante

print(dados)
