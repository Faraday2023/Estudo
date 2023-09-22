"""Faça um programa que tenha uma função chamada área(que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno."""

def área(largura,comprimento):
    area_terreno = largura * comprimento
    print(f'A largura é: {largura} e o comprimento é: {comprimento}')
    print(f'Área do terreno: {area_terreno}')

# Programa Principal
largura = int(input('Digite a largura do terreno: '))
comprimento = int(input('Digite o comprimento do terreno: '))
área(largura,comprimento)
