valores = dict()
valores['nome'] = str(input('Nome: '))
valores['media'] = float(input(f'Média de {valores["nome"]}: '))
if 10 >= valores['media'] >= 6:
    valores['situacao'] = "APROVADO"
if 4 <= valores['media'] < 6:
    valores['situacao'] = 'RECUPERAÇÃO'
if 0 <= valores['media'] < 4:
    valores['situacao'] = 'REPROVADO'
if valores['media'] < 0 or valores['media'] > 10:
    valores['situacao'] = 'ERRO'
for k, v in valores.items():
    print(f'{k.capitalize()} é igual a {v}')
