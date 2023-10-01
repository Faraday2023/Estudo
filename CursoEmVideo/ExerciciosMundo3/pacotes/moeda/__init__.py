# Programa com Funções

def aumentar(preço=0, taxa=0, formato = False):
    res = preço + (preço*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0, taxa=0, formato= False):
    res = preço - (preço*taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato = False):
    res = preço*2
    return res if not formato else moeda(res)

def metade(preço=0, formato = False):
    res = preço/2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')

def resumo(preço,a=10,d=5):

    print('-'*45)
    print('Resumo'.center(45))
    print('-'*45)

    print(f'O preço com aumento é: \t\t{aumentar(preço,a, True)}')
    print(f'O preço com desconto é: \t{diminuir(preço,d, True)}')
    print(f'O preço dobrado é: \t\t{dobro(preço, True)}')
    print(f'O preço com metade do valor é: \t{metade(preço, True)}')
    print(f'O preço com metade do valor é: \t{moeda(preço)}')

    print('-'*45)