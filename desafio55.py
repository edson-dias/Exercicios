for i in range(0, 5):

    n = float(input('Digite o peso: '))

    if i == 0:
        maior = n
        menor = n

    else:

        if maior < n:
            maior = n

        if menor > n:
            menor = n

print('O menor peso foi: {}\nO maior peso foi: {}'.format(menor, maior))
