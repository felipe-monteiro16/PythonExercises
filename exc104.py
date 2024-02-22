def leiaint(v):
    while True:
        num1 = input(v)
        if num1.isdigit() is True:
            break
        print('\033[91mERRO! Digite um número inteiro válido.\033[0;0m' )
    return num1


num = leiaint('Digite um Número: ')
print(f'Você acabou de digitar o número {num}.')
