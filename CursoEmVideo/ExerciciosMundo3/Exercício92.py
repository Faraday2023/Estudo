"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, 
o dicionário receberá também o ano de contratação e o salário. Calcule e  acrescente,
além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date

aposentar = 65

dic = {}

dic['nome'] = str(input('Digite o nome da pessoa: ')).strip().lower().capitalize()
dic['ano_nascimento'] = int(input('Digite o ano de nascimento: '))

dic['carteira'] = int(input('Digite o n° da CTPS: '))

if dic['carteira'] != 0:
    dic['ano_contratação'] = int(input('Digite o ano de contratação: '))
    dic['salário'] = float(input('Digite o salário do colaborador: '))

dic['idade'] = date.today().year - dic['ano_nascimento']
dic['aposentadoria'] = aposentar - dic['idade']

for pos, itens in dic.items():
    print(f'{pos} é: {itens}.')
