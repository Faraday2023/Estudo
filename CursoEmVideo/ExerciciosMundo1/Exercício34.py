"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

1) Para salários superiores a R$ 1.250,00 calcule aumento de 10%
2) Para os inferiores ou iguais, o aumento é de 15%"""

salário = float(input('Digite o salário do funcionário: '))

if salário >= 1250:

    salário_novo = salário + (salário*0.1)
    print(salário_novo)

else:

    salário_novo = salário + (salário*0.15)
    print(salário_novo)