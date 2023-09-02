# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angle = int(input('Digite o ângulo qualquer em graus: '))
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print(f'O ângulo digitado foi: {angle}, o seno dele é: {sen:.2f}, o cos é: {cos:.2f}, a tan: {tan:.2f}')