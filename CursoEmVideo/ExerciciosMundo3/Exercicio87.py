"""Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha."""

matriz = [[],[],[]]
aux = 0
soma = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o elemento {l}{c}: ')))

        if matriz[l][c] %2 == 0:
            aux += matriz[l][c]

        if c == 2:
            soma += matriz[l][2]

        if l == 1:
            if c == 0:
                aux_maior = matriz[1][c]
            else:
                if matriz[1][c] > aux_maior:
                    aux_maior = matriz[1][c]
            
print('-'*25)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma dos números pares é: {aux}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {aux_maior}')
print('-'*25)

"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
aux = 0
soma = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o elemento {l}{c}: '))

        if matriz[l][c] %2 == 0:
            aux += matriz[l][c]

        if c == 2:
            soma += matriz[l][2]

        if l == 1:
            if c == 0:
                aux_maior = matriz[1][c]
            else:
                if matriz[1][c] > aux_maior:
                    aux_maior = matriz[1][c]
            
print('-'*25)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma dos números pares é: {aux}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {aux_maior}')
print('-'*25)"""
