from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
nmenor = tupla[0]
nmaior = tupla[0]
for num in tupla:
    if num < nmenor:
        nmenor = num
    if num > nmaior:
        nmaior = num
print(f'Os valores sorteados foram: {tupla[0]}, {tupla[1]}, {tupla[2]}, {tupla[3]}, {tupla[4]}')
print(f'O maior é: {nmaior}')
print(f'E o menor é: {nmenor}')
