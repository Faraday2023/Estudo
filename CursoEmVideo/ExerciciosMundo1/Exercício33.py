# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:

    if num2 > num3:

        print('O número {} é o maior é o número {} é o menor'.format(num1,num3))

    else:
         
         print('O número {} é o maior é o número {} é o menor'.format(num1,num2))

elif num2 > num1 and num2 > num3:

    if num1 > num3:
        
        print('O número {} é o maior é o número {} é o menor'.format(num2,num3))

    else:
         
         print('O número {} é o maior é o número {} é o menor'.format(num2,num1))

else:

    if num1 > num2:

        print('O número {} é o maior é o número {} é o menor'.format(num3,num2))

    else:
         
         print('O número {} é o maior é o número {} é o menor'.format(num3,num1))
