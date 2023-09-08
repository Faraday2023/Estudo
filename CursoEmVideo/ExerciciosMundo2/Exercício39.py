"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua
idade, se ele ainda vai alistar-se ao serviço militar, se é a hora de se alistar ou se
já passou do tempo do alistamento . Seu programa também deverá  mostrar o tempo que falta
ou que passou do prazo"""

from datetime import date

ano = int(input('Digite o ano de nascimento do jovem: '))

ano_atual = date.today().year

idade = ano_atual - ano

if idade > 18:

    print(f'Você já devia ter se alistado a {idade-18} anos.')

elif idade == 18:

    print('Está na hora de você alistar-se.')

else:

    print(f'Ainda não está na hora de você alistar-se, faltam {18-idade} anos.')
