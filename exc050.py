a = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        a = a + n1
        cont = cont + 1
print(f'Você informou {cont} números pares e a soma deles deu {a}')
