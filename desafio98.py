from time import sleep


def contagem():
    for j in range(0, 10):
        print(j + 1, end=' ')
        sleep(0.5)

    print('\n')

    for k in range(10, -2, -2):
        print(k, end=' ')
        sleep(0.5)

    print('Now it''s your turn!')
    i = int(input('Ínicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p != 0:
        for j in range(i, f, p):
            print(j, end=' ')
            sleep(0.5)
    else:
        for j in range(i, f):
            print(j, end=' ')
            sleep(0.5)


contagem()
