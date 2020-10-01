sal = float(input('Digite o salário do funcionário: R$ '))
if sal > 1250:
    print('O novo salário é: {:.2f}'.format(sal*1.1))
else:
    print('O novo salário é: {:.2f}'.format(sal*1.15))
