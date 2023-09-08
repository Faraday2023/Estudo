"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços"""

print('-'*50)
frase = str(input('Digite uma frase: ')).strip().lower()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
#inverso = junto[::-1]
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('-'*50,'\n',f'Palavra inversa: {inverso.capitalize()}, palavra digitada: {frase.capitalize()}')

if inverso == junto:
    print('-'*50,'\n','A palavra é um palíndromo.')
else:
    print('-'*50,'\n','A palavra não é um palíndromo.')
print('-'*50)