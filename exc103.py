def jogador(a, b):
    if nome.strip() == '':
        a = "<desconhecido>"
    if b == '' or b.isdigit() is False:
        b = 0
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols:  '))
jogador(nome, gols)
