def area(a, b):
    c = a * b
    print(f"A área de um terreno de {a}x{b} é de {c}m².")


print('-' * 30)
print(f'{"Controle de Terrenos": ^30}')
print('-' * 30)
area(float(input("Largura (m): ")),
     float(input("Comprimento (m): ")))
