"""Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma
 mensagem:

1) O primeiro valor é maior
2) O segundo valor é maior
3) Não existe valor maior, os dois são iguais"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:

    print(f'O primero valor: {num1} é maior do que o segundo valor {num2}.')

elif num2 > num1:

    print(f'O segundo valor {num2} é maior do que o primeiro valor {num1}.')

else:

    print('Os dois números são iguais')