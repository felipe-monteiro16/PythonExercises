p = float(input('Valor do produto: '))
print('Escolha sua condição de pagamento: ')
print('Digite 1: Á vista dinheiro/cheque: 10% de desconto')
print('Digite 2: Á vista no cartão: 5% de desconto')
print('Digite 3: Em até 2x no cartão: Preço normal')
print('Digite 4: 3x ou mais no cartão: 20% de juros')
c = int(input(''))
if c == 1:
    print('Seu produto custará R${:.2f}'.format((p/100)*90))
elif c == 2:
    print('Seu produto custará R${:.2f}'.format((p/100)*95))
elif c == 3:
    print('Seu produto custará R${:.2f}'.format(p))
    print('E terá 2 parcelas de R${:.2f}'.format(p/2))
elif c == 4:
    par = int(input('Quantas parcelas terá seu produto? '))
    print('Seu produto custará R${:.2f}'.format((p/100)*120))
    print('E terá {} parcelas de R${:.2f}'.format(par, p/par))
