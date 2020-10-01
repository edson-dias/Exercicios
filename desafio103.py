def ficha(nome='<desconhecido>', gols=0):
    print('-=' * 30)
    print(f'O jogador {nome} fez {gols} gols')
    print('-=' * 30)


# n = str(input('Nome do jogador: '))
# g = str(input('Quantidade de gols: '))
# if g.isnumeric():
#     g = int(gols)
# else:
#     g = 0
#
# if n.strip() == '':
#     ficha(gols = g)
# else:
#     ficha(n, g)



ficha(gols=2)