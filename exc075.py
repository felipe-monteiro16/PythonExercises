v9 = par = v3 = 0
numeros = ()
for c in range(0, 4):
    num = 0
    n = int(input('Digite um número: '))
    num += n
    num = num,
    numeros += num
for pos, num in enumerate(numeros):
    if num == 9:
        v9 += 1
    if num == 3 and v3 == 0:
        print(f'O primeiro valor 3 foi digitado na {pos+1}ª posição.')
        v3 = 1
    if num % 2 == 0:
        par += 1
if v9 == 1:
    print(f'O valor 9 apareceu {v9} vez.')
else:
    print(f'O valor 9 apareceu {v9} vezes.')
if par == 1:
    print(f'Foi digitado somente {par} valor par')
else:
    print(f'Foram digitados {par} números pares.')
