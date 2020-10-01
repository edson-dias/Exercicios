from random import randint

print('Pensei em um número entre 0 e 10!')

v1 = randint(0, 10)
v2 = int(input('Tente adivinhar qual: '))

if v1 != v2:

    cont = 1

    while v1 != v2:
        v2 = int(input('Você errou, tente novamente: '))
        cont += 1

    print('Finalmente! Você teve que tentar {} vezes para poder acertar!'.format(cont))

else:
    print('Você acertou de primeira, parabéns!')


