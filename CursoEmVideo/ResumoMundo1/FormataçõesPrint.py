# Formas de formatação do print

x = input('Digite uma palavra: ')
y = input('Digite um número: ')

print('\nPalava digitada é {0} o número {1}'.format(x, y))
print(f'Curso de {x} é {y}')

print(type(x))
print(x.isnumeric())
print(x.isalnum())
print(x.isalpha())
print(x.islower())
print(x.isupper())