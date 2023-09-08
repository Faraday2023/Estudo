"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá 
perguntar se o usuário vai continuar. No final, mostre:

1) Qual é o total gasto na compra
2) Quantos produtos custam mais de R$ 1.000,00
3) Qual é o nome do produto mais barato."""

print('-='*30)

total = 0
maior = 0
barato = 0
c = 0
item_mais_barato = ''

while True:

    nome = str(input('Digite o nome do produto: ')).strip().lower()
    preço = float(input('Digite o preço do produto: '))

    total += preço

    if preço > 1000:

        maior += 1

    if c == 0:

        barato = preço
        item_mais_barato = nome

    if preço < barato:

        barato = preço
        item_mais_barato = nome

    escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    while escolha not in 'SN':

        escolha = str(input('Digite novamente. Deseja continuar [S/N]: ')).strip().upper()[0]

    if escolha in 'N':
        break

    c += 1

print('-='*30)
print(f'O total gasto na compra foi: R$ {total:.2f}.')
print(f'Existem {maior} produtos acima de R$ 1.000,00 .')
print(f'O item mais barato foi a/o {item_mais_barato.capitalize()} que custou R$ {barato:.2f}.')
