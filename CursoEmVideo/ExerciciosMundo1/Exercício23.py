# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int(input('Digite um número: '))
unidade = num%10
dezena = (num//10)%10
centena = (num//100)%10
milhar = (num//1000)%10

print('Milhar: {}, centena: {}, dezena: {}, unidade: {}'.format(milhar, centena, dezena, unidade))