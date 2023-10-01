"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros 
opcionais:o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz 
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado 
corretamente"""

def ficha(nome = '<Desconhecido>', gols = 0): # parâmetro opcional
    print('-'*30)
    print(f'O jogador {nome} fez {gols} gols')
    print('-'*30)


# Programa Principal

print('-'*30)
nome_jogador = str(input('Digite o nome do jogador: '))
print('-'*30)
gols_jogador = str(input(f'Digite quantos gols {nome_jogador} fez: '))
ficha(nome_jogador, gols_jogador)

if gols_jogador.isnumeric(): # verificação se a string é um número
    gols_jogador = int(gols_jogador) # caso seja passa a ser um inteiro

else:
    gols_jogador = 0 # se não for numérico, recebe "0"

if nome_jogador.strip() == '': # Caso o nome do jogador sem os espaços no fim e começo for igual a nada, a ficha é instanciada só o número de gols
    ficha(gols = gols_jogador)
else:
    ficha(nome = nome_jogador, gols = gols_jogador) # Se não instancia nome e quantidade de gols
