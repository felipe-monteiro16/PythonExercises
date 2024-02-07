v = int(input('Valor da casa: '))
s = int(input('Salário: '))
a = int(input('Quantos anos: '))
a1 = a*12
v1 = v/a1
s1 = (s/100) * 30
if v1 <= s1:
    print('O valor da prestação é R${}'.format(v1))
else:
    print('O valor da prestação é R${}'.format(v1))
    print('Você não pode financiar essa casa.')
