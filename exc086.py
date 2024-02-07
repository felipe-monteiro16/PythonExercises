valores = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        valores[c].append(int(input(f'Digite um valor para a posição [{c}, {d}]: ')))
print('=-' * 30)
for c in range(0, 3):
    print(f'[{valores[c][0]:^5}][{valores[c][1]:^5}][{valores[c][2]:^5}]')
