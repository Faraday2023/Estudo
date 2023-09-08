"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre 
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""

print('-'*50)

from datetime import date

maior_de_idade = 0
menor_de_idade = 0
ano_base = date.today().year

for pessoas in range(1,8):

    nascimento = int(input(f'Digite o ano de nascimento da pessoa {pessoas}: '))
    saldo = ano_base - nascimento

    if saldo >=18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print('-'*50)
print(f'Existem {maior_de_idade} pessoas maior de idade e {menor_de_idade} menor de idade')