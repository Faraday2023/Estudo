"""Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta"""

from random import randint
from time import sleep

jogadas = int(input('Digite quantos jogos pretende fazer: '))
lista_aux = []
lista_final = []
count = 0

for j in range(0, jogadas):

    while count < 6:

        numero = (randint(1,60))

        if numero not in lista_aux:

            lista_aux.append(numero)
            count += 1

    lista_final.append(lista_aux[:])
    lista_aux.clear()
    count = 0

print('-'*40)

for itens, palpites in enumerate(lista_final):
    print(f'Jogada n°{itens+1}: {palpites}')
    sleep(1)
    print('-'*40)
print('Obrigado, volte sempre !')
