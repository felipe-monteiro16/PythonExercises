from time import sleep
from random import randint
numeros = list()


def sorteio():
    numeros.clear()
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        sleep(0.3)
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
    print('PRONTO!')


def somapar():
    sleep(0.3)
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteio()
somapar()
