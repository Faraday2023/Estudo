"""Faça um programa que tenha uma função chamada contador(), que receba três 
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através 
da função criada: """

from time import sleep

def contador(início, fim, passo):
    print('-'*30)
    if passo < 0:
               passo = passo * -1
               
    print(f'Contagem de {início} até {fim} de {passo} em {passo}.')

    if início < fim:

        count = início

        while count <= fim:
           print(count, end = ' ', flush=True)
           sleep(0.5)
           count += passo
        print()

    else:
       
       count = início
       
       while count >= fim:
           print(count, end = ' ', flush=True)
           sleep(0.5)
           count -= passo
       print()

contador(1,10,1)
contador(10,0,2)

print(f'Escolha sua contagem personalizada')

início = int(input('Digite o começo do passo: '))
fim = int(input('Digite o fim do passo: '))
passo = int(input('Digite o passo do laço: '))
contador(início, fim,passo)
