# -*- coding: latin-1 -*-
from time import sleep

"""
    Esse é o mesmo código do diretório exc115v3, contudo em um arquivo só, e, consequentemente, bem menos organizado.
    Nesse programa será mostrado um menu com três opções do que fazer, na opção de ver as pessoas, irá mostrar as
cadastradas, na opção de cadastrar uma nova irá pedir o nome e a idade e será adicionada uma nova, e na opção de sair,
irá sair do sistema, contudo, os dados continuarão salvos mesmo depois que encerrar o programa.
    O código foi feito como o último projeto do curso de Python até então, tentei fazer com que o programa não desse 
erro independente do que a pessoa que estivesse executando fizesse. :)
"""


'''
# Essas são as funções relacionadas ao arquivo e seu tratamento
'''


def arquivo_existe(nome):
    """
    -> Função para verificar se o arquivo txt existe no diretório.
    :param nome: Nome do arquivo de texto
    :return: 'False' se não existir e 'True' se existir.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
    -> Função para criar novo arquivo de texto (acionada caso ele não exista).
    :param nome: Nome do arquivo de texto.
    :return: Arquivo de texto criado com mensagem informando o ocorrido
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception:
        print('\033[91mHouve um erro na criação do arquivo\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def mostra_pessoas():
    """
    -> Função para mostrar as pessoas cadastradas no sistema, dados salvos no arquivo de texto
    :return: As pessoas cadastradas e suas respectivas idades de forma formatada
    """
    contador = 0
    lin('PESSOAS CADASTRADAS')
    print(f"{c('1')}{'No.': <5}", end='')
    print(f"{'NOME': <40}", end='')
    print(f' IDADE{c()}')
    with open('cursoemvideo.txt', 'r') as f:
        for li in f:
            print(f'{contador: <5}', end='')
            nome1 = li.split(";")[0]
            idade1 = li.split(";")[1].replace('\n', '')
            print(f'{nome1: <41}{idade1: <3} anos')
            contador += 1
            sleep(0.3)


def novo_cadastro():
    """
    -> Função para cadastrar uma nova pessoa e salvar no arquivo de texto.
    :return: Mensagem mostrando sse o processo deu certo ou não.
    """
    lin('NOVO CADASTRO')
    try:
        nome = input('Nome: ').capitalize().strip()
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
            nome = nome_maiusculo(nome)
            with open('cursoemvideo.txt', 'a') as f:
                f.write(f'{nome};{idade}\n')
            break
        except Exception:
            print(f'{c("91")}Por Favor, Digite um valor inteiro válido.{c()}')
        else:
            nome = nome_maiusculo(nome)
            with open('cursoemvideo.txt', 'a') as f:
                f.write(f'{nome};{idade}\n')
            linha()
            print(f" {c('92')}Registro de {nome.split()[0]} adicionado com sucesso.{c()}")
            break


'''
Aqui estão as funções para a interface.
'''


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


# Criando o arquivo de texto para caso ele não exista
arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)


'''
E aqui está a função para executar todas as outras
'''


def geral():
    """
    -> Função que faz o loop do menu e que ativa as respectivas funções
    :return: Tudo aquilo que é para mostrar no programa
    """
    while True:
        # Mostrando o menu principal personalizado
        mostra_menu(["Ver pessoas cadastradas", "Cadastrar uma nova pessoa", "Sair do sistema"])
        op = valida_opt()
        if op == 1:
            # Mostrando as pessoas cadastradas
            mostra_pessoas()
        if op == 2:
            # Adicionando uma nova pessoa
            novo_cadastro()
        if op == 3:
            # Finalizando o programa
            lin('VOLTE SEMPRE!')
            break


geral()
