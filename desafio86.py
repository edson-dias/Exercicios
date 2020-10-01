lista = [], [], []
# Podia ter colocado os zeros dentro da declaração de lista e usado o comando lista[i][j] = int(input(''))

for i in range(0, 3):
    for j in range(0, 3):
        lista[i].append(int(input(f'Digite um número para a posição a{i}{j}: ')))

for i in range(0, 3):
    print(lista[i])
