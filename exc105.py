def notas(*n, sit=False):
    """
    —> Função para analisar nota e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param sit: Mostrar situação ou não (opcional).
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    di = {'total': len(n), "maior": max(n), "menor": min(n)}
    di["media"] = sum(n)/di["total"]
    if sit:
        if di["media"] < 6:
            di['situacao'] = 'RUIM'
        if 6 <= di['media'] < 8:
            di['situacao'] = 'BOA'
        if 8 <= di["media"] <= 10:
            di['situacao'] = 'ÓTIMA'
    return di


print('~' * 50)
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
