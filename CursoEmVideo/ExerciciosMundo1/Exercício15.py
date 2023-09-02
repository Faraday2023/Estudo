# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

km_rodado = float(input('Digite a quilometragem percorrida pelo carro: '))
valor_km = 0.15
diária = 60
dias_alugados = int(input('Digite quantos dias o carro foi alugado: ')) 
preço_cobrado = km_rodado*valor_km + dias_alugados*diária
print(f'Valor a ser pago pelo seu aluguel: R$ {preço_cobrado:.2f} ')