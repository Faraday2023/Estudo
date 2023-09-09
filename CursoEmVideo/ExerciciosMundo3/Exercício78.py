"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas 
posições na lista"""

lista = list()
maior = 0
menor = 0

for c in range(0,5):

    lista.append(int(input('Digite números: ')))

    if c == 0:
        maior = menor = lista[c]

    else:
        if lista[c] > maior:
            maior = lista[c]

        if lista[c] < menor:
            menor = lista[c]

print(f'O maior valor é: {maior}, na posição: ', end = '')

for pos, item in enumerate(lista):

    if item == maior:
        print(f'{pos},', end =' ')

print(f'O menor valor é: {menor}, na posição: ', end = '')

for pos, item in enumerate(lista):

    if item == menor:
        print(f'{pos},', end = ' ')

"""
for c in range(1, 6):

    lista.append(int(input('Digite números: ')))

maior = max(lista)
menor = min(lista)

for pos, item in enumerate(lista):

    if maior == lista[pos]:

        pos_maior = pos

    if menor == lista[pos]:

        pos_menor = pos

print(f'A posição do maior valor: {maior} é: {pos_maior}')
print(f'A posição do maior valor: {menor} é: {pos_menor}')
"""