"""Crie um programa que vai ler vários números e colocar em uma lista. Depois 
disso, crie duas listas extras que vão conter apenas só valores pares e os 
valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas"""

lista = []
lista_par = []
lista_ímpar = []

while True:

    num = int(input('Digite um número: '))

    lista.append(num)


    escolha = str(input('Quer continuar [S/N]: ')). strip().upper()[0]

    if escolha in 'Nn':
        print('Obrigado, volte sempre.')
        break

for itens in lista:

    if itens %2 == 0:
         lista_par.append(itens)
    elif itens %2 == 1:
         lista_ímpar.append(itens)
    else:
        print('Número inválido.')

print(lista)
print(lista_par)
print(lista_ímpar)
