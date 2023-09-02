"""Escreva um programa que faça o computador "pensar em um número inteiro entre 
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu"""

from random import randint
from time import sleep

aleatório = randint(0,5)

num = 6

while num !=aleatório:
  print('--'*40)
  num = int(input('Descubra o número que estou pensando. Irei dar uma dica, ela está entre 0 e 5: '))
  print('Processando...')
  sleep(2)
  if aleatório == num:
     print('Parabéns, você acertou.')
  else:
     print('Errou, tente novamente')

