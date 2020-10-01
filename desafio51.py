'''a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desta PA: '))

termos = a1

print('Os dez primeiros termos da sua PA são: \n{}'.format(termos))

for i in range(1, 10):
    termos = termos + r
    print(termos) '''


a10 = a1 + (10-1)*r

for i in range(a1, a10 + r, r):
    print('{} '.format(i), end=' -> ')
print('Acabou!')
