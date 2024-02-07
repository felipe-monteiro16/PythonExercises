n = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
b = int(input(''))
if b == 1:
    print('Binário: {}'.format(bin(n)[2:]))
elif b == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif b == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção Inválida. Tente Novamente.')
