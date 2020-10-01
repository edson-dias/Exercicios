def mostraLinha(v):
    print('-' * 30)
    print(v)
    print('-' * 30)


def soma(
        *valores):  # Colocando * na frente do parâmetro, o programa realiza um empacotamento dos dados. O resultado disso é uma tupla.
    s = 0
    for n in valores:
        s += n
    print(f'A soma foi: {s}')


def testeListas(lst):  # lst é uma lista, para este tipo de parâmetro não importa a quantidade de itens dentro da lista.
    for i in range(0, len(lst)):
        lst[i] *= 2
    print(lst)


mostraLinha('Cabeçalho')
soma(2, 4, 6, 10)
exemplo = [2, 5, 4]
testeListas(exemplo)
