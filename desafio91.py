from random import randint
from operator import itemgetter

rank = list()

jogo = {'Jogador1': randint(0, 10),
        'Jogador2': randint(0, 10),
        'Jogador3': randint(0, 10),
        'Jogador4': randint(0, 10)}

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')
