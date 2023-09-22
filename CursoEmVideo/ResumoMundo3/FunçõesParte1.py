def mostraLinha():
    print('-'*30)

def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

def contador(*num): # O * permite que usuário passe vários parâmetros e jogue dentro de num - Desempacotamento
    for valor in num:
        print(valor, end = ' ')
    print('Fim')

def contador2(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


# Programa Principal
mostraLinha()
print(f'{"Jogo":^30}')
mostraLinha()

mensagem(f'{"Sistema de Alunos":^30}')
soma(2,3)
mostraLinha()
soma(a=3, b=5)

mostraLinha()
contador(1,2,3,4)
mostraLinha()

contador2(4,3,2,1)
mostraLinha()

valores = [1, 2, 3, 4, 5]
dobra(valores)
