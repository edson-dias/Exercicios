from datetime import date

cont = 0

for i in range(0, 7):
    nasc = int(input('Digite o ano que que você nasceu: '))

    if date.today().year - nasc >= 18:
        cont = cont + 1

if cont == 7:
    print('Todas as 7 pessoas já atingiram a maioridade!')
else:
    print('{} pessoa(s) já atingiram a maioridade e {} pessoa(s) ainda não atingiram a maioridade'.format(cont, 7 - cont))
