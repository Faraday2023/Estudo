"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento
 de um atleta e mostre sua categoria, de acordo com a idade:

1) Até 9 anos: Mirim
2) Até 14 anos: infantil
3) Até 19 anos: Junior
4) Até 25 anos: Sênior
5) Acima: Master"""

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year

idade_atleta = ano_atual - ano_nascimento

if idade_atleta <= 9:
    print('Mirim.')

elif idade_atleta > 9 and idade_atleta <= 14:
    print('Infantil.')

elif idade_atleta > 14 and idade_atleta <= 19:
    print('Junior')

elif idade_atleta > 19 and idade_atleta <= 25:
    print('Sênior')
else:
    print('Master')