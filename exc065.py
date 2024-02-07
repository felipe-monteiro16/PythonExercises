r = 1
a = soma = maior = menor = 0
while r == 1:
    n = int(input('Escreva um número: '))
    a += 1
    soma += n
    if a == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print('[1] = Sim')
    print('[0] = Não')
    r = int(input('Quer continuar? '))
print(f'A média dos {a} números foi {soma/a}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')
