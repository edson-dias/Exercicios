a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desta PA: '))

count = 0

while count != 10:

    print('A{} = {}'.format(count + 1, a1))
    a1 += r
    count += 1

cont = 1

while cont != 0:
    cont = int(input('Deseja mostrar mais termos? Se sim digite a quantidade desejada, caso não digite 0: '))
    if cont != 0:
        cont += count
        while count != cont:
            print('A{} = {}'.format(count + 1, a1))
            a1 += r
            count += 1
