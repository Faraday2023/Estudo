# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere US$ 1,00 = R$ 3.27

reais = float(input('Digite quantos reais você tem na carteira: '))

print(f'Você tem R$ {reais:.2f}., convertidos em $ :{(reais/3.27):.2f} ')