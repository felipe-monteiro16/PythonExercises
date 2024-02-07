lista = list()
posmaior = list()
posmenor = list()
nmenor = nmaior = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {c}: ')))
for c in range(0, len(lista)):
    if c == 0:
        nmenor = nmaior = lista[c]
    else:
        if lista[c] < nmenor:
            nmenor = lista[c]
        if lista[c] > nmaior:
            nmaior = lista[c]
for pos, num in enumerate(lista):
    if num == nmenor:
        posmenor.append(pos)
for pos, num in enumerate(lista):
    if num == nmaior:
        posmaior.append(pos)
print(25 * '=-')
print(f'Você digitou os valores {lista[:]}.')
print(f'O menor valor digitado foi {nmenor}, e ', end='')
if len(posmenor) > 1:
    print('suas posições foram ', end='')
    for c in range(0, len(posmenor)):
        print(f'[{posmenor[c]}] ', end='')
    print()
elif len(posmenor) == 1:
    print(f'sua posição foi {posmenor}')

print(f'O maior valor digitado foi {nmaior}, e ', end='')
if len(posmaior) > 1:
    print('suas posições foram ', end='')
    for c in range(0, len(posmaior)):
        print(f'[{posmaior[c]}] ', end='')
    print()
elif len(posmaior) == 1:
    print(f'sua posição foi {posmaior}')
