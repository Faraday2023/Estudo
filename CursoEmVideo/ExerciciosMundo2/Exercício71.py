"""Crie um programa que simule o funcionamento de um caixa eletrônico, No início
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues

OBS. Considere que o caixa possui cédulas de R$ 50,00 R$ 20,00 R$ 10,00 e R$ 1,00:"""

valor_sacado = float(input('Digite o valor a ser sacado: '))
aux = valor_sacado
céd = 50
total_céd = 0

while True:

    if aux >= céd:

        aux = aux - céd
        total_céd = total_céd + 1

    else:

        if total_céd > 0:

            print(f'Foram contabilizadas {total_céd} cédulas de R$ {céd}')

        if céd == 50:
            céd = 20

        elif céd == 20:
            céd = 10

        elif céd == 10:
            céd = 1

        total_céd = 0
        
        if aux == 0:
            print('Todas as cédulas foram contabilizadas.')
            break
