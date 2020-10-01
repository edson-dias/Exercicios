r1 = float(input('Digite o segmento: '))
r2 = float(input('Digite o segmento: '))
r3 = float(input('Digite o segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem gerar um triângulo!')
else:
    print('Os segmentos não podem gerar um triângulo!')
