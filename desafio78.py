lista = []

for i in range(0, 5):
    lista.append(int(input('Digite uma valor: ')))

    if i == 0:
        menor = maior = lista[0]

    if lista[i] < menor:
        menor = lista[i]
        menorposicao = i

    if lista[i] > maior:
        maior = lista[i]
        maiorposicao = i

print(f'O maior valor digitado foi {maior} na posição: {maiorposicao}')
print(f'O menor valor digitado foi {menor} na posição: {menorposicao}')
