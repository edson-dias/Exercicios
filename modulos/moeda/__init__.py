def aumentar(x, y, format=False):
    """
    :param x: valor
    :param y: porcentagem
    :return: valor acrescido da porcentagem.
    """
    x = x + (x * (y * 0.01))
    return x if format is False else moeda(x)


def diminuir(x, y, format=False):
    """
    :param x:valor
    :param y: porcentagem
    :return: valor acrescido da porcentagem
    """
    x = x - (x * (y * 0.01))
    return x if format is False else moeda(x)


def dobro(x, format=False):
    """
    :param x: valor a ser dobrado
    :return: valor dobrado
    """
    x *= 2
    return x if format is False else moeda(x)


def metade(x, format=False):
    """
    :param x: valor
    :return: metade do valor
    """
    x /= 2
    return x if format is False else moeda(x)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(x=0, y=0, format=False):
    print('-=' * 30)
    print(aumentar(x, y, format))
    print(diminuir(x, y, format))
    print(dobro(x, format))
    print(metade(x, format))
    print('-=' * 30)