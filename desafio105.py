pythondef notas(*lst, sit=False):
    '''

    :param lst: dsadsda
    :param sit: dsadas
    :return: sadsadasda


    '''

    dicio = dict()

    som = 0

    for i in range(0, len(lst)):
        som += lst[i]

    dicio['Quantidade de Notas'] = len(lst)
    dicio['Média da Turma'] = som / len(lst)
    dicio['Maior nota'] = max(lst)
    dicio['Menor nota'] = min(lst)

    if som / len(lst) >= 6.0:
        msg = 'Tudo Ok!'
    else:
        msg = 'Nada Ok!'

    if sit:
        dicio['Situação'] = msg

    return dicio


n = notas(3, 5, 3.5, 15, 10, sit=False)
print(n)
help(notas)