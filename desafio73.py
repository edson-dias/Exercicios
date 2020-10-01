brasileiro = 'Corinthians', 'Atlético', 'Coritiba', 'Parana', 'flamengo', 'Palmeiras', 'Gremio'

print(f'Os quatro primeiros colocados são: {brasileiro[0:4]}')
print(f'Os quatro últimos colocados são {brasileiro[-4:]}')
print(f'Os times em ordem alfabética: {sorted(brasileiro)}')
print(f'O parana está na posição: {brasileiro.index("Parana") + 1}')

