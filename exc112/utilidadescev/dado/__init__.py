def leiadinheiro(n):
    while True:
        cont = 0
        num = input(n)
        num = num.replace(',', '.').strip()
        for c in num:
            if c == '.':
                cont += 1
        if cont < 2:
            if num.replace('.', '').isnumeric():
                num = float(num)
                break
            else:
                print(f'\033[91mERRO! "{num}" não é um preço inválido.\033[m')
        else:
            print(f'\033[91mERRO! "{num}" não é um preço inválido.\033[m')
    return num
