lista = 'lapis', 1.75, 'borracha', 5.52, 'caderno', 10.54, 'caneta', 6.47, 'penal', 8.47

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R$ {lista[i]:>5.2f}')

