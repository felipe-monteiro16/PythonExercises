v = int(input('Qual é a distância da viagem? '))
if v <= 200:
    s = v * 0.5
    print('Sua viagem custará {} Reais.'.format(s))
else:
    print('Sua viagem custará {} Reais.'.format(v * 0.45))
