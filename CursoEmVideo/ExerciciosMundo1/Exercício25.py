# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

#nome = str(input('Digite o nome da pessoa: ')).strip().upper()
#print('SILVA' in nome)

nome = str(input('Digite o nome da pessoa: ')).strip().upper()

aux = 'SILVA' in nome

if aux == True:
    print('O nome tem Silva')
else:
    print('O nome não tem silva')