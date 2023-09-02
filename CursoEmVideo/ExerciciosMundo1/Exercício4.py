# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possíveis sobre ele

algo = input('Digite algo na tela: ')

a = algo.isnumeric()
b = algo.isalpha()
c = algo.isalnum()
d = algo.isdecimal()
e = algo.islower()
f = algo.isupper()
g = algo.isspace()
h = algo.istitle()
i = type(algo)

print("""O que você digitou é:
      
      1) Um número: {}
      2) Uma palavra: {}
      3) Uma palava alfanumérica: {}
      4) Um número decimal: {}
      5) Uma palavra com letras minúsculas: {}
      6) Uma palavra com letras maiúscula: {}
      7) Só tem espaços: {}
      8) É um título: {}
      9) Tipo primitivo: {}""".format(a,b,c,d,e,f,g,h,i))