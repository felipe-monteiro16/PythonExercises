total = p = a = menor = 0
n = 'a'
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    print('-' * 30)
    total += preco
    a += 1
    if preco > 1000:
        p += 1
    if a == 1:
        menor = preco
    if preco < menor:
        menor = preco
        n = nome
    while True:
        d = str(input('Deseja continuar? [S/N] '))
        print('-' * 30)
        if d in 'SsNn':
            break
    if d in 'Nn':
        break
print(f'O total gasto foi {total:.2f}')
print(f'Temos {p} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {n} que custou R${menor:.2f}')
