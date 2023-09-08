""""Crie um programa qeu tenha uam tupla única com nomes de produtos e seus 
respectivos preços, na sequência. No final, mostre uma listagem de preços, 
organizando os dados em forma tabular"""

listagem = ('Lápis',1.00,'Borracha',1.5, 'Caneta',2.00,'Caderno',
             10.00,'Estojo',5.00)

print('-'*40)
print(f'{"Lista de Materiais":^40}')
print('-'*40)
for posição in range(0, len(listagem)):

    if posição %2 == 0:
        print(f'{listagem[posição]:.<30}', end = '')
    else:
        print(f'R$ {listagem[posição]: >5.2f}')
print('-'*40)