# Primeiro Programa em Python

# Desenvolvedor: Marcos Paulo P. Carneiro

import numpy as np

print('Calculadora Básica\n')

print('Menu Interativo:\n \n 1) Soma \n 2) Subtração \n 3) Divisão \n 4) Multiplicação\n')

x = int(input('Digite a operação desejada: '))

num1 = int(input('\nDigite o primeiro número: '))

num2 = int(input('\nDigite o segundo número: '))

if x == 1:
   
   print('\nOperação escolhida: Soma.')
   print(num1 + num2)

elif x == 2:
   
   print('\nOperação escolhida: Subtração.')
   print(num1 - num2)

elif x == 3:

   print('\nOperação escolhida: Divisão.')
   print(num1/num2)

elif x == 4:
   print('\nOperação escolhida: Multiplicação.')
   print(num1*num2)

else:
   print('\nOperação Inválida.')