valores = [[], []]
for c in range(1, 8):
    num = int(input(f'{c}° valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('=-' * 30)
print(f'Os valores pares foram: {sorted(valores[0])}')
print(f'E os ímpares foram: {sorted(valores[1])}')
