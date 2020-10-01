n = int(input('DIgite um inteiro: '))

fatorial = n

while n != 1:
    print(' {} '.format(n), end='x')

    fatorial = fatorial * (n - 1)
    n = n - 1

print(' {} '.format(n))
print('O fatorial deste número é: {}'.format(fatorial))
