"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um
sistema de visualização do aproveitamento de cada jogador"""

dic = {}
list_final = []
lista = []
total_gols = 0

while True:
    
    print('-'*60)
    dic['Nome'] = str(input('Digite o nome do jogador: '))
    Quantidade_partidas = int(input('Digite a quantidade de partidas jogadas: '))

    for c in range(1, Quantidade_partidas+1):
        lista.append(int(input(f'Digite quantos gols foram feitos na partida: {c}: ')))
        total_gols += lista[c-1]
        dic['Quant_gols'] = lista[:]

    dic['Total_gols'] = total_gols

    list_final.append(dic.copy())
    dic.clear()
    lista.clear()
    total_gols = 0

    escolha = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if escolha in 'Nn':
        break

print('-'*60)

for pos, item in enumerate(list_final):
    print(f'{pos} - {item}')

print('-'*60)
print(f'{"Cód":^3}|{"Nome":^14}|{"Gols":^16}|{"Total":^14}|')

for k, v in enumerate(list_final):
    print(f'{k:^3}', end='')
    for d in v.values():
        print(f'{str(d):^16}', end='')
    print()
    
print('-'*60)

while True:

    visualização = int(input('Deseja visualizar o desempenho de qual jogador (999 para parar): '))

    if visualização == 999:
        break

    if visualização > len(list_final) - 1:
        print('Erro, digite corretamente.')

    else:
        print('-'*60)
        print(f'O jogador {list_final[visualização]["Nome"]} tem os seguintes dados: ')

        for c, gols in enumerate(list_final[visualização]['Quant_gols']):

            print(f'No jogo {c+1} ele fez: {gols} gols')
