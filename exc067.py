cont = 1
while True:
    t = int(input('Quer ver a tabuada de qual valor? (0 pra sair) '))
    print('-' * 35)
    if t == 0:
        break
    while True:
        print(f'{t} x {cont} = {t*cont}')
        if cont == 10:
            break
        cont += 1
    print('-' * 35)
    cont = 1
print('Fim')
