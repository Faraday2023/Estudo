# Faça um programa que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

preço_antigo = float(input('Digite o preço antigo do produto: '))
desconto = 0.05
preço_novo = preço_antigo-(preço_antigo*desconto)
print('O produtor passou de R$ {} para R$ {}'.format(preço_antigo,preço_novo))