"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o 
primeiro que indique o número a calcular e o outro chamado show, que será um valor
lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do 
fatorial"""

def fatorial(num, show=False):
    
    """
    -> Calcula o fatorial de um número
    :param num: O número que irá ser calculado o fatorial
    :param show: (Opcional) Mostrar ou não os cálculos
    :return: retorna o fatorial
    """
    f = 1
    for c in range(num, 0,-1):
        if show == True:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

print(fatorial(5,show = False))
#print(help(fatorial))
