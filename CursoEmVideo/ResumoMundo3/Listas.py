lista = ['A','D','C','F']
lista.append('E')
lista.remove('A')
lista.sort()
print(lista)
lista.sort(reverse = True)
print(lista)
del lista[1]
print(lista)
lista.pop(0)
print(lista)
lista.remove('C')
print(lista)
valores = list(range(0,8))
print(valores)
lista.insert(1, 'H')
print(lista)

a = [1, 2, 3, 4]
b = a[:]
b[2] = 6
c = a # cria uma correlação entre 'c' e 'a'
print(a, b)