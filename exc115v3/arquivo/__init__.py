from exc115v3.interface import *


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
                f.write(f'\n{nome};{idade}')
            break
        except Exception:
            print(f'{c("91")}Por Favor, Digite um valor inteiro válido.{c()}')
        else:
            nome = nome_maiusculo(nome)
            with open('cursoemvideo.txt', 'a') as f:
                f.write(f'\n{nome};{idade}')
            linha()
            print(f" {c('92')}Registro de {nome.split()[0]} adicionado com sucesso.{c()}")
            break
