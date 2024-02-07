a = 1
n = int(input('Digite um número: '))
for c in range(1, 11):
    a = a + 1
    if n % a == 0 and n != a:
        print('O número {} não é primo'.format(n))
        exit()
else:
    print('O número {} é primo'.format(n))
