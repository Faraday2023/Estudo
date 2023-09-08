"""Refaça o desafio 051, lendo o primeiro termo de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while"""

print('=-='*15)
a1 = int(input('Digite um número inteiro: '))
razão = int(input('Digite a razão da PA: '))
termo = a1
c = 1

print('=-='*15)
print('A progressão aritmética é: ')
while c <= 10:

    print(a1, end = '')
    print(',' if a1 < 10   else '.',end = ' ')
    a1 += razão
    c += 1

#for c in range(a1,décimo+1,razão):
 #   print(c, end = ' ')