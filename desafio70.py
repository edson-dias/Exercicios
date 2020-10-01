soma = count = 0
contador = 1

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    soma += preco

    if preco > 1000:
        count += 1

    if contador == 1:
        precomenor = preco

    if precomenor > preco:
        precomenor = preco
        nomebarato = nome

    contador += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if continuar == 'N':
        break

print(f'O total da compra R${soma:.2f}.')
print(f'Foram comprados {count} itens com preço acima de R$1000,00')
print(f'O produto mais barato foi {nomebarato}')
