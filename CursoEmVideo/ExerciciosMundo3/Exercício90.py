"""Faça um programa que leia nome e média de um aluno, guardando também a situação em
um dicionário. No final, mostre o conteúdo da estrutura na tela"""

dic = dict()

for c in range(0,1):

    dic['nome'] = str(input('Digite o nome do aluno: ')).strip().lower()
    dic['média'] = float(input('Digite a média do aluno: '))

    if dic['média'] < 6:
        dic['situação'] = 'Reprovado'

    elif dic['média'] == 6:
        dic['situação'] = 'Recuperação'

    elif dic['média'] >= 7:
        dic['situação'] = 'Aprovado'
    
    print(dic)
    