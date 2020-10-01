som = 0
dicio = dict()
lista = list()
listapartidas = list()

while True:
    dicio['Nome'] = str(input('Nome do Jogador: '))
    dicio['Partidas'] = int(input('Quantidade de partidas jogadas: '))

    for i in range(0, dicio['Partidas']):
        j = 'Partida ' + str(i + 1)
        dicio[j] = int(input(f'Gols feitos na partida {i + 1}: '))
        som += dicio[j]
        listapartidas.append()

    dicio['Total'] = som

    lista.append(dicio.copy())
    dicio.clear()

    flag = str(input('Deseja cadastrar mais um jogador? [S/N] '))

    if flag in 'Nn':
        break

for i in range(0, len(lista)):
    print(i+1, end=' ')
    print(lista[i]['Nome'], end='     ')
    print(listapartidas, end='      ')
    print(som)
