p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p1 = p
while p1 < r*10:
    print(f'{p1} → ', end='')
    p1 += r
print('Fim.')
