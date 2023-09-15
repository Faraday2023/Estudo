"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados so valores pares e ímpares. No final,  
mostre os valores pares e ímpares em ordem crescente"""

"""""
ListaImpar = []
ListaPar = []

for c in range(1,8):

    num = int(input('Digite um número: '))

    if num % 2 == 0:
        ListaPar.append(num)

    else:
        ListaImpar.append(num)

ListaImpar.sort()
ListaPar.sort()
ListaÚnica = [ListaImpar] + [ListaPar]

print(ListaImpar)
print(ListaPar)
print(ListaÚnica)"""

"""Se não precisar da lista original, pode usar o método sort, a função sorted cria uma nova 
lista"""

Lista = [ [], [] ]

for c in range(1,8):

    num = int(input('Digite um número: '))

    if num % 2 == 0:
        Lista[0].append(num)

    else: 
        Lista[1].append(num)

Lista[0].sort()
Lista[1].sort()

print(Lista)

