e = 4
while e == 4:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print('''Escolha a operação
    Digite: 
    [1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Novos números 
    [5] Sair do programa''')
    e = int(input('Sua escolha: '))
if e == 1:
    print(f'{n1} + {n2} = {n1+n2}')
elif e == 2:
    print(f'{n1} * {n2} = {n1*n2}')
elif e == 3:
    if n1 > n2:
        print(f'{n1} é maior que {n2}')
    elif n1 < n2:
        print(f'{n2} é maior que {n1}')
    elif n1 == n2:
        print(f'{n1} e {n2} são iguais.')
elif e == 5:
    print('Fim')
