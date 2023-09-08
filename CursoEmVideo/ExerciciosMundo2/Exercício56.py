"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre:

1) A média de idade do grupo
2) Qual é o nome do homem mais velho
3) Quantas mulheres têm menos de 20 anos"""

print('-'*70)

soma = 0
mais_velho = 0
nome_mais_velho = ''
idade_mulher = 20
quant_mulher = 0

for pessoas in range(1,3):

    nome = str(input(f'Digite o nome da pessoa {pessoas}: ')).strip().lower()
    idade = int(input(f'Digite a idade da pessoa {pessoas}: '))
    sexo = str(input('Digite o sexo da pessoa [F/M]: ')).strip().lower()

    soma += idade
    quant = pessoas

    if pessoas == 1 and sexo == 'm': # ou sexo in 'Mm' para evitar erro do usuário

        mais_velho = idade 
        nome_mais_velho = nome
    
    if idade > mais_velho and sexo == 'm':

        mais_velho = idade
        nome_mais_velho = nome
    
    if sexo == 'f' and idade < idade_mulher:

        quant_mulher += 1

média = soma/quant

print('-'*70)
print(f"""A média das idades é: {média}, o homem mais velho se chama: {nome_mais_velho.capitalize()} e
existe {quant_mulher} mulher com menos de 20 anos.""")
print('-'*70)