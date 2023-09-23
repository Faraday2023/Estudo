"""Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES 
sorteados pela função anterior"""

from random import randint
from time import sleep

def sorteia(lista):

    for c in range(0,5):
        lista.append(randint(0,10))

def somaPar(lista):
    soma = 0

    for c in lista:
        if c %2 == 0:
            soma += c
    return soma

# Programa Principal

num = list()
sorteia(num)
print(num)
b = somaPar(num)
print(b)
        