f = str(input('Digite algo: '))
f1 = f.replace(' ', '')
f2 = f1.upper()
f3 = f2[::-1]
print(f'O inverso de {f2} é {f3}')
if f3 == f2:
    print('A frase digitada é um Palíndromo')
else:
    print('A frase digitada não é um palíndromo')
