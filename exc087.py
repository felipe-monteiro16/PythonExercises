valores = [[], [], []]
soma = vmaior = scol = 0
for c in range(0, 3):
    for d in range(0, 3):
        valores[c].append(int(input(f'Digite um valor para a posição [{c}, {d}]: ')))
print('=-' * 30)
print(valores)
for c in range(0, 3):
    print(f'[{valores[c][0]:^5}][{valores[c][1]:^5}][{valores[c][2]:^5}]')
    if c == 0:
        vmaior = valores[1][c]
    elif valores[1][c] > vmaior:
        vmaior = valores[1][c]
    for d in range(0, 3):
        if valores[c][d] % 2 == 0:
            soma += valores[c][d]
    scol += valores[c][2]
print('=-' * 30)
print(f'A soma de todos os valores pares é igual a {soma}.')
print(f'A soma dos valores da terceira coluna é igual a {scol}.')
print(f'O maior valor da segunda linha é igual a {vmaior}.')
