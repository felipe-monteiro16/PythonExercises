a = int(input('Quantos quilômetros rodados: '))

b = int(input('Quantos dias alugados: '))

c = a * 0.15

d = b * 60

print('O total a pagar é de R${:.2f}'.format(c + d))
