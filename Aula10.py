carro = int(input('Tempo do carro: '))
if carro <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('Fim do programa!')
print('#'*15)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média: {:.2f}'.format(m))
if m < 7.0:
    print('Você foi reprovado!')
else:
    print('Você foi aprovado!')

