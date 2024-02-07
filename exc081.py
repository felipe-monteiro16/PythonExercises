lista = list()
pos = int()
positions = list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        con = input('Deseja continuar? [S/N]: ')
        if con in 'SsNn':
            break
    if con in 'Nn':
        break
print('=-' * 30)
if len(lista) == 1:
    print('Nessa lista, foi digitado 1 número.')
else:
    print(f'Nessa lista, foram digitados {len(lista)} números.')
while pos < len(lista):
    if lista[pos] == 5:
        positions.append(pos)
    pos += 1
if len(positions) == 0:
    print('O número 5 não foi digitado.')
if len(positions) == 1:
    print(f'O número 5 foi digitado na posição {positions[0]}.')
if len(positions) > 1:
    print(f'O número 5 foi digitado nas posições {positions[:]}.')
print(f'Os seus valores em ordem decrescente são: {lista.sort(reverse=True)}.')
