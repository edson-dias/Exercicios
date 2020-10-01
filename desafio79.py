lista = []

while True:
    n = int(input('Digite um valor: '))

    if n in lista:
        print('Número já cadastrado!')
    else:
        lista.append(n)

    flag = str(input('Deseja digitar mais um número? [S/N]: '))

    if flag in 'Nn':
        break

lista.sort()
print(f'Os números digitados foram: {lista}')
