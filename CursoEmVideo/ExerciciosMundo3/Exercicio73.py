""""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

1) Os 5 primeiros colocados
2) Os últimos 4 colocados
3) Times em ordem alfabética
4) Em qual posição está o time da Chapecoense"""

brasileiro2023 = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo','Fluminense',
                  'Bragantino','Atlético Paranaense', 'Fortaleza', 'Atlético MG',
                  'Cuiabá', 'São Paulo','Cruzeiro', 'Corinthians', 'Internacional',
                  'Goiás', 'Bahia', 'Santos', 'Vasco', 'América MG', 'Coritiba')

primeiros = brasileiro2023[0:5]
últimos = brasileiro2023[16:20]
ordem = sorted(brasileiro2023)
santos = brasileiro2023.index('Santos')

print(f'Os cinco primeiros são: {primeiros}')
print(f'Os últimos são: {últimos}')
print(f'Times ordenados: {ordem}')
print(f'O Santos está na posição: {santos}')
