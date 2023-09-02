"""Crie um programa que leia o nome completo de uma pessoa e mostre:

1) O nome com todas as letras maiúsculas e minúsculas
2) Quantas letras ao todo (sem considerar espaços)
3) Quantas letras tem o primeiro nome"""

nome = str(input('Digite o nome completo da pessoa: ')).strip()

print('O nome maiúsculo é: {}'. format(nome.upper()))
print(f'O nome minúsculo é: {nome.lower()}')
print('O nome tem tamanho de: {}'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {}'.format(len(nome.split()[0])))