import random
r = (random.randrange(0,5))
n = int(input('Escolhi um número de 0 a 5, adivinhe: '))
if n == r:
    print('Acertou, o número era {}!'.format(r))
else:
    print('Errou, o número era {}'.format(r))
