"""Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado. Crie 
uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma
validação de dados para aceitar apenas valores que sejam monetários."""

from pacotes import dado, moeda

print('-'*30)
preço = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(preço,20,12)
