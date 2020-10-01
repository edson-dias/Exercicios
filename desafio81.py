lista = []
count = 0

while True:

    lista.append(int(input('Digite um valor: ')))
    conf = str(input('Deseja continuar? [S/N]: '))
    count += 1

    if conf in 'Nn':
        break

print(f'Foram digitados {count} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')


