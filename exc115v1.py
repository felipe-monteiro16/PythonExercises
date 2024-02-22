from time import sleep
pessoas = ['ana paula vieira', 32, 'Cláudio Medonça', 18, 'Gustavo Guanabara', 41, 'Maria Clara Peixoto', 100]


def c(cor=''):
    return f'\033[{cor}m'


def lin(text):
    print(f'{c("1")}~{c()}' * 60)
    print(f'{c("1")}{text.center(60)}{c()}')
    print(f'{c("1")}~{c()}' * 60)


def linha():
    print(f'{c("1")}~{c()}' * 60)


def geral():
    cont1 = 0
    while True:
        # Mostrando o menu principal personalizado
        lin('MENU PRINCIPAL')
        print(f"{c('93')}1{c()} - {c('94')}Ver pessoas cadastradas")
        print(f"{c('93')}2{c()} - {c('94')}Cadastrar uma nova pessoa")
        print(f"{c('93')}3{c()} - {c('94')}Sair do sistema{c()}")
        linha()
        while True:
            try:
                opt = int(input(f"{c('33')}Sua Opção: {c()}"))
            except Exception:
                print(f"{c('91')}Digite uma Opção válida.")
            except KeyboardInterrupt:
                opt = 3
                print(f"\n{c('91')}Programa Interrompido.{c()}")
                break
            else:
                if 1 != opt != 2 != opt != 3:
                    print(f"{c('91')}O valor \'{opt}\' não está dentro das opções...{c()}")
                    print(f"{c('91')}Digite uma Opção válida.")
                else:
                    break
        # Mostrando as pessoas cadastradas
        if opt == 1:
            lin('PESSOAS CADASTRADAS')
            print(f"{c('1')}{'No.': <5}", end='')
            print(f"{'NOME': <40}", end='')
            print(f' IDADE{c()}         ')
            for cont, p in enumerate(pessoas):
                if cont % 2 == 0:
                    print(f'{cont1: <5}', end='')
                    cont1 += 1
                    print(f'{p.capitalize(): <40}', end=' ')
                else:
                    print(f'{p: <3} anos')
                    sleep(0.3)
        # Adicionando uma nova pessoa
        if opt == 2:
            lin('NOVO CADASTRO')
            try:
                nome = input('Nome: ').capitalize()
            except KeyboardInterrupt:
                nome = "<desconhecido>"
                print(f"\n{c('91')}Programa Interrompido.{c()}")
                break
            if nome.strip() == '':
                nome = "<desconhecido>"
            while True:
                try:
                    idade = int(input('Idade: '))
                except KeyboardInterrupt:
                    print(f'\n{c("31")}O usuário preferiu não digitar a idade.{c()}')
                    idade = '-'
                    pessoas.append(nome)
                    pessoas.append(idade)
                    break
                except Exception:
                    print(f'{c("91")}Por Favor, Digite um valor inteiro válido.{c()}')
                else:
                    pessoas.append(nome)
                    pessoas.append(idade)
                    linha()
                    print(f"{c('92')}Registro de {nome.split()[0]} adicionado com sucesso.{c()}")
                    break
        # Finalizando o programa
        if opt == 3:
            lin('VOLTE SEMPRE!')
            break


geral()
