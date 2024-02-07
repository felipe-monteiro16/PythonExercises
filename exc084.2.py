pesomenor = pesomaior = c = 0
dados = list()
while True:
    dados.append([])
    dados[c].append(str(input('Nome: ')))
    dados[c].append(float(input('Peso: ')))
    resp = input('Deseja continuar? [S/N]: ')
    if resp in 'Nn':
        break
    c += 1
a = len(dados)
print('=-' * 30)
print(f'Ao todo, foram cadastradas {a} pessoas.')
for pos in range(0, a):
    if pos == 0:
        pesomenor = pesomaior = dados[0][1]
    if pos > 0:
        if dados[pos][1] > pesomaior:
            pesomaior = dados[pos][1]
        if dados[pos][1] < pesomenor:
            pesomenor = dados[pos][1]
print(f'E o maior peso foi {pesomaior} Kg, peso de ', end='')
for p in dados:
    if p[1] == pesomaior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi {pesomenor} Kg, peso de ', end='')
for p in dados:
    if p[1] == pesomenor:
        print(f'[{p[0]}]', end=' ')
