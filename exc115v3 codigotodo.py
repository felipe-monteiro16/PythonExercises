# -*- coding: latin-1 -*-
from time import sleep

"""
    Esse � o mesmo c�digo do diret�rio exc115v3, contudo em um arquivo s�, e, consequentemente, bem menos organizado.
    Nesse programa ser� mostrado um menu com tr�s op��es do que fazer, na op��o de ver as pessoas, ir� mostrar as
cadastradas, na op��o de cadastrar uma nova ir� pedir o nome e a idade e ser� adicionada uma nova, e na op��o de sair,
ir� sair do sistema, contudo, os dados continuar�o salvos mesmo depois que encerrar o programa.
    O c�digo foi feito como o �ltimo projeto do curso de Python at� ent�o, tentei fazer com que o programa n�o desse 
erro independente do que a pessoa que estivesse executando fizesse. :)
"""


'''
Essas s�o as fun��es relacionadas ao arquivo e seu tratamento
'''


def arquivo_existe(nome):
    """
    -> Fun��o para verificar se o arquivo txt existe no diret�rio.
    :param nome: Nome do arquivo de texto
    :return: 'False' se n�o existir e 'True' se existir.
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
    -> Fun��o para criar novo arquivo de texto (acionada caso ele n�o exista).
    :param nome: Nome do arquivo de texto.
    :return: Arquivo de texto criado com mensagem informando o ocorrido
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception:
        print('\033[91mHouve um erro na cria��o do arquivo\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def mostra_pessoas():
    """
    -> Fun��o para mostrar as pessoas cadastradas no sistema, dados salvos no arquivo de texto
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
    -> Fun��o para cadastrar uma nova pessoa e salvar no arquivo de texto.
    :return: Mensagem mostrando sse o processo deu certo ou n�o.
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
            print(f'\n{c("31")}O usu�rio preferiu n�o digitar a idade.{c()}')
            idade = '-'
            nome = nome_maiusculo(nome)
            with open('cursoemvideo.txt', 'a') as f:
                f.write(f'{nome};{idade}\n')
            break
        except Exception:
            print(f'{c("91")}Por Favor, Digite um valor inteiro v�lido.{c()}')
        else:
            nome = nome_maiusculo(nome)
            with open('cursoemvideo.txt', 'a') as f:
                f.write(f'{nome};{idade}\n')
            linha()
            print(f" {c('92')}Registro de {nome.split()[0]} adicionado com sucesso.{c()}")
            break


'''
Aqui est�o as fun��es para a interface.
'''


def c(cor=''):
    """
    -> Fun��o para adicionar cores nas strings.
    :param cor: C�digo num�rico da cor
    :return: C�digo da cor
    """
    return f'\033[{cor}m'


def lin(text):
    """
    -> Fun��o para fazer um cabe�alho com texto alinhado
    :param text: texto para fazer cabe�alho
    :return: mostra um cabe�alho pronto e formatado
    """
    print(f'{c("1")}~{c()}' * 60)
    print(f'{c("1")}{text.center(60)}{c()}')
    print(f'{c("1")}~{c()}' * 60)


def linha():
    """
    Fun��o para mostrar uma linha de 60 caracteres.
    :return: Linha
    """
    print(f'{c("1")}~{c()}' * 60)


def mostra_menu(menu):
    """
    -> Fun��o para fazer um menu personalizado.
    :param menu: Lista de strings utilizadas no menu
    :return: Um menu personalizado
    """
    lin('MENU PRINCIPAL')
    for cont, va in enumerate(menu):
        print(f"{c('93')}{cont + 1}{c()} - {c('94')}{va}{c()}")
    linha()


def valida_opt():
    """
    -> Fun��o para validar a op��o escolhida no menu, com tratamento de erro
    para caso n�o seja digitado uma das op��es citadas.
    :return: Mensagem de erro para respostas incorretas.
    """
    while True:
        try:
            opc = int(input(f"{c('33')}Sua Op��o: {c()}"))
        except Exception:
            print(f"{c('91')}Digite uma Op��o v�lida.")
            sleep(0.5)
        except KeyboardInterrupt:
            opc = 3
            print(f"\n{c('91')}Programa Interrompido.{c()}")
            break
        else:
            if 1 != opc != 2 != opc != 3:
                print(f"{c('91')}O valor \'{opc}\' n�o est� dentro das op��es...{c()}")
                sleep(0.5)
                print(f"{c('91')}Digite uma Op��o v�lida.")
                sleep(0.5)
            else:
                break
    return opc


def nome_maiusculo(n=''):
    """
    -> Fun��o para deixar a primeira letra de cada nome/sobrenome mai�sculo,
    com exce��o dos sobrenomes de at� duas letras.
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


# Criando o arquivo de texto para caso ele n�o exista
arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)


'''
E aqui est� a fun��o para executar todas as outras
'''


def geral():
    """
    -> Fun��o que faz o loop do menu e que ativa as respectivas fun��es
    :return: Tudo aquilo que � para mostrar no programa
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
