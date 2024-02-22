def aumentar(n=0, p=0, f=False):
    n += n * p/100
    if f:
        n = moeda(n)
    return n


def diminuir(n=0, p=0, f=False):
    n -= n * p/100
    if f:
        n = moeda(n)
    return n


def metade(n, f=False):
    n = n/2
    if f:
        n = moeda(n)
    return n


def dobro(n, f=False):
    n *= 2
    if f:
        n = moeda(n)
    return n


def moeda(n):
    n = f'R${n:.2f}'
    return n
