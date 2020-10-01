countm = countf = count = 0

while True:

    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()

# while sexo not in 'MF'

    if idade > 18:
        count += 1

    if sexo == 'M':
        countm += 1

    elif sexo == 'F':
        countf += 1

    continuar = str(input('Deseja cadastrar mais alguma pessoa? [S/N]: ')).strip().upper()

    if continuar == 'N':
        break

    print('')

print(f'Foram cadastradas {count} pessoas com idade acima de 18 anos.')
print(f'Foram cadastradas {countm} homens e {countf} mulheres.')
