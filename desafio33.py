v1 = int(input('Digite um valor inteiro: '))
v2 = int(input('Digite um valor inteiro: '))
v3 = int(input('Digite um valor inteiro: '))
if v1 > v2:
    if v1 > v3:
        print('O maior valor é: {}'.format(v1))
    else:
        print('O maior valor é: {}'.format(v3))

    if v2 < v3:
        print('O menor valor é: {}'.format(v2))
    else:
        print('O menor valor é: {}'.format(v3))

else:
    if v2 > v3:
        print('O maior valor é: {}'.format(v2))
    else:
        print('O maior valor é: {}'.format(v3))

    if v1 < v3:
        print('O menor valor é: {}'.format(v1))
    else:
        print('O menor valor é: {}'.format(v3))

# if b<a and b<c: <------- forma mais simplificada de fazer o código
