lista = [], [], []
som = somcol = 0

for i in range(0, 3):
    for j in range(0, 3):

        n = int(input(f'Digite um número para a posição a{i + 1}{j + 1}: '))

        if n % 2 == 0:
            som += n

        lista[i].append(n)

        if i == 1 and j == 0:
            maior = lista[i][0]

        if i == 1:
            if maior <= lista[i][j]:
                maior = lista[i][j]

for i in range(0, 3):
    print(lista[i])
    somcol += lista[i][2]

print(somcol)
print(maior)
