# Escreva um programa que converta uma temperatura digitada em °C para °F

# 1°C = 33,8°F

Temp_Celsius = float(input('Digite a temperatura em °C: '))
Temp_Far = Temp_Celsius*1.8 + 32
print(f'A temperatura em Celsius é: {Temp_Celsius}° e Fahrenheit: {Temp_Far}°')