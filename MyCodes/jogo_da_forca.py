from random import choice
import sys
try:
    from unidecode import unidecode
except ModuleNotFoundError:
    print('Vá ao terminal e digite: pip install unidecode')

palavras = ('ABACAXI', 'BANANA', 'COMPUTADOR', 'ELEFANTE', 'GIRAFA', 'HIPOPÓTAMO', 'INTERNET', 'JACARÉ', 'KIWI',
            'LIMÃO', 'MACACO', 'NAVIO', 'OVELHA', 'PINGUIM', 'QUEIJO', 'RATO', 'SOL', 'TIGRE', 'URSO', 'VELA',
            'XADREZ', 'YACHT', 'ZEBRA', 'AVIÃO', 'BICICLETA', 'CACHORRO', 'DADO', 'ELETRICIDADE', 'FOCA', 'GATO',
            'HARPA', 'IATE', 'JARDIM', 'KETCHUP', 'LÂMPADA', 'MONTANHA', 'NUVEM', 'ÔNIBUS', 'PAPAGAIO', 'QUEBRA-CABEÇA',
            'RÃ', 'SAPATO', 'TARTARUGA', 'UVA', 'VENTO', 'WAFFLE', 'XÍCARA', 'YOGA', 'ZANGÃO', 'ÁRVORE')

num_erros = num_acertos = temp = 0
letras = []
tentativas = []
palavra = choice(palavras).upper()
p1 = p2 = p3 = p4 = p5 = p6 = p7 = ''


def lin(p='', n=70, cor='1;1', li='='):
    """
    -> Função para escrever mensagem centralizada com linhas encima e embaixo
    :param p: Palavra
    :param n: Número de caracteres
    :param cor: Número da cor que deseja usar
    :param li: Caractere que será usado como linha, ex: "="
    """
    linha = li * n
    print(f'\n{c(linha, cor)}')
    print(f"{c(f'{p:^{n}}', cor)}")
    print(f'{c(linha, cor)}\n')


def c(p='', cor=''):
    """
    -> Função para escrever mensagem colorida/com efeitos, ex: Negrito
    :param p: Texto a ser colorido
    :param cor: Número da cor/efeito
    :return: Mensagem com os efeitos/cores escolhidos
    """
    return f'\033[{cor}m{p}\033[m'


def desenha_jogo(cor='34;1'):
    """
    -> Função que mostra na tela tudo aquilo que não exige iteratividade no jogo,
    ex: desenho, tentativas corretas, tentativas usadas.
    :param cor: Cor que o desenho do boneco ficará, padrão Vermelho Negrito.
    """
    global num_erros, palavra, p1, p2, p3, p4, p5, p6, p7

    # Verificando a quantia de erros

    if num_erros == 1:
        p1 = 'O'
    if num_erros == 2:
        p2 = ' |'
    if num_erros == 3:
        p3 = '/'
        p2 = '|'
    if num_erros == 4:
        p4 = '\\'
    if num_erros == 5:
        p5 = '|'
    if num_erros == 6:
        p6 = '/'
    if num_erros == 7:
        p7 = '\\'

    # Mostrando o Jogo

    print(c(f'''
       _ _ _ _ _                
      | /       |               
      |/        {p1}            
      |        {p3}{p2}{p4}     
      |         {p5}            
      |        {p6} {p7}        
      |                         
      |         ''', cor), end='')

    # Mostrando as tentativas corretas

    for con in range(0, len(palavra)):
        print(c(f'{letras[con]}', '21;1'), end=' ')
    print()
    print(c('     ======', cor))

    # Mostrando todas as tentativas incorretas

    print('\n    Letras Usadas:    ', end='')
    for le in tentativas:
        print(c(le, "9;1"), end=' ')
    print()


lin('JOGO DA FORCA')

# Preenchendo a lista com espaços e com travessão caso haja

for cont, letra in enumerate(palavra):
    letras.append(' ')
    if letra == '-':
        num_acertos += 1
        letras[cont] = letra

desenha_jogo()

while True:

    # Coletando o palpite do Jogador

    while True:

        # Tratamento de erro para programa interrompido ou valor inválido

        try:
            palpite = input(f'\nA palavra escolhida tem {len(palavra)} letras, qual o seu palpite? ').upper()
        except KeyboardInterrupt:
            print(c('\nPrograma Interrompido', '91'))
            sys.exit(1)
        if len(palpite) == 1 and not palpite.isnumeric() and palpite not in (tentativas + letras):
            if palpite.isalpha() and palpite.isascii():
                tentativas.append(palpite)
                break
        if palpite in (tentativas + letras) and not palpite.isspace():
            print(c(f'\nA Letra "{palpite}" já foi, tente outra.', '31'))
        elif not palpite.isalpha() or not palpite.isascii():
            print(c(f'\nSomente \033[4mletras não acentuadas\033[0;31m serão aceitas. Tente Novamente.', '31'))
        else:
            print(c('ERRO! Tente Novamente.', '91'))

    # Verificando acertos e mostrando resultado

    temp = num_acertos
    for cont, letra in enumerate(palavra):
        if palpite == unidecode(letra):
            num_acertos += 1
            letras[cont] = letra
    if temp == num_acertos:
        lin('ERROU', cor='31', li='-')
        num_erros += 1
    elif temp < num_acertos:
        lin('ACERTOU', cor='32', li='-')
    desenha_jogo()

    # Finalizando jogo

    if num_acertos == len(palavra) or num_erros == 7:
        break
if num_acertos == len(palavra):
    lin('FIM DE JOGO! VOCÊ GANHOU', cor='92;1')
elif num_erros == 7:
    lin('FIM DE JOGO! VOCÊ PERDEU', cor='91;1')
    for cont, letra in enumerate(palavra):
        letras[cont] = letra
    desenha_jogo('91;1')

# Fim.
