def cabecalho(tam=42, msg=''):
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)


def menu(lst):
    for i in range(0, len(lst)):
        print(f'\033[34m{lst[i]}\033[m')

    print('-' * 42)
