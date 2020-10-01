n1 = float(input('Nota: '))
n2 = float(input('Nota: '))
media = (n1 * n2) / 2
if media < 5.0:
    print('Reprovado!')
elif 5.0 <= media < 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')
