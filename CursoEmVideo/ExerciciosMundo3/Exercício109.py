"""Modifique as funções que foram criadas no desafio 107 para que elas aceitam um parâmetro a 
mais, informando se o valor retornando por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108"""

import CursoEmVideo.ExerciciosMundo3.pacotes.moeda as moeda

preço = float(input('Digite o preço do produto: '))

print(f'O preço com aumento é: R$ {moeda.aumentar(preço,10, True)}')
print(f'O preço com desconto é: R$ {moeda.diminuir(preço,10, True)}')
print(f'O preço dobrado é: R$ {moeda.dobro(preço, True)}')
print(f'O preço com metade do valor é: R$ {moeda.metade(preço, True)}')
print(f'O preço com metade do valor é: R$ {moeda.moeda(preço)}')
