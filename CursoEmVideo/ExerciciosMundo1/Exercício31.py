"""Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o 
preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para 
viagens mais longas"""

distância = float(input('Digite a distância do lugar de origem ao de destino: '))

if distância <=200:
    print('O valor da viagem ficou: R$ {}'.format(distância*0.5))

else:
    print('Preço Promo - O valor da viagem ficou: R$ {}'.format(distância*0.45))