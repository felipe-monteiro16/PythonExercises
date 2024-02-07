n = ('Zero', 'Um', 'Dois', 'Três',
     'Quatro', 'Cinco', 'Seis', 'Sete',
     'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
     'Treze', 'quatorze', 'Quinze', 'Dezesseis',
     'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou {n[num]}')
