# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

num = float(input('Digite uma medida em metros: '))

print('O valor digitado em m: {}, cm: {}, mm: {}'.format(num,num*100,num*1000))