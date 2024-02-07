n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if 5 > m:
    print('REPROVADO')
elif 5 <= m < 7:
    print('RECUPERAÇÃO')
elif 7 <= m:
    print('APROVADO')
