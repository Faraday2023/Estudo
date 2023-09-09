"""Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, mostre:

A) Quantos números foram digitados;
B) A lista de valores, ordenados de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista"""

lista = list()
c = 0

while True:

    num = int(input('Digite um número: '))
    lista.append(num)

    escolha = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if escolha in 'Nn':
        print('Obrigado, volte sempre.')
        break

    c += 1

lista.sort(reverse = True)

"""for num in lista:
    if num == 5:
        a = True
    else:
       a = False"""
if 5 in lista:
    a = True
else:
    a = False

print(f'Foram digitados {c + 1} valores.')
print(f'Lista em ordem decrescente: {lista}')
print(F'O valor 5 foi digitado: {a}')