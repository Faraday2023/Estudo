"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

cores = {

    'padrão': '\033[m',
    'azul': '\033[34m',
    'vermelho': '\033[31m', 
    'verde': '\033[32m', 
    'azul' : '\033[34m ',  
    'ciano' : '\033[36m', 
    'magenta' : '\033[35m', 
    'amarelo' : '\033[33m', 
    'preto' : ' \033[30m',  
    'branco' : '\033[37m',  
    'negro' : '\033[1m ', 
    'reverso' : '\033[2m' 

}

tot = 0
num = int(input('Digite um número: '))

for c in range(1, num + 1):
    
    if num % c == 0:
        print (cores['vermelho'], end = ' ')
        tot += 1
    
    else:
        print (cores['amarelo'], end = ' ')

    print (c, cores['padrão'],end = ' ')  

if tot > 3:
    print(f'\nO número: {num} não é primo, pois é divisível por: {tot} números')
else:
     print(f'\nO número: {num} é primo, pois é divisível por: {tot} números')