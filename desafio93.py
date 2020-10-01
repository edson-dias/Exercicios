som = 0
dicio = dict()

dicio['Nome'] = str(input('Nome do Jogador: '))
dicio['Partidas'] = int(input('Quantidade de partidas jogadas: '))

for i in range(0, dicio['Partidas']):
    j = 'Partida ' + str(i + 1)
    dicio[j] = int(input(f'Gols feitos na partida {i + 1}: '))
    som += dicio[j]

for k, v in dicio.items():
    print(f'{k} = {v}')
print(f'Total de gols no campeonato: {som}')
