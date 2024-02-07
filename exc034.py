s = int(input('Qual é o salário: '))
if s > 1250:
    a = s/100*10
    print('O aumento foi de {} reais'.format(a))
else:
    a = s/100*15
    print('O aumento foi de {}'.format(a))
