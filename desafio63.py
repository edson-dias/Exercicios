n = int(input('Digite um número inteiro: '))
a1 = 0
a2 = 1

print('{} - {} - '.format(a1, a2), end='')

cont = 3

while cont <= n:

    a3 = a2 + a1
    print('- {} -'.format(a3), end='')
    a1 = a2
    a2 = a3
    cont += 1
