lista = list()
expr = input('Digite uma expressão: ')
for w in expr:
    lista.append(w)
if lista.count('(') == lista.count(')'):
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')
