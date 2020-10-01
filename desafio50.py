soma = 0
print('Digite 6 números: ')

for i in range(0, 6):

    n = int(input())

    if n % 2 == 0:
        soma = soma + n

print('Os números pares somados são: {}'.format(soma))
