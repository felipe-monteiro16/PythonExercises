from random import randrange
from time import sleep
jogos = list()
print('-' * 30)
print(f"{'SORTEADOR DA MEGA SENA' : ^30}")
print('-' * 30)
num = int(input('Quantos jogos serão sorteados? '))
for c in range(0, num):
    jogos.append([])
    while len(jogos[c]) < 6:
        a = randrange(1, 61)
        if a not in jogos[c]:
            jogos[c].append(a)
print(f'-=-=-= SORTEANDO {num} JOGOS =-=-=-')
for c in range(0, num):
    jogos[c].sort()
    print(f'Jogo {c+1:^2}: {jogos[c]}')
    sleep(1)
print('-=-=-= < BOA SORTE! > =-=-=-')
