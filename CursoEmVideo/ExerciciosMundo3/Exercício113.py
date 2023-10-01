"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da 
digitação de um número de tipo inválido. Aproveite e crie também uam função leiaFloat()) com a
mesma funcionalidade."""

def leiaInt(msg):

    while True:

        try:
            entrada = int(input(msg))

        except (ValueError, TypeError):
            print('Por favor, digite números inteiros.')
            continue
        
        except (KeyboardInterrupt):
            return 0

        else:
            return entrada
        
def leiaFloat(msg):

    while True:

        try:
            entrada = float(input(msg))

        except (ValueError, TypeError):
            print('Por favor, digite números inteiros.')

        else:
            return entrada

n = leiaInt('Digite um número inteiro: ')
print(f'O número é: {n}')
