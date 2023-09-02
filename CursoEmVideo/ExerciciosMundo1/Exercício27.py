""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente"""

nome = str(input('Digite o nome da pessoa: ')).strip()

lista = nome.split()

print(lista[0],lista[len(lista)-1])