from time import sleep
from random import randint

count = 0

while True:
    m = randint(0, 10)
    n = int(input('Escolha um valor entre 0 e 10: '))
    escolha = str(input('Escolha Par ou ímpar [P/I]: ')).strip().upper()

    print('1 ...')
    sleep(0.5)
    print('2 ...')
    sleep(0.5)
    print('3 ...')
    sleep(0.5)
    print('e ...')
    sleep(0.5)
    print('JÁ ...')
    sleep(0.5)

#while tipo not in 'PpIi'
    if (n + m) % 2 == 0:

        if escolha == 'P':
            print(f'Eu escolhi {m} e você escolheu {n}, {m + n} é Par, você ganhou!')

        elif escolha == 'I':
            print(f'Eu escolhi {m} e você escolheu {n}, {m + n} é Par, você perdeu!')
            break
    else:

        if escolha == 'I':
            print(f'Eu escolhi {m} e você escolheu {n}, {m + n} é Ímpar, você ganhou!')

        elif escolha == 'P':
            print(f'Eu escolhi {m} e você escolheu {n}, {m + n} é Ímpar, você perdeu!')
            break
    count += 1

print(f'Game Over! Vocẽ ganhou {count} vezes')

