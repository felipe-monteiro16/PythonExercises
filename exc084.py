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
print(dados)
a = len(dados)
print('=-' * 30)
print(f'Ao todo, foram cadastradas {a} pessoas.')
for pos in range(0, a):
    if pos == 0:
        pesomenor = pesomaior = dados[0][1]
        dados.append([dados[0][0]])
        dados.append([dados[0][0]])
    if pos > 0:
        if dados[pos][1] == pesomaior:
            dados[a].append(dados[pos][0])
        if dados[pos][1] == pesomenor:
            dados[a+1].append(dados[pos][0])
        if dados[pos][1] > pesomaior:
            pesomaior = dados[pos][1]
            dados[a].insert(1, dados[pos][0])
            del dados[a][0]
        if dados[pos][1] < pesomenor:
            pesomenor = dados[pos][1]
            dados[a+1].insert(1, dados[pos][0])
            del dados[a+1][0]
print(f'O menor peso foi de {pesomenor}Kg, peso de {dados[a+1]}')
print(f'e o maior peso foi de {pesomaior}Kg peso de {dados[a]}')
