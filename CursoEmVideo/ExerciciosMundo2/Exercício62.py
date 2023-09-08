"""Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns
 termos. O programa encerra quando ele disser que quer mostrar 0 termos."""

print('=-='*15)
a1 = int(input('Digite um número inteiro: '))
razão = int(input('Digite a razão da PA: '))
termo = a1
c = 1
mais_termos = 10
total = 0
print('=-='*15)
print('A progressão aritmética é: ')

while mais_termos !=0:

    total  += mais_termos

    while c <= total:

        print(a1, end = '')
        print(',' if a1 < 10   else '.',end = ' ')
        a1 += razão
        c += 1

    mais_termos = int(input('\nDeseja adicionar mais termos: '))

print(f'Termos adicionados {total}.')
