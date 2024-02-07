a = int(input('Ano de nascimento: '))
b = 2020 - a
if b < 18:
    print('Você poderá se alistar daqui {} anos'.format(18 - b))
elif b == 18:
    print('Você já está na hora de se alistar!')
elif b > 18:
    print('Você poderia se alistar há {} anos'.format(b - 18))
