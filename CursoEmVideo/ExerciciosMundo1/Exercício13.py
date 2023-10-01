# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento

salário_antigo = float(input('Digite o salário antigo do funcionário: '))
aumento = 0.15
salário_novo = salário_antigo+(salário_antigo*aumento)

print(f'O salário passou de R$ {salário_antigo:.2f} para R$ {salário_novo:.2f}')
