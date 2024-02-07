a = e = d = 1
b = c = x = 0
print('Sequência de Fibonacci')
n = int(input('Quantos números você quer mostrar? '))
while n > x:
    print(f'{c} → ', end='')
    x += 1
    b = a
    a = c
    c = a + b
    if e == d:
        print('')
        d = 0
        e += 1
    d += 1
print('Fim')
