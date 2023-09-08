"""Desenvolva um programa  que leia o primeiro termo e a razão de uma PA. No final,
 mostre os 10 primeiros termos dessa progressão."""

a1 = int(input('Digite um número inteiro: '))
razão = int(input('Digite a razão da PA: '))
décimo = a1 + (10-1)*razão
print('A progressão aritmética é: ')

for c in range(a1,décimo+1,razão):
    print(c, end = ' ')