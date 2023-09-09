"""Crie um programa onde o usuário digite uam expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
parênteses abertos e fechados na ordem correta."""

expressão = str(input('Digite uma expressão matemática: '))
lista = []

for símbolos in expressão:

    if símbolos == '(':
        lista.append(símbolos)
    elif símbolos == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(símbolos)

if len(lista) == 0:

    print('Sua expressão está correta.')
else:

    print('Sua expressão está inválida.')
