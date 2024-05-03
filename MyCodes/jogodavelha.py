# -*- coding: utf-8 -*-
from random import choice
from time import sleep


li = []
nums = []
fim = cont = 0
vencedor = ''


def lin(p='', n=50):
    print('=' * n)
    print(f'{p:^{n}}')
    print('=' * n)


def mostra_jogo():
    jogo = (f'\n{li[6]} | {li[7]} | {li[8]}\n'
            f'---|---|---\n'
            f'{li[3]} | {li[4]} | {li[5]}\n'
            f'---|---|---\n'
            f'{li[0]} | {li[1]} | {li[2]}')
    for linha in jogo.splitlines():
        print(f'{linha:^50}')
    print()


def ve2(n1, n2, n3):
    global vencedor
    global fim
    if li[n1-1] == li[n2-1] == li[n3-1] != ' ':
        vencedor = li[n1-1]
        fim = 1


def verifica_win():
    global vencedor
    ve2(1, 2, 3)
    ve2(4, 5, 6)
    ve2(7, 8, 9)
    ve2(1, 4, 7)
    ve2(2, 5, 8)
    ve2(3, 6, 9)
    ve2(1, 5, 9)
    ve2(3, 5, 7)
    if fim == 1:
        print('FIM DE JOGO')
        if vencedor == j1:
            print('JOGADOR VENCEU')
        elif vencedor == j2:
            print('COMPUTADOR VENCEU')


for c in range(1, 10):
    li.append(c)
    nums.append(c)

lin('JOGO DA VELHA')

mostra_jogo()

li.clear()
for c in range(1, 10):
    li.append(' ')


while True:
    j1 = input('Você quer ser o [ X ] ou o [ O ]? ').upper()
    if j1 in 'XO' and len(j1) == 1:
        j2 = 'X' if j1 == 'O' else 'O' if j1 == 'X' else ' '
        break
    else:
        print(f'\033[91mERRO! Tente novamente.\033[0m')


while True:
    while True:
        pos = int(input('Digite a posição: '))
        if pos in nums:
            li[pos - 1] = j1
            nums.remove(pos)
            break
        else:
            print(f'\033[91mERRO! Tente novamente.\033[0m')
    mostra_jogo()
    cont += 1
    verifica_win()
    if fim == 1:
        break
    sleep(1)
    num_pc = choice(nums)
    print(f'Minha Vez! Escolhi a posição {num_pc}.')
    sleep(0.5)
    li[num_pc - 1] = j2
    nums.remove(num_pc)

    mostra_jogo()
    cont += 1
    verifica_win()
    if fim == 1:
        break
    elif cont == 9:
        print('EMPATE! deu velha')
