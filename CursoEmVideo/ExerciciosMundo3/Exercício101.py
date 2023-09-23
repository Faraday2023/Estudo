"""Crie um programa que tenha uma função chamada voto() que vai receber  como
parâmetro o ano de nascimento de uma pessoa, retornando um valor  literal indicando se
uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições"""

def voto(ano):
    from datetime import date
    aux = date.today().year
    idade = aux - ano

    if 65 > idade >= 18:
        return 'OBRIGATÓRIO'
    
    elif 16 <=idade < 18 or idade >= 65:
        return 'OPCIONAL'
    
    elif idade < 16:
        return 'NEGADO'
    else:
        return 'INVÁLIDO'

print(voto(1940))
