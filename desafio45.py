from random import choice
# from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
cl = str(input('Escolha Pedra, Papel ou tesoura: ')).strip().upper()

if pc.upper() == cl:
    print('Empatamos! ')

elif pc.upper() == 'PEDRA':
    if cl == 'TESOURA':
        print('Pedra ganha de Tesoura! Eu ganhei! ')

    elif cl == 'PAPEL':
        print('Pedra perde para papel, você ganhou :( ')

elif pc.upper() == 'PAPEL':
    if cl == 'TESOURA':
        print('Papel perde para Tesoura! Eu perdi :( ')

    elif cl == 'PEDRA':
        print('Papel ganha de pedra, você perdeu! HAHAHAHA')

elif pc.upper() == 'TESOURA':
    if cl == 'PEDRA':
        print('Tesoura perde para pedra! :9')

    elif cl == 'PAPEL':
        print('Tesoura ganha de papel! Você perdeu!!!')
