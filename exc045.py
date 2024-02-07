from random import randint
from time import sleep
c = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
e = int(input('Qual é a sua escolha? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('=' * 25)
if c == 0:
    print('Computador jogou Pedra')
elif c == 1:
    print('Computador jogou Papel')
elif c == 2:
    print('Computador jogou tesoura')
if e == 0:
    print('Jogador jogou Pedra')
elif e == 1:
    print('Jogador jogou Papel')
elif e == 2:
    print('Jogador jogou Tesoura')
print('=' * 25)
if c == 0 and e == 0 or c == 1 and e == 1 or c == 2 and e == 2:
    print('EMPATE')
if c == 0 and e == 2 or c == 1 and e == 0 or c == 2 and e == 1:
    print('Computador Vence')
if e == 0 and c == 2 or e == 1 and c == 0 or e == 2 and c == 1:
    print('Jogador Vence')
if e != 0 and e != 1 and e != 2:
    print('Você deve jogar somente 0, 1 ou 2.')
