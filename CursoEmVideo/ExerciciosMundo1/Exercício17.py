# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math

x = float(input("Digite o cateto adjacente: "))
y = float(input('Digite o cateto oposto: '))
print('O triângulo tem hipotenusa {:.2f}'.format(math.hypot(x,y)))