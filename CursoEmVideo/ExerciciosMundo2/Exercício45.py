"""Crie um programa que faça o computador jogar jokenpô com você."""

from random import randint
from time import sleep

computador = randint(1,3)
itens = (' ','Pedra', 'Papel', 'Tesoura')
         
print('-'*40,"""\n1) Pedra\n2) Papel\n3) Tesoura""",'\n','-'*40)
jogador = int(input('Digite uma opção: '))

sleep(1)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')

if jogador == computador:

    print('-'*40,'\n','Empate')

elif jogador  - computador == -1 or jogador - computador == 2:

    print('-'*40,'\n','Computador ganhou')

elif jogador - computador ==  1 or jogador - computador == -2:

    print('-'*40,'\n','Jogador ganhou')

else:

    print('-'*40,'\n','Jogada inválida')

print('-'*40,'\n',f'Computador jogou: {itens[computador]} , Jogador jogou: {itens[jogador]}')