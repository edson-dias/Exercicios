tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

flag = 1

while True:

    num = int(input('Digite um número de 0 a 10: '))

    if 0 <= num <= 10:
        break
    else:
        print('Entrada incorreta!')

print(f'Você digitou o número {tupla[num]}')
