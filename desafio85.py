temp = list()
lista = [], []

for i in range(0, 7):
    n = int(input('Digite um valor '))
    if n % 2 == 0:
        lista[0].insert(0, n)
        # lista[0].append(n) tbm funciona!
    elif n % 2 == 1:
        lista[1].insert(0, n)
lista[0].sort()
lista[1].sort()
print(lista)
