"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado"""

from random import randint
from time import sleep
from operator import itemgetter

dic = {}
ranking = []

print('Valores Sorteados: ')
for c in range(0,4):

    dic[f'Jogador {c+1}'] = randint(1,6)

print('-'*35)

for pos, item in dic.items():
    print(f'O {pos} tirou: {item} no dado')
    sleep(1)

print('-'*35)
print('Ranking dos jogadores')

ranking = sorted(dic.items(), key = itemgetter(1), reverse = True)
print('-'*35)

for pos, item in enumerate(ranking):

    print(f'O {item[0]} ficou em: {pos+1}°')
    sleep(1)

print('-'*35)