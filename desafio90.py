dicionario = dict()

dicionario['Nome'] = str(input('Digite o nome do aluno: '))
dicionario['media'] = float(input(f'Digite a média do aluno {dicionario["Nome"]}: '))

if dicionario['media'] >= 7.0:
    dicionario['Situacao'] = 'Aprovado'

elif dicionario['media'] < 7:
    dicionario['Situacao'] = 'Recuperação'

elif dicionario['media'] < 5:
    dicionario['Situacao'] = 'Reprovado'

for k, v in dicionario.items():
    print(f'{k} = {v}')