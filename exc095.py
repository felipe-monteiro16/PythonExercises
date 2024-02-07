dados = list()
a = 0
lista = list()
while True:
    dados.append({})
    dados[a]['nome'] = input('Nome do Jogador: ')
    p = int(input(f'Quantas partidas {dados[a]["nome"]} jogou? '))
    dados[a]['gols'] = list()
    dados[a]['total'] = int()
    for c in range(0, p):
        dados[a]['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
        dados[a]['total'] += dados[a]['gols'][c]
    while True:
        c = input('Quer continuar? [S/N] ').upper()
        if c in 'SN':
            break
    if c == 'N':
        break
    a += 1
    print('-' * 30)
print('-=' * 30)
print(f"{'Código': <10}", end='')
print(f'{"Nome": <15}', end='')
print(f'{"Gols": <20}', end='')
print(f'{"Total": >10}')
print('-' * 56)
for num, c in enumerate(dados):
    print(f'{num: ^10}', end='')
    print(f'{c["nome"]: <15}', end='')
    print(f'{str(c["gols"]): <26}', end='')
    print(f'{c["total"]: <5}', end='')
    print()
while True:
    while True:
        print('-' * 56)
        p = int(input('Deseja mostrar os dados de qual jogador? (999 para encerrar): '))
        if 0 <= p < len(dados) or p == 999:
            break
        if p >= len(dados) or p < 0:
            print(f"ERRO! Não existe o Jogador {p}, tente novamente.")
    if p == 999:
        break
    print(f' - Levantamento do jogador {dados[p]["nome"]}')
    for c, g in enumerate(dados[p]["gols"]):
        print(f'    No jogo {c} {dados[p]["nome"]} fez {dados[p]["gols"][c]} gols.')
print('<< Volte Sempre! >>')
    