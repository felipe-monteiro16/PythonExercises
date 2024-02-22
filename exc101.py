def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if 0 < idade < 16:
        return "\033[34;1mNÃO VOTA\033[32m"
    if 18 > idade >= 16 or idade >= 65:
        return "\033[33;1mVOTO OPCIONAL\033[33m"
    if 65 > idade >= 18:
        return "\033[32;1mVOTO OBRIGATÓRIO\033[31m"
    if idade < 0:
        return "\033[31;1mERRO\033[31m"


print('=' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
