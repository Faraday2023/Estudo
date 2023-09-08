"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
 tupla. No final, mostre:

1) Quantas vezes apareceu o valor 9
2) Em que posição foi digitado o primeiro valor 3
3) Quais foram os números pares"""

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'Apareceram {tupla.count(9)} valores 9')
if 3 in tupla:
    print(f'O primeiro três aparaceu na posição: {tupla.index(3)+1}')
else:
    print('Não existe o 3 na tupla')

print(f'Elemento par da tupla: ', end = '')

for n in tupla:
    if n %2 == 0:
        print(n, end = ' ')
