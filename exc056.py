m20 = 0
maior = 0
menor = 0
a1 = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(float(input('Idade: ')))
    sexo = str(input('Sexo: [M/F]: '))
    a1 = a1 + idade
    sexo = sexo.upper()
    if c == 1:
        maior = idade
        menor = idade
        nmaior = nome
        nmenor = nome
    else:
        if idade > maior:
            maior = idade
            nmaior = nome
        if idade < menor:
            menor = idade
            nmenor = nome
    if sexo == 'F' and idade < 20:
        m20 = m20 + 1

print(f'A média de idade do grupo é {a1 / 4}')
print(f'O nome da pessoa mais velha é {nmaior}')
print(f'O nome da pessoa mais nova é {nmenor}')
print(f'{m20} mulheres tem menos de 20 anos')
