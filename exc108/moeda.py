def aumentar(n=0, p=0):
    n += n * p/100
    return n


def diminuir(n=0, p=0):
    n -= n * p/100
    return n


def metade(n=0):
    n = n/2
    return n


def dobro(n=0):
    n *= 2
    return n


def moeda(n=0):
    a = f'R${n:.2f}'.replace('.', ',')
    return a
