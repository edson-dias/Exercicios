somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for i in range(0, 4):
    print('----- {} Pessoa -----'.format(i + 1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('Media idade: {}'.format(mediaidade))
print('O home mais velho se chama: {}'.format(nomevelho))
print('Mulheres com menos de 20 anos: '.format(totmulher20))
