"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
 qual será a base de conversão
 
 1) Binário
 2) Octal
 3) Hexadecimal"""

num = int(input('Digite um número qualquer: '))

print('-'*20, 'Menu Interativo', '-'*20,"""
      
      1) Binário
      2) Octal
      3) Hexadecimal\n""",
      '-'*55)

opção = int(input('Digite em qual base deseja converter: '))

if opção == 1:

    print(f'O número em binário é: {bin(num)}')

elif opção == 2:

    print(f'O número em octal é: {oct(num)}')

else:

    print(f'O número em hexadecimal é: {hex(num)}')
