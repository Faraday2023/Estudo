# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = 5
altura = 2.7
rend_tinta = 2
area = largura*altura
QuantTinta_Nec = round(area/rend_tinta,1)
print(f'Você precisará de {QuantTinta_Nec} litros de tinta')