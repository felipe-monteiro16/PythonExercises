n = 0
tabela = ('América-MG', 'Athlético-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Ceará SC', 'Chapecoense', 'Corinthians',
          'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras',
          'Bragantino', 'Santos', 'Sport Recife', 'São Paulo')
print('=-' * 50)
print(f'Os 5 primeiros colocados:{tabela[0: 5]}')
print('=-' * 50)
print(f'Os 4 últimos colocados:{tabela[-4:]}')
print('=-' * 50)
print(f'Em ordem alfabética:{sorted(tabela)}')
print('=-' * 50)
for pos, time in enumerate(tabela):
    if time in 'Chapecoense':
        print(f'O Chapecoense está na {pos + 1}ª posição.')
