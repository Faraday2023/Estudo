#help(print)
#print(input.__doc__)

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo de contagem
    :return: sem retorno"""

    c = 1
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')

help(contador)

# Parâmetros Opcionais

def somar(a=0,b=0,c=0):
    
    s = a+b+c
    print(f'A soam vale {s}')
somar(3,2,5)
somar(8,4)

"""Os parâmetros opcionais servem para preencher as variáveis quando não declaradas pelo usuário"""