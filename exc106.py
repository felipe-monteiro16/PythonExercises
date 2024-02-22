from time import sleep


def reverso():
    print('\033[0;0m', end='')


def linhas(s, cor):
    linha = len(s) + 4
    print(f'\033[30;1;{cor}m~' * linha)
    print(f'{s: ^{linha}}')
    print('~' * linha)
    reverso()


def encontrahelp():
    linhas('SISTEMA DE AJUDA PyHELP', 103)
    reverso()
    sleep(0.5)
    f = input('Função ou Biblioteca > ')
    if f.lower() != 'fim':
        sleep(0.5)
        linhas(f"Acessando o manual do comando '{f}' ", 104)
        sleep(0.5)
        print(f'\033[107;30;1m', end='')
        help(f)
        reverso()
        sleep(0.5)
        return 0
    else:
        linhas('ATÉ LOGO!', 101)
        return 1


while True:
    a = encontrahelp()
    if a == 1:
        break
