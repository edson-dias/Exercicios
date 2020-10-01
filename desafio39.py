from datetime import date
idade = int(input('Digite seu ano de nascimento: '))
if date.today().year - idade < 18:
    print('Faltam {} ano(s) para você se alistar!'.format(18 - (date.today().year - idade)))

elif date.today().year - idade > 18:
    print('Você deveria ter se alistado a {} ano(s)!'.format(date.today().year - idade - 18))

else:
    print('Está na hora de se alistar!')
