n = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(
    input('Digite um número: '))

print(f'Foram digitados os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na posição: {n.index(3) + 1}')
else:
    print('Não foi digitado o valor 3')

for j in n:
    if j % 2 == 0:
        print(j, end=' ')
