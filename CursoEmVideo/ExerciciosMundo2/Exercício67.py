"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo"""

print('-='*20)

while True:

    num = int(input('Digite o número que deseja ver a tabuada: '))

    if num < 0:

        print('\nNão existe tabuada de número negativo.')

        break

    c = 0

    while c <= 10:

        print(f'Elemento {c}: {num*c}. ')

        c += 1

    print('-='*20)
