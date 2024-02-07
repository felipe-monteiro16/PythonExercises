dados = dict()
dados['nome'] = input('Nome do Jogador: ')
p = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = list()
dados['total'] = int()
for c in range(0, p):
    dados['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    dados['total'] += dados['gols'][c]
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {p} partidas.')
for c in range(0, p):
    print(f'    => Na partida {c}, fez {dados["gols"][c]} gols.')
print(f'Foi um total de {dados["total"]} gols.')
