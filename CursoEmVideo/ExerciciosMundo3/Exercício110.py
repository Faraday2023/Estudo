"""Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que 
mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui
"""

import CursoEmVideo.ExerciciosMundo3.pacotes.moeda as moeda

print('-'*30)
preço = float(input('Digite o preço do produto: '))
moeda.resumo(preço,20,12)
