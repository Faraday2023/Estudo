""""Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequência de Fibonacci"""

número = int(input('Digite um número: '))
termo1 = 0
termo2 = 1
termo3 = 0
c = 3

print(f'{termo1}, {termo2},',end = ' ')

while c <= número:

    termo3 = termo1 + termo2
    print(f'{termo3}', end = '')
    print(',' if c < número   else '.',end = ' ')
    termo1 = termo2
    termo2 = termo3
    c += 1
