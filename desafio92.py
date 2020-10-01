from datetime import date

dicio = dict()

dicio['Nome'] = str(input('Digite o nome: '))
dicio['Nasc'] = int(input('Digite o ano de nascimento: '))
dicio['CTPS'] = int(input('Digite a CTPS sem pontuação: (Caso nao tenha, digite "0") '))
dicio['Idade'] = date.today().year - dicio['Nasc']

if dicio['CTPS'] != 0:

    dicio['Ano'] = int(input('Digite o ano de contratação: '))
    dicio['Sálario'] = float(input('Digite o sálario: '))
    # dicio['Aposentadoria'] = preguiça de fazer.

    print('Funcionário 1:')
    print('-'*30)
    for k, v in dicio.items():
        print(f'{k} = {v}')

else:
    for k, v in dicio.items():
        print(f'{k} = {v}')