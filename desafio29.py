v1 = int(input('Digite a sua Velocidade: '))
if v1 > 80:
    print('Você foi multado! Você deve pagar: R${}.00'.format((v1-80)*7))
