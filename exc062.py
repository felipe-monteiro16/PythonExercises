a = 1
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p1 = p
while p1 < r*10:
    print(f'{p1} → ', end='')
    p1 += r
print('Pausa')
while a != 0:
    if p1 >= r*10:
        a = int(input('Quantos números Você quer colocar a mais? '))
        p2 = p1 - 1
        p2 = r * a
        p2 -= 1
        while p2 < r * a:
            print(f'{p1} → ', end='')
            p2 += r
        print('Pausa')
