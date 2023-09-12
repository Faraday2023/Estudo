dados = list()
cpf = list()
pessoas = list()

dados.append('Pedro')
dados.append(25)
cpf.append('120.340.550-79')

pessoas.append(dados[:])
pessoas.append(cpf[:])

print(pessoas[1][0])
