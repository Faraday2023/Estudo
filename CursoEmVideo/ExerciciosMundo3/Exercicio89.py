"""Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita que 
o usuário possa mostrar as notas de cada aluno individualmente"""

lista = list()
c = 1
opção = 0

while True:

    nome = str(input(f'Digite o nome do aluno {c}: ')).strip().lower()
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    média = (nota1+nota2)/2

    lista.append([nome, [nota1, nota2], média])

    escolha = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if escolha in 'Nn':
        break

print('-'*40)
print(f'{"Pos":^7}|{"Nome":^25}|{"Média":^7}')

for pos, itens in enumerate(lista):
   print(f'{pos+1:^7}|{itens[0].capitalize():^25}|{itens[2]:^7}')

while opção != 999:

    opção = int(input('Deseja mostrar as notas de qual aluno (999 interrompe o programa): ')) - 1
    tam = len(lista[0]) 
    print(tam)

    if opção <= tam:

        print(f'O aluno: {lista[opção][0]} tirou as notas: {lista[opção][1]}')
