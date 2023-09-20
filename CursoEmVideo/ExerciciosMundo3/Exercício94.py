"""Crie um programa qeu leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, 
mostre:

A) Quantas pessoas cadastradas
B) A média de idade
C) Uma lista com mulheres
D) Uma lista com idade acima da média"""

dic_pessoas = {}
dic_aux = {}
lista_final = []
lista_mulher = []
lista_maior_média = []
soma = 0

while True:

    dic_aux['nome'] = str(input('Digite o nome da pessoa: ')).strip().lower().capitalize()
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().lower().upper()

    while sexo not in 'MF':
        print('Por favor, digite corretamente.')
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().lower().upper()

    dic_aux['sexo'] = sexo
    dic_aux['idade'] = int(input('Digite a idade da pessoa: '))

    dic_pessoas = dic_aux.copy()

    escolha = str(input('Deseja continuar cadastrando [N/S]: ')).strip().lower().upper()[0]

    while escolha not in 'NS':

        print('Por favor, digite corretamente.')
        escolha = str(input('Deseja continuar cadastrando [N/S]: ')).strip().lower().upper()[0]
    
    dic_aux.clear()

    lista_final.append(dic_pessoas)

    if escolha in 'Nn':
        break

print('-'*60)
print(lista_final)
print('-'*60)
tamanho = len(lista_final)

for pos, item in enumerate(lista_final):

     for i, valores in item.items():
         if i == 'idade':
             soma += valores
             média = soma/tamanho 

             if item['idade'] >= média:
                 lista_maior_média.append([item['nome'],item['sexo'], item['idade']])

         if i == 'sexo':
             if valores == 'F':
                 lista_mulher.append(item['nome'])

print(f'Quantidade de pessoas cadastradas: {tamanho}')
print(f'Nome das mulheres: {lista_mulher}')
print(f'Media das idades: {média}')
print(f'Lista com pessoas acima da idade média: {lista_maior_média}')
