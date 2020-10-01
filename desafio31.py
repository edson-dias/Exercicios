quilo = float(input('Digite a distância percorrida: '))
if quilo <= 200:
    print('O total da viagem será: R${:.2f}'.format(quilo*0.5))
else:
    print('O total da viagem será: R${:.2f}'.format(quilo*0.45))
