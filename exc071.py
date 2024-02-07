valor = int(input('Qual o valor que você quer sacar? '))
valor50 = valor20 = valor10 = valor1 = 0
while True:
    if valor >= 50:
        if valor % 50 == 0:
            valor50 = valor/50
            break
        else:
            valor50 = valor//50
            valor = valor % 50
    if valor >= 20:
        if valor % 20 == 0:
            valor20 = valor/20
            break
        else:
            valor20 = valor//20
            valor = valor % 20
    if valor >= 10:
        if valor % 10 == 0:
            valor10 = valor/10
            break
        else:
            valor10 = valor//10
            valor = valor % 10
    if valor < 10:
        valor1 = valor
        break
    break
if valor50 != 0:
    print(f'Total de {valor50} cédulas de R$50')
if valor20 != 0:
    print(f'Total de {valor20} cédulas de R$20')
if valor10 != 0:
    print(f'Total de {valor10} cédulas de R$10')
if valor1 != 0:
    print(f'Total de {valor1} cédulas de R$1')
