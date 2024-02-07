lista = list()
a = media = 0
while True:
    lista.append(dict())
    lista[a]['nome'] = input('Nome: ').capitalize()
    while True:
        sexo = input('Sexo: [M/F]: ')
        if sexo in 'MmFf':
            lista[a]['sexo'] = sexo.upper()
            break
    lista[a]['idade'] = int(input('Idade: '))
    while True:
        c = input('Quer continuar? [S/N]: ')
        if c in 'SsNn':
            break
    a += 1
    if c in 'Nn':
        break
print('-=' * 30)
print(f' - O grupo tem um total de {len(lista)} pessoas.')
print(f' - As mulheres cadastradas foram ', end='')
for b in lista:
    media += b['idade']
    if b['sexo'] == 'F':
        print(b['nome'], end=' ')
media /= len(lista)
print()
print(f' - A média de idade é de {media}')
print(' - Lista de pessoas que estão com idade acima da média:')
for num, b in enumerate(lista):
    if b['idade'] > media:
        for k, v in lista[num].items():
            print(f'    {k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
