# Faça um programa que leia o nome de quatro alunos e sorteei a ordem da apresentação de trabalho

from random import shuffle

Aluno1 = str(input('Digite o nome do aluno 1: '))
Aluno2 = str(input('Digite o nome do aluno 2: '))
Aluno3 = str(input('Digite o nome do aluno 3: '))
Aluno4 = str(input('Digite o nome do aluno 4: '))

lista = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle(lista)
print(lista)

    