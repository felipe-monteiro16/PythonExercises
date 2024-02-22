# -*- coding: latin-1 -*-
from exc115v3.arquivo import *


"""
    Nesse programa será mostrado um menu com três opções do que fazer, na opção de ver as pessoas, irá mostrar as
cadastradas, na opção de cadastrar uma nova irá pedir o nome e a idade ela será adicionada, e na opção de sair,
irá sair do sistema, contudo, os dados continuarão salvos mesmo depois que encerrar o programa.
    O código foi feito como o último projeto do curso de Python até então, tentei fazer com que o programa não desse 
erro independente do que a pessoa que estivesse executando fizesse. :)
"""


# Criando o arquivo de texto para caso ele não exista
arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)


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
