from datetime import date
ano = int(input('Digite seu ano de nascimento: '))

if date.today().year - ano <= 9:
    print('Mirim!')

elif 9 < date.today().year - ano <= 14:
    print('Infantil')

elif 14 < date.today().year - ano <= 19:
    print('Junior')

elif 19 < date.today().year - ano <= 20:
    print('Sênior')

else:
    print('Master')
