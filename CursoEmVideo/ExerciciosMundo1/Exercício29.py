"""Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$ 7,00 por cada km acima do limite"""

from time import sleep

velocidade = int(input('Digite a velocidade do carro: '))

print('\nProcessando...')
sleep(2)

if velocidade > 80:

    excedente = velocidade - 80

    print('Voce foi multado e deve pagar uma multa de R$: {:.2f}'.format(excedente*7))
else:
    print('Parabéns, está dirigindo dentro dos limites da via')

