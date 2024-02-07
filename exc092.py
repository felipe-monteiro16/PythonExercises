from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = int(datetime.now().year - ano)
dados['ctps'] = int(input('Carteira de trabalho: (0 não tem) '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (datetime.now().year - dados['contratação']) + dados['idade'])
print('=-' * 20)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
