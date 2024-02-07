import random
v = 0
while True:
    n1 = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar? [P/I] '))
    print('-' * 30)
    n2 = random.randint(1, 10)
    r = n1+n2
    if r % 2 == 0:
        print(f'Você jogou {n1} e o computador {n2}. Totalizando {r} Deu Par.')
        print('-' * 30)
        if e in 'Pp':
            v += 1
            print('Você ganhou')
            print('Vamos denovo...')
            print('-' * 30)
        if e in 'Ii':
            print('Você perdeu')
            break
    else:
        print(f'Você jogou {n1} e o computador {n2}. Totalizando {r}, Ímpar.')
        print('-' * 30)
        if e in 'Ii':
            v += 1
            print('Você ganhou')
            print('Vamos denovo...')
            print('-' * 30)
        if e in 'Pp':
            print('Você perdeu')
            break
print('=-' * 15)
if v == 0:
    print('GAME OVER! Você venceu nenhuma vez.')
elif v == 1:
    print(f'GAME OVER! Você venceu {v} vez.')
elif v > 1:
    print(f'GAME OVER! Você venceu {v} vezes.')
