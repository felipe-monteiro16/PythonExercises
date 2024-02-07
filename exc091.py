from random import randint
from time import sleep
valores = dict()
print('Valores Sorteados:')
sleep(0.5)
for c in range(1, 5):
    num = randint(1, 6)
    print(f'    O jogador{c} tirou {num}')
    valores['jogador' + str(c)] = num
    sleep(0.5)
c = 0
ordem = list(valores.items())
for num, i in enumerate(ordem):
    if num > 0:
        for num2, i2 in enumerate(ordem):
            if i2[1] < i[1]:
                ordem[num], ordem[num2] = ordem[num2], ordem[num]
valores = dict(ordem)
print('Ranking dos Jogadores:')
for k, v in valores.items():
    sleep(0.5)
    c += 1
    print(f'    {c}° lugar: {k} com {v}')
