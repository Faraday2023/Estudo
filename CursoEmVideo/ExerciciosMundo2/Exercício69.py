"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final mostre:

1) Quantas pessoas tem mais de 18 anos
2) Quantos homens foram cadastrados
3) Quantas mulheres tem menos de 20 anos"""

print('-='*30)

maior = 0
quant_homens = 0
quant_mulheres = 0

while True:

    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]

    if idade >= 18:

        maior += 1

    if sexo in 'M':

        quant_homens += 1

    if idade < 20 and sexo in 'F':

        quant_mulheres += 1
    
    escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    while escolha not in 'SN':

        escolha = str(input('Digite novamente. Deseja continuar [S/N]: ')).strip().upper()[0]

    if escolha in 'N':
        break

print('-='*30)
print(f'Existem {maior} pessoas maiores de idade cadastradas.')
print(f'Existem {quant_homens} homens cadastrados.')
print(f'Existem {quant_mulheres} mulheres menores de 20 anos cadastradas.')
