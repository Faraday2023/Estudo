"""Faça um programa que leia uma frase pelo teclado e mostre:
   
   1) Quantas vezes aparece a letra a
   2) Em que posição ela aparece pela primeira vez
   3) Em que posição ela aparece na última vez"""

frase = str(input('Digite uma frase: ')).strip().lower()

print(frase.count('a'),frase.find('a'), frase.rfind('a'))