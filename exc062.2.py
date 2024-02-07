a = b = 1
print('=' * 15)
print('GERADOR DE PA')
print('=' * 15)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
while a < 11:
    print(f'{p} →', end=' ')
    p += r
    a += 1
print('PAUSA')
while b != 0:
    b = int(input('Quantos termos você deseja mostrar mais? '))
    d = 0
    for c in range(0, b):
        p += r
        print(f'{p} →', end=' ')
        a += 1
        d += 1
        if d == 15:
            print('')
            d = 0
    if b != 0:
        print('PAUSA')
print(f'Progressão finalizada com {a-1} termos mostrados.')
