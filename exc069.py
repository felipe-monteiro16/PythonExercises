i = s = h = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    print('-' * 30)
    while True:
        c = str(input('Deseja continuar? [S/N] '))
        print('-' * 30)
        if c in 'SsNn':
            break
    if idade > 18:
        i += 1
    if sexo in 'Mm':
        h += 1
    if sexo in 'Ff' and idade < 20:
        s += 1
    if c in "Nn":
        break
print(f'''Das pessoas cadastradas:
{i} tem mais que 18 anos, {h} São homens e
{s} São mulheres com menos de 20 anos.''')
