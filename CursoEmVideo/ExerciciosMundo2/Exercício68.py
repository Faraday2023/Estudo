"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou 
no final do jogo"""

from random import randint

print('-='*30)
c = 0
total = 0

while True:

    computador = randint(1,10)
    jogador = int(input('Digite um número: '))
    total = computador + jogador

    escolha = str(input('Você quer o resultado Par ou ímpar [P/I]: ')).strip().upper()[0]
    print('-='*30)

    if escolha in 'P':

        if total % 2 == 0:

            print('Você Venceu')
            print('-='*30)

            c += 1
        else:

            print('Você Perdeu.')
            break
    
    if escolha in 'I':

        if total % 2 != 0:

            print('Você Venceu')
            print('-='*30)

            c += 1
        
        else:

            print('Você Perdeu')
            break

print('-='*30)
print(f'Fim de jogo. Você ganhou {c} vezes.')
