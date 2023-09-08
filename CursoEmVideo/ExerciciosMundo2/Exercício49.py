"""Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,só que
 agora utilizando um laço for"""

num = int(input('Digite o número que deseja ver a tabuada: '))
print('-'*15)
for c in range(1, 11):
    resultado = num*c
    print(f'{num} * {c:2} = {resultado}')