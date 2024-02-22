from exc115v2.interface import *


def geral():
    while True:
        # Mostrando o menu principal personalizado
        mostramenu(["Ver pessoas cadastradas", "Cadastrar uma nova pessoa", "Sair do sistema"])
        op = validaopt()
        # Mostrando as pessoas cadastradas
        if op == 1:
            mostrapessoas()
        # Adicionando uma nova pessoa
        if op == 2:
            novocadastro()
        # Finalizando o programa
        if op == 3:
            lin('VOLTE SEMPRE!')
            break


geral()
