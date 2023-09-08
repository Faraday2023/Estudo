"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O
programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores"""

c = 0
maior = 0
menor = 0
soma = 0
escolha = ' '

print('-='*20)

while escolha not in 'Nn':

    num = int(input('Digite um número: '))

    soma += num

    if c == 0:
        maior = num
        menor = num
    
    if num > maior:
        maior = num

    if num < menor:
        menor = num
    
    escolha = str(input('Quer continuar: [S/N]: ')).strip()

    c += 1

média = soma/c

print('-='*20)
print(f'A média dos {c} valores digitados é: {média}')
print(f'O maior valor é: {maior} e o menor é: {menor}')
