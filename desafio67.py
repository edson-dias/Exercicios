while True:
    n = int(input('Digite a tabuada desejada! Para sair tecle um número negativo! '))

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
