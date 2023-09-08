"""Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma
 mensagem no final, de acordo com a média atingida:

1) Média abaixo de 5.0: Reprovado
2) Média entre 5.0 e 6.9 Recuperação
3) Média 7.0 ou superior: Aprovado"""

import numpy

print('-'*40)
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
print('-'*40)
list = [nota1, nota2]

media = numpy.mean([list])

if media < 5:

    print(f'Reprovado com média {media}.')

elif media > 5 and media < 6.9:

    print(f'Recuperação com média {media}')

else:

    print(f'Aprovado com média {media}.')