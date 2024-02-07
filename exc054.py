a = 0
m = 0
for c in range(0, 7):
    n = int(input('Ano de nascimento: '))
    if n < 2003:
        a = a + 1
    elif n > 1999:
        m = m + 1
print('Dessas pessoas {} já são maiores de idade, {} não'.format(a, m))
