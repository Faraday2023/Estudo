"""Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável"""

def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)

texto = str(input('Digite: '))
escreva(texto)
