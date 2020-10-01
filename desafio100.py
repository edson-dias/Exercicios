numeros = list()
from random import randint


def sorteia(lst):
    for i in range(0, 5):
        lst.append(randint(0, 10))
    print(lst)


def somaPar(lista):
    som = 0
    for i in lista:
        if i % 2 == 0:
            som += i
    print(som)



sorteia(numeros)
somaPar(numeros)