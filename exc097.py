def escreva(txt):
    a = len(txt) + 4
    print('~' * a)
    print(f'{txt: ^{a}}')
    print('~' * a)


escreva('teste  ')
escreva('Curso de Python no Youtube')
escreva('a')
