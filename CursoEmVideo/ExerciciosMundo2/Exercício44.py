"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 
preço normal e condição de pagamento:

1) À vista dinheiro/cheque: 10% de desconto
2) Em até 2x no cartão: preço normal
3) 3X ou mais no cartão: 20% de juros
4) À vista no cartão: 5% de desconto"""

preço = float(input('Digite o preço do produto: '))

print('-'*50,""" 
        1) À vista: 10% de desconto;
        2) Em até 2x no cartão: preço normal;
        3) Em 3x ou mais: 20% de juros;
        4) Á vista no cartão: 5% de desconto. """,'\n','-'*50)

forma_de_pagamento = int(input('Digite a foma de pagamento: '))

if forma_de_pagamento == 1:

    preço_final = preço - (preço*0.1)
    parcelamento = 0

elif forma_de_pagamento == 2:

    preço_final = preço
    parcelamento = 2

elif forma_de_pagamento == 3:

     preço_final = preço + (preço*0.2)
     parcelamento = int(input('Quantas parcelas deseja: '))


elif forma_de_pagamento == 4:

    preço_final = preço + (preço*0.05)

else:

    print('Opção inválida, digite novamente.')

if parcelamento == 0:

    print('-'*50,'\n'f'O valor devido é: R$ {preço_final}. Sendo pago a vista','\n','-'*50)

else:

    print('-'*50,'\n'f'O valor devido é: R$ {preço_final}. Sendo dividido em {parcelamento}X de R$ {preço_final/parcelamento}','\n','-'*50)

