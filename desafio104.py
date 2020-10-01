def leiaInt(text):
    while True:
        num = str(input(text))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mEntrada incorreta, digite novamente!\033[m')
    return num


n = leiaInt('Só um teste: ')
print(f'Voce acabou de digitar o número {n}')
