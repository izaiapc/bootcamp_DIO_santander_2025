'''
def somar(a,b):
    return a + b

def exibir(a,b,funcao):
    resultado=funcao(a,b)
    print(f'A soma é {a}+{b}={resultado}')

exibir(1,2,somar)
'''
def somar(a,b):
    return a + b

def exibir(a,b,somar):
    #resultado=funcao(a,b)
    print(f'A soma é {a}+{b}={somar}')

exibir(1,2,somar)