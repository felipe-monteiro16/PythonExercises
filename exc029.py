v = int(input('Qual é a velocidade: '))
if v >= 80:
    print('Você foi multado')
    m = v - 80
    m1 = m*7
    print('A multa custará {} reais.'.format(m1))
