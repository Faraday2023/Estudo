"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma
lista. No final mostre:

1) Quantas pessoas foram cadastradas;
2) Uma listagem com as pessoas mais pesadas;
3) Uma listagem com as pessoas mais leves"""

pessoas = list()
dados = list()
cont = 0
aux = 0

while True:

    dados.append(str(input('Digite o nome da pessoa: ')).strip().capitalize())
    dados.append(int(input('Digite o peso da pessoa: ')))

    cont += 1

    if len(pessoas) == 0:
        maior = menor = dados[1]
    
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    escolha = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if escolha in 'Nn':

        print('Obrigado, volte sempre.')
        break

print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso é {maior} kg de: ', end = '')

for p in pessoas:

    if p[1] == maior:
        print(f'{p[0]}', end = ' ')

print()
print(f'O menor peso é {menor} kg de: ', end = '')

for p in pessoas:
    if p[1] == menor:
        aux += 1
        print(f'{p[0]}','.' if aux > 1 else ',', end = ' ')
   