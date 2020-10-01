peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print('Seu IMC é: {:.2f}! Você está abaixo do peso!'.format(imc))

elif 18.5 <= imc < 25:
    print('Seu IMC é: {:.2f}! Você está com o peso ideal!'.format(imc))

elif 25 <= imc < 30:
    print('Seu IMC é: {:.2f}! Você está com sobrepeso!'.format(imc))

elif 30 <= imc < 40:
    print('Seu IMC é: {:.2f}! Você está Obeso!'.format(imc))

else:
    print('Seu IMC é: {:.2f}! Você está obeso mórbido!'.format(imc))
