"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela, com a formatação correta"""

matriz = [[],[],[]]
aux = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o elemento {l}{c}: ')))

        if matriz[l][c] %2 == 0:
            aux += matriz[l][c]

print('-'*25)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

print('-'*25)
print(aux)
