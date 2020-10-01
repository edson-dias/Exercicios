lista = list()
temporario = list()


while True:
    temporario.append(str(input('Digite o nome: ')))
    temporario.append(int(input('Digite o peso: ')))
    lista.append(temporario[:])
    temporario.clear()
    flag = str(input('Deseja continuar? [S/N]: '))

    if flag in 'Nn':
        break


print(lista)

print(f'Os menores pesos foram: ', end='  ')

for p in lista:
    if p[1] <= 70:
        print(f'{p[0]} com {p[1]}Kg', end=' ')

print(f'\nOs maiores pesos foram: ', end=' ')

for p in lista:
    if p[1] >= 100:
        print(f'{p[0]} com {p[1]}Kg', end=' ')
