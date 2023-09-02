"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR"""

num = int(input('Digite um número: '))

if num%2 != 0:
    print('*='*20)
    print('O número digitado é ímpar.')
    print('*='*20)
else:
    print('*='*20)
    print('O número digitado é par.')
    print('*='*20)