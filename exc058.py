from random import randrange
a = 0
r = (randrange(1, 10))
n = int(input('Escolhi um número de 1 a 10, Adivinhe! '))
while r != n:
    n = int(input('Errou! Tente Novamente: '))
    a = a + 1
print(f'Acertou! o número era {r} e você errou {a} Vezes!')
