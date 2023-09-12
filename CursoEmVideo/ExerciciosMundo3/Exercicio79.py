"""Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todos os valores únicos digitados, em 
ordem crescente."""

escolha = ''
lista = []

while True:

    num = (int(input('Digite um número: ')))

    if num not in lista:

        lista.append(num)
    else:
        print('Você já cadastrou este número no banco de dados.')

    escolha = str(input('Quer continuar [S/N]: '))
    if escolha in 'Nn':
        break

lista.sort()
print(lista)
