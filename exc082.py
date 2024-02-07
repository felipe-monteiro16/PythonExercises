lista = list()
pares = list()
impares = list()
pos = int()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Deseja continuar? [S/N]: '))
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break
print('=-' * 30)
while pos < len(lista):
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
    else:
        impares.append(lista[pos])
    pos += 1
print(f'A lista completa é: {lista}')
print(f'A lista dos pares é: {pares}')
print(f'A lista dos impares é {impares}')
