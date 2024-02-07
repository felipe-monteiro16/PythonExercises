p = []
for c in range(0, 5):
    p.append(float(input('Insira o peso: Kg ')))
print('O maior peso foi {}Kg e o menor foi {}Kg'.format(max(p), min(p)))
print(p)