from time import sleep


def lin():
    print('=' * 40)


def maior(*a):
    nmaior = 0
    lin()
    if len(a) != 0:
        nmaior = a[0]
    print('Analisando os valores passados...')
    for num in a:
        print(num, end=' ')
        sleep(0.5)
        if num > nmaior:
            nmaior = num
    print(f'Foram informados {len(a)} valores ao todo.')
    print(f'O maior valor informado foi {nmaior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0, 1)
maior(1, 2)
maior(6)
maior()
lin()
