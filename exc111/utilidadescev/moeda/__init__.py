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


def resumo(n, a, d):
    print('=' * 30)
    print(f'{"RESUMO DO VALOR": ^30}')
    print('=' * 30)
    print(f'{"Preço analisado:": <20}{moeda(n): <10}')
    print(f'{"Dobro do preço": <20}{dobro(n, True): <10}')
    print(f'{"Metade do preço": <20}{metade(n, True): <10}')
    print(f'{(str(a) + "% de aumento:"): <20}{aumentar(n, a, True): <10}')
    print(f'{(str(d) + "% de redução:"): <20}{diminuir(n, d, True): <10}')
    print('=' * 30)
