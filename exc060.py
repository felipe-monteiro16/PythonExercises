n = int(input('Digite um número para calcular seu fatorial: '))
n1 = n
r = 1
print(f'{n}! = {n} * ', end='')
while n1 > 0:
    if r != 1:
        print(f'{n1}', end='')
        print(' * ' if n1 > 1 else ' = ', end='')
    r *= n1
    n1 -= 1
print(r)
