a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))
if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('Essas retas podem formar um triângulo.')
    if a == b == c:
        print('Esse triângulo é equilátero')
    elif a == b or a == c or b == c:
        print('Esse triângulo é isósceles')
    elif a != b != c != a:
        print('Ese triângulo é escaleno')
else:
    print('Essas retas não podem formar um triângulo.')
