num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(3, 0)
print(num)
# num.pop(2)
print(num)
num.remove(2) # remove apenas o primeiro elemento que encontrar. Se tiver mais de um 2 ele removerá apenas o primeiro.

valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

a = [2, 3, 4, 7]
b = a       # linkou as listas. Se alterar um valor em uma, altera o valor em outra
b[2] = 8
print(a)
print(b)
b = a[:]    # aqui foi feito uma cópia de todos os elementos de a, assim não se cria o link

