cont = num1 = 0
while True:
    num = int(input('Digite um número: [999 pra parar] '))
    if num == 999:
        break
    num1 += num
    cont += 1
print(f'A soma dos {cont} valores deu {num1}')
