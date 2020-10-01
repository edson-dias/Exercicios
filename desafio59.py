v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:

    opcao = int(input('Qual operação deseja realizar: \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5]Sair do programa\n'))

    if opcao == 1:
        print('A soma dos valores é: {:.2f}'.format(v1 + v2))

    elif opcao == 2:
        print('A multiplicação dos valores é: {:.2f}'.format(v1 * v2))

    elif opcao == 3:
        if v1 > v2:
            print('O maior valor digitado foi: {:.2f}'.format(v1))
        elif v1 == v2:
            print('Não há maior valor!')
        else:
            print('O maior valor digitado foi: {:.2f}'.format(v2))

    elif opcao == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Finalizando o programa!')

    print('\n')
