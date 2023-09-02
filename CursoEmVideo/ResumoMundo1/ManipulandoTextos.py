# Manipulando Textos

Frase = "Curso em Vídeo"
print(Frase[3])
print(Frase[0:5])
print(Frase[:5])
print(Frase[:])
print(Frase[0:14:2])
print(Frase[3::2])
print(Frase[::2])

print("""
      aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")

x = """  bbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbb
bbbbbbb  """

print(x)

y = x.count('b')
print(y)

z = len(x)
print(z)

w = x.strip()
print(len(w))

t = Frase.replace('Vídeo', 'Android')
print(t)

print('Curso' in Frase)
m = Frase.find('em')
print(m)

n = Frase.split()
print(n)
print(n[0][1])
print(n[0][0:])
print(n[1][0:3])