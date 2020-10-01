dicio = dict()
lista = list()
listaf = list()
listamedia = list()

while True:

    dicio['Nome'] = str(input('Digite o nome: '))
    dicio['Sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
    dicio['Idade'] = int(input('Digita a idade: '))
    flag = str(input('Deseja continuar? [S/N]: '))

    lista.append(dicio.copy())

    if flag in 'Nn':
        break

print(f'Foram cadastradas {len(lista)} pessoas')

som = 0

for i in range(0, len(lista)):

    som += lista[i]['Idade']

    if lista[i]['Sexo'] in 'Ff':
        listaf.append(lista[i])

for i in range(0, len(lista)):

    if lista[i]['Idade'] >= (som / len(lista)):
        listamedia.append(lista[i])

print(f'A média das idades: {som / len(lista)}')
print(f'Apenas mulheres: {listaf}')
print(f'Apenas pessoas acima da média de idade: {listamedia}')
