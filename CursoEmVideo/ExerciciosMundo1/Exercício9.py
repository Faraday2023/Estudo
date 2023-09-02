# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número: '))

print(""" Sua tabuada é:
      1) {0}*1 = {1}
      2) {0}*2 = {2}
      3) {0}*3 = {3}
      4) {0}*4 = {4}
      5) {0}*5 = {5}
      6) {0}*6 = {6}
      7) {0}*7 = {7}
      8) {0}*8 = {8}
      9) {0}*9 = {9}
      10) {0}*10 = {10}""".format(num,num*1,num*2,num*3,num*4,num*5,num*6,num*7,num*8,num*9,num*10))