"""Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga
mostrar os valores como um valor monetário formatado"""

import CursoEmVideo.ExerciciosMundo3.pacotes.moeda as moeda

preço = float(input('Digite o preço do produto: '))

print(f'O preço com aumento é: R$ {moeda.moeda(moeda.aumentar(preço,10))}')
print(f'O preço com desconto é: R$ {moeda.moeda(moeda.diminuir(preço,10))}')
print(f'O preço dobrado é: R$ {moeda.moeda(moeda.dobro(preço))}')
print(f'O preço com metade do valor é: R$ {moeda.moeda(moeda.metade(preço))}')
print(f'O preço com metade do valor é: R$ {moeda.moeda(preço)}')
