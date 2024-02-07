lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não será adicionado.')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    while True:
        a = str(input('Deseja continuar? [S/N]: '))
        if a in 'NnSs':
            break
    if a in 'Nn':
        break
lista.sort()
print('=-' * 30)
print(f'Você digitou os valores {lista[:]}')
