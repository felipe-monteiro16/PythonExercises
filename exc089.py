pqp = list()
c = 0
while True:
    pqp.append([(str(input('Nome: ')))])
    pqp[c].append([float(input('Primeira nota: '))])
    pqp[c][1].append(float(input('Segunda nota: ')))
    resp = input('Deseja continuar? [S/N]: ')
    if resp in 'Nn':
        break
    c += 1
print('=-' * 30)
print('No.  NOME           MÉDIA')
print('-' * 25)
for c in range(0, len(pqp)):
    print(f'{c: <5}', end='')
    print(f'{pqp[c][0]: <15}', end='')
    print(f'{(pqp[c][1][0]+ pqp[c][1][1])/2:>5.1f}')
print('-' * 25)
while True:
    resp = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        print('FINALIZANDO...')
        break
    print('-' * 30)
    print(f'As notas de {pqp[resp][0].capitalize()} são {pqp[resp][1][0], pqp[resp][1][1]}')
