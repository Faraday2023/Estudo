"""Faça um programa que leia um número qualquer e mostre o seu fatorial"""

from math import factorial

num = int(input('Digite um número: '))
c = num 
aux = 1
print(f'O fatorial de {num}! =', end = ' ')

while c != 0:

    print(c, end = ' ')
    print('x' if c > 1 else '=',end = ' ')

    aux = aux*c
    c -= 1

print(aux)
