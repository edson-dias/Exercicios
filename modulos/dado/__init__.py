def leiaDinheiro(msg):
    valido = False

    while not valido:

        entrada = str(input(msg)).replace(',', '.').strip()

        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu nao digitar nada')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o número.')
            return 0
        except (TypeError, ValueError):
            print('Digite um valor válido!')
            continue
        else:
            return n
