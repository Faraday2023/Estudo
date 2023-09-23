"""Faça um programa que tenha um função chamada maior(), que receba vários parâmetros 
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual 
deles é o maior"""

from time import sleep

def maior(*num):
    maior_num=cont=0
    print('-'*40)
    print(f'Foram informados os valores: ', end='')
    for c in num:
        print(f'{c}', end=' ',flush=True)
        sleep(0.5)
        if c == 0:
            maior_num = c
        else:
            if c > maior_num:
                maior_num = c
        cont +=1
    print()
    print(f'Quantidade valores analisados: {cont}')
    return maior_num

a = maior(5,4,8,2,1)
print('-'*40)
print(f'O maior valor foi: {a}')
print('-'*40)