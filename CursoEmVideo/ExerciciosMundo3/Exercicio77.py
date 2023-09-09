"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso você deve mostrar, para cada palavra, quais são as suas vogais"""

tupla = ('astro', 'brasil', 'casa', 'dado', 'estrada', 'força', 
         'gato', 'hospital', 'iguana', 'ovo','faca','gosto')

print('-'*47)
for palavra in tupla:
    print(f'Na palavra {palavra} temos as vogais: ',end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra},', end =' ')
    print('\n', end = '')
    print('-'*47)
