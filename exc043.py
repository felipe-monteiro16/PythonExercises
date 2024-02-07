peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc < 25:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbita')
print('Seu IMC é de {:.2f}.'.format(imc))

