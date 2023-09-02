"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se 
elas podem ou não formar um triângulo"""

"""Teoria: Para formar um triângulo a condição abaixo precisa ser respeitada:
|b-c|<a<b+c
|a-c|<b<a+c
|a-b|<c<a+b"""

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:

    print(f'As retas a: {a}m, b: {b}m, c: {c}m, formam um triângulo')

else:
    print(f'As retas a: {a}m, b: {b}m, c: {c}m, não formam um triângulo')