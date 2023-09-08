"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se 
elas podem ou não formar um triângulo"""

"""Acrescentar o recurso identificador:

1) Equilátero - Todos os lados iguais
2) Isósceles - Dois lados iguais
3) Escaleno - Todos os lados diferentes"""

"""Teoria: Para formar um triângulo a condição abaixo precisa ser respeitada:
|b-c|<a<b+c
|a-c|<b<a+c
|a-b|<c<a+b"""

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:

    print(f'As retas a: {a}m, b: {b}m, c: {c}m, formam um triângulo')

    if a == b  and b == c :
        print('O triângulo é equilátero.')
    elif a == b != c or a == c != b or b == c != a:
        print('O triângulo é isósceles.')
    else:
        print('o triângulo é escaleno')

else:
    print(f'As retas a: {a}m, b: {b}m, c: {c}m, não formam um triângulo')