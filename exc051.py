p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print(f'{p} → ', end='')
for c in range(0, 9):
    p = p + r
    print(p, '→',  end=' ')
print('Acabou.')
