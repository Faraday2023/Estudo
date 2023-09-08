"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem 
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso"""

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
         'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
         'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print('-'*25)
while True:
    num = int(input('Digite um número: '))
    if 0<=num<=20:
        print(tupla[num])
        print('-'*25)
        break
    print('-'*25)
    print('Por favor, digite corretamente.')
    print('-'*25)
    
