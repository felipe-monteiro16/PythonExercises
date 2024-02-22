from time import sleep
pessoas = {'pessoa1': ('ana paula vieira', 32), 'pessoa2': ('Cláudio Medonça', 18),
           'pessoa3': ('Gustavo Guanabara', 41), 'pessoa 4': ('Maria Clara Peixoto', 100)}


def c(cor=''):
    return f'\033[{cor}m'


def lin(text):
    print(f'{c("1")}~{c()}' * 60)
    print(f'{c("1")}{text.center(60)}{c()}')
    print(f'{c("1")}~{c()}' * 60)


def linha():
    print(f'{c("1")}~{c()}' * 60)


def mostramenu(menu):
    lin('MENU PRINCIPAL')
    for cont, va in enumerate(menu):
        print(f"{c('93')}{cont + 1}{c()} - {c('94')}{va}{c()}")
    linha()


def validaopt():
    while True:

        try:
            opc = int(input(f"{c('33')}Sua Opção: {c()}"))
        except Exception:
            print(f"{c('91')}Digite uma Opção válida.")
        except KeyboardInterrupt:
            opc = 3
            print(f"\n{c('91')}Programa Interrompido.{c()}")
            break
        else:
            if 1 != opc != 2 != opc != 3:
                print(f"{c('91')}O valor \'{opc}\' não está dentro das opções...{c()}")
                print(f"{c('91')}Digite uma Opção válida.")
            else:
                break
    return opc


def mostrapessoas():
    cont1 = 0
    lin('PESSOAS CADASTRADAS')
    print(f"{c('1')}{'No.': <5}", end='')
    print(f"{'NOME': <40}", end='')
    print(f' IDADE{c()}         ')
    for k, v in pessoas.items():
        print(f'{cont1: <5}', end='')
        cont1 += 1
        print(f'{v[0].capitalize(): <40}', end=' ')
        print(f'{v[1]: <3} anos')
        sleep(0.3)


def novocadastro():
    lin('NOVO CADASTRO')
    try:
        nome = input('Nome: ').capitalize()
    except KeyboardInterrupt:
        nome = "<desconhecido>"
        print(f"\n{c('91')}Programa Interrompido.{c()}")
    if nome.strip() == '':
        nome = "<desconhecido>"
    while True:
        try:
            idade = int(input('Idade: '))
        except KeyboardInterrupt:
            print(f'\n{c("31")}O usuário preferiu não digitar a idade.{c()}')
            idade = '-'
            pessoas[f'pessoa{len(pessoas)}'] = nome, idade
            break
        except Exception:
            print(f'{c("91")}Por Favor, Digite um valor inteiro válido.{c()}')
        else:
            pessoas[f'pessoa{len(pessoas)}'] = nome, idade
            linha()
            print(f"{c('92')}Registro de {nome.split()[0]} adicionado com sucesso.{c()}")
            break
