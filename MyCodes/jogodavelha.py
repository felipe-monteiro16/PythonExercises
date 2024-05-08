# -*- coding: utf-8 -*-


# Jogo da velha feito por mim. Tentei fazer com que o programa não desse erro em nenhuma ocasião.
# Nesse, o jogador escolhe se quer ser o "X" ou a "O" e a posição que quer jogar, e o computador escolhe uma aleatória.


from random import choice
from time import sleep
import sys

li = []
nums = []
fim = cont = 0
vencedor = j1 = j2 = ''


def lin(p='', n=50):
    """
    -> Função para mostrar mensagem formatada
    :param p: Mensagem
    :param n: Número de caracteres
    """
    print('=' * n)
    print(f'{p:^{n}}')
    print('=' * n)


def mostra_jogo():
    """
    -> Função para mostrar o Jogo
    """
    jogo = (f'\n{li[6]} | {li[7]} | {li[8]}\n'
            f'---|---|---\n'
            f'{li[3]} | {li[4]} | {li[5]}\n'
            f'---|---|---\n'
            f'{li[0]} | {li[1]} | {li[2]}')
    for linha in jogo.splitlines():
        print(f'{linha:^50}')
    print()


def verifica_win():
    global fim
    global vencedor
    """
    -> Função para verificar se o jogo acabou e ver quem foi o vencedor.
    :return: None
    """
    def ve2(n1, n2, n3):
        """
        -> Função para verificar se os valores da lista que estão na posição dos parâmetros pedidos são iguais,
        complementando a função 'verifica_win'.
        :param n1: Posição 1
        :param n2: Posição 2
        :param n3: Posição 3
        :return: Não há retorno para não precisar de vários 'if' na outra função, mas a variável 'fim' deixa de
        ser 0 e passa a ser 1 caso o jogo acabe.
        """
        global vencedor
        global fim
        if li[n1 - 1] == li[n2 - 1] == li[n3 - 1] != ' ':
            vencedor = li[n1 - 1]
            fim = 1

    ve2(1, 2, 3)
    ve2(4, 5, 6)
    ve2(7, 8, 9)
    ve2(1, 4, 7)
    ve2(2, 5, 8)
    ve2(3, 6, 9)
    ve2(1, 5, 9)
    ve2(3, 5, 7)

    if fim == 1:
        lin('FIM DE JOGO')
        if vencedor == j1:
            print('JOGADOR VENCEU')
        elif vencedor == j2:
            print('COMPUTADOR VENCEU')
    elif cont == 9:
        print('EMPATE! deu velha.')
        fim = 1


for c in range(1, 10):
    li.append(c)
    nums.append(c)

lin('JOGO DA VELHA')

mostra_jogo()

li.clear()
for c in range(1, 10):
    li.append(' ')

# Coletando opção do jogador com tratamento de erro impossibilitando opção inválida.

while True:
    try:
        j1 = input('Você quer ser o [ X ] ou o [ O ]? ').upper()
    except KeyboardInterrupt:
        print('\033[91mPrograma Interrompido.\033[m')
        sys.exit(1)
    if j1 in 'XO' and len(j1) == 1:
        j2 = 'X' if j1 == 'O' else 'O' if j1 == 'X' else ' '
        break
    else:
        print(f'\n\033[91mERRO! Tente novamente.\033[0m\n')


while True:
    while True:
        # Tratamento de erro

        try:
            pos = input('Digite a posição: ')
        except KeyboardInterrupt:
            print('\033[91mPrograma Interrompido.\033[m')
            sys.exit(1)

        # Verificando se o valor digitado é válido

        if pos.isnumeric():
            pos = int(pos)
            if pos in nums:
                li[pos - 1] = j1
                nums.remove(pos)
                break
            if pos not in nums:
                print(f'\033[91mERRO! Tente novamente.\033[0m')
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
