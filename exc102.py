def fatorial(n=1, show=False):
    """
    -> Calculador de Fatorial
    :param n: Número a se calcular o fatorial.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: Fatorial de "n"
    """
    num = n
    for c in range(n, 0, -1):
        if c < n:
            num *= c
        if show is True:
            print(c, end=' ')
            if c != 1:
                print('x ', end='')
            else:
                print('=', end=' ')
    return num


print("=" * 30)
print(fatorial(5, True))
help(fatorial)
