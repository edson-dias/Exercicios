flag = 1
while flag != 0:
    nome = str(input('Digite o seu sexo: [M/F]: ')).strip().upper()[0]
    if nome != 'M' and nome != 'F':
        print('Caractere Errado. Digite novamente!')
    else:
        flag = 0

#while sexo not in 'MmFf':
