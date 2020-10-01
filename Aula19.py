# pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
# print(pessoas['nome'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5

brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[0]['uf']) #brasil[0].values() ou .keys() tbm funciona

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


