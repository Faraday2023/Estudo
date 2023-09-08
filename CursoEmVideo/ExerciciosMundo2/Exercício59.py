"""Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso

1) Somar
2) Multiplicar
3) Maior
4) Novos números
5) Sair do programa"""

from time import sleep

print('-'*50)
operação = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('-'*50)
while operação !=5:

    print("""1) Somar\n2) Multiplicar\n3) Maior\n4) Novos números\n5) Sair do programa\n""")
    operação = int(input('Digite a operação desejada: '))

    if operação == 1:
        print('-'*50)
        soma = num1 + num2
        print(f'A soma de {num1} + {num2} = {soma}')
    
    elif operação == 2:
        print('-'*50)
        multiplicar = num1*num2
        print(f'A multiplicação de {num1} * {num2} = {multiplicar}')

    elif operação == 3:
        print('-'*50)
        maior = max(num1,num2)

        if num1 == num2:
            print('Os números são iguais')
        else:
    
            print(f'O maior número é: {maior}')
    
    elif operação == 4:

        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

    elif operação == 5:

        print('Obrigado, volte sempre.')
        
    else:

        print('Operação Inválida, tente novamente.')
    print('-'*50)
    sleep(2)
