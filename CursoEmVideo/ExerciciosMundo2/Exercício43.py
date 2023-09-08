"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e 
mostre seu status, de acordo com a tabela abaixo:

1) Abaixo de 18.5 - Abaixo do Peso
2) Entre 18.5 e 25 - Peso Ideal
3) 25 até 30: Sobrepeso
4) 30 até 40: Obesidade"""

peso = float(input('Digite o peso da pessoa em "kg": '))
altura = float(input('Digite a altura da pessoa em "m": '))
imc = peso/pow(altura,2)

if imc < 18.5:
    print(f'Abaixo do peso: IMC {imc:.2f}.')

elif imc < 25:
    print(f'Peso ideal: IMC {imc:.2f}.')

elif imc < 30:
    print(f'Sobrepeso: IMC {imc:.2f}.')

else:
    print(f'Obesidade: IMC {imc:.2f}.')