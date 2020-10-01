from math import hypot
cata = float(input('Digite o valor do cateto adjacente: '))
cato = float(input('Digite o valor do cateto oposto: '))
print('O valor da hipotenusa é: {:.2f}'.format(hypot(cata, cato)))
