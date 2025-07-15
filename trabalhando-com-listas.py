
"""import numpy 

numeros = [0,1,2,3,4,5,6,7,8,9,10]
numeros_pares = numeros[0:-1:2]
numeros_impares = numeros[1:-1:2]
print(numeros_pares)
print(numeros_impares)

for i in range(11):
    print(numeros[i])
#
#  compreenção de listas
a=[numero**2 for numero in numeros]
print(a)
b=[n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(b)
#
email = 'isaias plácido de carvalho'
separar = email.split(' ')
print(separar[0].title()+' '+separar[-1].title())

carros = ("gol") 
print(isinstance(carros, tuple))

pessoa = dict( 
    nome='isaias',
    idade=35,
    roupas=['camisa','bermuda']
)
pessoa['hobby']='jogar videogame'
print(

    f'''
O {pessoa['nome']} tem {pessoa['idade']} 
anos está usando {pessoa["roupas"][0]} e {pessoa["roupas"][1]}
ele também gosta de {pessoa["hobby"]}

)

print(pessoa.keys())
vazio = dict.fromkeys(["chave"],'valor')
print(vazio)
#
print(pessoa.get('calça'),'valor inexistente')
"""
dic = {'ele':['joao','mateus','pedro'],
       'ela':['maria','joana']}
print(dic.items())
