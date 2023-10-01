"""Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando"""

from pacotes import moeda

print('-'*30)
preço = float(input('Digite o preço do produto: '))
moeda.resumo(preço,20,12)
