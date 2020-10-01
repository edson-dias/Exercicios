n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite 1 para binário, 2 para octal e 3 para conversão hexadecimal: '))
if n2 == 1:
    print('{} em binário: {}'.format(n1, bin(n1)))

elif n2 == 2:
    print('{} em octal: {}'.format(n1, oct(n1)))

elif n2 == 3:
    print('{} em Hexadecimal: {}'.format(n1, hex(n1)))

else:
    print('Número não identificado!')
