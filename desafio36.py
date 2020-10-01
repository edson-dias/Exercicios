vc = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salário: '))
anos = int(input('Financiar em quantos anos: '))
prest = vc / (anos*12)
if prest >= sal*0.3:
    print('Não podemos financiar com R$ {:.2f} como prestação!'.format(prest))
else:
    print('Seu financiamento ficou: {} parcelas de R$ {:.2f}'.format(anos*12, prest))
