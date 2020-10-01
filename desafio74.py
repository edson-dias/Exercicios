from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for j in n:
    print(f'{j} ', end='')

for i in range(0, len(n)):

    if i == 0:
        menor = n[0]
        maior = n[0]

    if n[i] < menor:
        menor = n[i]

    if n[i] > maior:
        maior = n[i]


print(f'\nO menor número randomico foi: {menor}')
print(f'O maior número randomico foi: {maior}')

# print(f'O maior valor sorteado foi {max(n)}')     Max e min exclui a necessidade do if
# print(f'O menor valor sorteado foi {min(n)}')