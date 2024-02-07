palavras = ('Felipe', 'Monteiro', 'Mateus', 'e', 'Souza')
for num, p in enumerate(palavras):
    print(f'Na palavra "{p}" temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
    print('')
