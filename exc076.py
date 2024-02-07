lista = ('Lápis', 2, 'Borracha', 1.5, 'Caderno', 9.5, 'Estojo', 25, 'Mochila', 129.99)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<15}', end='')
    else:
        print(f'R${lista[pos]: >7.2f}')
