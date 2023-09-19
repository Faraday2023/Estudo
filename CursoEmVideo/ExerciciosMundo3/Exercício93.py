"""Crie um programa qeu gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato"""

dic = {}
lista = []
total_gols = 0

print('-'*60)
dic['Nome'] = str(input('Digite o nome do jogador: '))
dic['Quantidade_partidas'] = int(input('Digite a quantidade de partidas jogadas: '))

for c in range(1, dic['Quantidade_partidas']+1):
    lista.append(int(input(f'Digite quantos gols foram feitos na partida: {c}: ')))
    total_gols += lista[c-1]
    dic['Quant_gols'] = lista[:]

dic['Total_gols'] = total_gols
print('-'*60)
print(dic)
print('-'*60)

for pos, item in dic.items():
    print(f'{pos} - {item}')

print('-'*60)
print(f'O jogador {dic["Nome"]} jogou {dic["Quantidade_partidas"]} partidas')
print('-'*60)

for i, item in enumerate(lista):
    print(f'Na partida: {i+1} - Fez: {item} gols')
print(f'Com total de {total_gols} gols.')
