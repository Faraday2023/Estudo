"""Crie um programa que tenha função leiaInt(), que vai funcionar de forma semelhante á função 
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico
Ex:
n = leiaInt('Digite um n')"""

def leia_int(msg):
     while True:
          num = str(input(msg))
          if num.isnumeric() == True:
               break
          else:
               print('Erro, digite um número.')
     return num
     

# Programa Principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
