import random
v1 = int(input('Pensei em um número aleatório de 0 a 5, tente adivinhar qual eu pensei: '))
v2 = random.randint(0,5)
if v1 == v2:
    print('Você acertou!')
else:
    print('HAHA! VOCÊ ERROU! Eu escolhi o: {}'.format(v2))
