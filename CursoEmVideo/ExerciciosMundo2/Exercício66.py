"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles desconsiderando o flag"""

c = 0
soma = 0

while True:

    num = int(input('Digite um número, para parar só digitar [999]: '))

    if num == 999:
        break
    soma += num
    c += 1

print(f'A soma foi {soma}, com {c} valores digitados')
