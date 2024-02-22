# Aqui estão as funções para a interface.
from time import sleep


def c(cor=''):
    """
    -> Função para adicionar cores nas strings.
    :param cor: Código numérico da cor
    :return: Código da cor
    """
    return f'\033[{cor}m'


def lin(text):
    """
    -> Função para fazer um cabeçalho com texto alinhado
    :param text: texto para fazer cabeçalho
    :return: mostra um cabeçalho pronto e formatado
    """
    print(f'{c("1")}~{c()}' * 60)
    print(f'{c("1")}{text.center(60)}{c()}')
    print(f'{c("1")}~{c()}' * 60)


def linha():
    """
    Função para mostrar uma linha de 60 caracteres.
    :return: Linha
    """
    print(f'{c("1")}~{c()}' * 60)


def mostra_menu(menu):
    """
    -> Função para fazer um menu personalizado.
    :param menu: Lista de strings utilizadas no menu
    :return: Um menu personalizado
    """
    lin('MENU PRINCIPAL')
    for cont, va in enumerate(menu):
        print(f"{c('93')}{cont + 1}{c()} - {c('94')}{va}{c()}")
    linha()


def valida_opt():
    """
    -> Função para validar a opção escolhida no menu, com tratamento de erro
    para caso não seja digitado uma das opções citadas.
    :return: Mensagem de erro para respostas incorretas.
    """
    while True:
        try:
            opc = int(input(f"{c('33')}Sua Opção: {c()}"))
        except Exception:
            print(f"{c('91')}Digite uma Opção válida.")
            sleep(0.5)
        except KeyboardInterrupt:
            opc = 3
            print(f"\n{c('91')}Programa Interrompido.{c()}")
            break
        else:
            if 1 != opc != 2 != opc != 3:
                print(f"{c('91')}O valor \'{opc}\' não está dentro das opções...{c()}")
                sleep(0.5)
                print(f"{c('91')}Digite uma Opção válida.")
                sleep(0.5)
            else:
                break
    return opc


def nome_maiusculo(n=''):
    """
    -> Função para deixar a primeira letra de cada nome/sobrenome maiúsculo,
    com exceção dos sobrenomes de até duas letras.
    :param n: Nome a ser formatado.
    :return: Nome formatado.
    """
    nome_teste = n.split()
    for cont, nom in enumerate(nome_teste):
        if len(nom) > 2:
            nome_teste[cont] = nome_teste[cont].capitalize()
    print(nome_teste)
    nome = ''
    for cont in nome_teste:
        nome += cont
        nome += ' '
    return nome.strip()


