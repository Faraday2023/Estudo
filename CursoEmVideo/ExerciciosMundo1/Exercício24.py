# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo

#cidade = str(input('Digite o nome da cidade: ')).strip()
#print(cidade[:5].upper() == 'SANTO')

cidade = str(input('Digite o nome da cidade: ')).strip().upper()

aux = 'SANTO' in cidade

if aux == True:

    aux2 = cidade.find('SANTO')

    if aux2 == 0:
        print('A cidade começa com o nome Santo')
    else:
        print('A cidade tem o nome santo, porém, não começa com ele')
else:
    print('A cidade não tem o nome Santo.')