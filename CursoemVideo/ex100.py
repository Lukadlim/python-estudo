from random import randint
from time import sleep
numeros = []


def sorteia(numeros):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')


lista = []
sorteia(lista)
somapar(lista)
