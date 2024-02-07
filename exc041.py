n = int(input('Ano de nascimento: '))
i = 2020 - n
if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JÚNIOR')
elif i == 20:
    print('SÊNIOR')
elif i > 20:
    print('MASTER')
