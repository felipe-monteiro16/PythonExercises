import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Pegundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
names = [n1, n2, n3, n4]
r = random.choice(names)
print('O aluno escolhido foi {}'.format(r))
