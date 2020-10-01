from random import choice
a = input('Nome aluno: ')
b = input('Nome aluno: ')
c = input('Nome aluno: ')
d = input('Nome aluno: ')
lista = [a, b, c, d]
print('O aluno sorteado foi: {}'.format(choice(lista)))
