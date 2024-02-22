num1 = real1 = 0


def leiaint():
    while True:
        global num1
        try:
            num1 = int(input('Digite um Número Inteiro: '))
        except KeyboardInterrupt:
            print('\n\033[91mO usuário preferiu não informar o valor.\033[0;0m')
            break
        except Exception:
            print('\033[91mERRO! Digite um número inteiro válido.\033[0;0m')
        else:
            break
    return num1


def leiafloat():
    global real1
    while True:
        try:
            real1 = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print('\n\033[91mO usuário preferiu não informar o valor.\033[m')
            break
        except (ValueError, TypeError):
            print('\033[91mERRO! Digite um número real válido.\033[0;0m')
            continue
        else:
            break
    return real1


num = leiaint()
real = leiafloat()
print(f'Você acabou de digitar o número inteiro {num} e o real {real}.')
