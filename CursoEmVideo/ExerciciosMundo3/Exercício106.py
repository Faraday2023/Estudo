"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa
se encerrará.

OBS.: use cores"""

from time import sleep

cores = {

    'padrão': '\033[m',
    'vermelho': '\033[0:30:41m',
    'verde': '\033[0:30:42m', 
    'amarelo': '\033[0:30:43m', 
    'azul' : '\033[0:30:44m ',  
    'roxo' : '\033[0:30:46m',
    'branco': '\033[7:30m'
    
}

def ajuda(com):
    título(f'Acessando o manual do comando {com}', 'amarelo')
    help(com)
    print(cores['padrão'], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cores['padrão'], end='')
    sleep(1)


# Programa Principal

comando = ''

while True:
    título('Sistema de ajuda Python', 'verde')
    comando = str(input('Função ou biblioteca: '))

    if comando.upper() == 'FIM':
        break
    
    else:
        ajuda(comando)
print('Até logo')
