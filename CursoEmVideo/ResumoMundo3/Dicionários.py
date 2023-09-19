"""Valor:São os valores que compreendem o dicionário
Chave:São os índices na lista
Item: Valores + chaves"""

filme = {'Título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

dados = dict() #Outra forma de declarar um dicionário
dados['sexo'] = 'M' #Adiciona um valor com uma chave
del dados['sexo'] #Apaga um bloco
lista = []
lista.append(filme)
lista.append(dados)

filme.values() # Pega os valores do dicionário
filme.keys() # Pega as chaves do dicionário
filme.items() # Pega tanto as chaves como os valores

for c, v in filme.items():
    print(c)

print(f'O filme é: {filme["Título"]}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, valor in e.items():
        print(k, valor)