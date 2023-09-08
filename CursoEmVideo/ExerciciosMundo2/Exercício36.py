"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma 
casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
 vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o 
 empréstimo será negado"""

# Variáveis de entrada

valor_da_casa = float(input('Digite o valor da casa: '))
salário = float(input('Digite o salário do colaborador: '))
tempo = int(input('Digite em quantos anos pretende fazer o financiamento: '))

# Variáveis auxiliares
#  
tempo_em_meses = tempo*12
prestação = valor_da_casa/(tempo_em_meses)

if prestação > salário*0.3:

    print('Desculpe, seu empréstimo foi negado por exceder 30% do seu salário.')

else:
    print(f'Parabéns, seu empréstimo foi aprovado - Prestação: R$ {prestação:.1f}')
