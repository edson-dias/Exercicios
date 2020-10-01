a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desta PA: '))

count = 0

while count != 10:

    print('A{} = {}'.format(count + 1, a1))
    a1 += r
    count += 1
