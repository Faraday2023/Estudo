"""Crie um programa chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

import CursoEmVideo.ExerciciosMundo3.pacotes.moeda as moeda

preço = float(input('Digite o preço do produto: '))

print(f'O preço com aumento é: R$ {moeda.aumentar(preço,10)}')
print(f'O preço com desconto é: R$ {moeda.diminuir(preço,10)}')
print(f'O preço dobrado é: R$ {moeda.dobro(preço)}')
print(f'O preço com metade do valor é: R$ {moeda.metade(preço)}')
