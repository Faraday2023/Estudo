# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random

Aluno1 = input('Digite o nome do primeiro aluno: ')
Aluno2 = input('Digite o nome do segundo aluno: ')
Aluno3 = input('Digite o nome do terceiro aluno: ')
Aluno4 = input('Digite o nome do quarto aluno: ')

turma = [Aluno1, Aluno2, Aluno3, Aluno4]

Aluno_Sorteado = random.choice(turma)
print(Aluno_Sorteado)