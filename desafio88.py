from random import randint

lista = list()
temp = list()

n = int(input('Quantos jogos você deseja que eu sorteie? '))

for i in range(0, n):

    for j in range(0, 6):

        aleat = randint(1, 60)

        while aleat in temp:
            aleat = randint(1, 60)

        temp.append(aleat)

    lista.append(temp[:])
    temp.clear()

for k in range(0, n):
    lista[k].sort()
    print(lista[k])

