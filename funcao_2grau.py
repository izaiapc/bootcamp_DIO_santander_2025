import numpy as np
def funcao(a,b,c):
    raiz=b**2-4*a*c 
    if raiz==b**2-4*a*c < 0:
        print('Não possui raizes reais')
    else:
        x1=(-b + np.sqrt(raiz))/(2*a)
        x2=(-b - np.sqrt(raiz))/(2*a)
        print(f'As raizes da equação são {x1} e {x2}')

funcao(-2,3,5)