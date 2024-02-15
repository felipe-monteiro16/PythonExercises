from time import sleep


def lin():
    print('=' * 40)


def contador(inicio, fim, passo):
    lin()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    print(inicio, end=' ')
    sleep(0.3)
    if passo == 0:
        passo = 1
    if fim < inicio and passo > 0 or fim > inicio and passo < 0:
        passo *= -1
    if fim > inicio:
        while True:
            if inicio + passo > fim:
                print('Fim!')
                break
            print(inicio + passo, end=' ')
            sleep(0.3)
            inicio = inicio + passo
    if fim < inicio:
        while True:
            if inicio + passo < fim:
                print('Fim!')
                break
            print(inicio + passo, end=' ')
            sleep(0.3)
            inicio = inicio + passo


contador(1, 10, 1)
contador(10, 0, 2)
lin()
print("Agora é sua vez de personalizar o contador!")
contador(int(input('Início: ')),
         int(input('Fim:    ')),
         int(input('Passo:  ')))
