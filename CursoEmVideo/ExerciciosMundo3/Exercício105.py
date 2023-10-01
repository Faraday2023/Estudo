"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai 
retornar um dicionário com as seguintes informações:

1) Quantidade de notas;
2) A maior nota;
3) A menor nota;
4) A média da turma;
5) A situação(opcional).

OBS.: Adicione também as docs strings"""

def notas(*num, sit = True):

    """
    -> Calcula a situação de um aluno
    :param num: recebe uma tupla com vários números
    :param sit: mostra a situação do aluno, caso verdadeira
    :return: retorna um dicionário com a situação do aluno

    """

    maior = menor = soma =  0 # Variáveis locais
    dict = {} 

    for pos, itens in enumerate(num): # laço para varredura da tupla
        if pos == 0: # caso seja a primeira leitura, maior e menor recebem o primeiro valor
            maior = menor = itens
        else:
            if itens > maior: # se não for a primeira leitura e itens for maior do que maior, maior recebe itens
                maior = itens

            if itens < menor: # se itens for menor do que menor, itens recebe menor
                menor = itens
        soma += itens # somatório de todas as notas
    
    média = soma/len(num) # cálculo da média

    dict['Maior'] = maior # Adicionando maior nota ao dicionário
    dict['Menor'] = menor # Adicionando menor nota ao dicionário
    dict['Média'] = média # Adicionando a média no dicionário

    if sit == True: # Se sit receber True, o dicionário terá um índice situação do aluno

        if média >=6 and média <7:
            dict['Situação'] = 'Razoável'

        elif média >=7:
            dict['Situação'] = 'Boa'

        elif média < 6:
            dict['Situação'] = 'Ruim'

    return dict # A função retorna o dicionário


# Programa Principal

aluno = notas(7,7,7,sit = True) # Chamada da função ou instância
print(aluno) # Exibição
help(notas) # Help da função
