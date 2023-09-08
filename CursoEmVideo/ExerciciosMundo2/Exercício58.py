"""Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessários para vencer"""

from random import randint
from time import sleep

aleatório = randint(0,5)
num = 6
palpites = 0

while num !=aleatório:
  print('--'*40)
  num = int(input('Descubra o número que estou pensando. Irei dar uma dica, ela está entre 0 e 5: '))
  palpites += 1
  print('Processando...')
  sleep(1)
  if aleatório == num:
     print(f'Parabéns, você acertou. Utilizando {palpites} tentativas')
  else:
     print('Errou, tente novamente')
     if num > aleatório:
        print('Irei dar uma dica, o número é menor do que o digitado')
     else:
        print('Irei dar uma dica, o número é menor do que o digitado.')
