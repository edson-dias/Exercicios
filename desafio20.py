from random import shuffle
a = input('Nome do aluno: ')
b = input('Nome do aluno: ')
c = input('Nome do aluno: ')
d = input('Nome do aluno: ')
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
