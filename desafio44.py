preco = float(input('Digite o Valor a ser pago: '))
opcao = int(input('Qual a opção de pagamento? \n\033[1;34m1\033[m - à vista no dinheiro'
                  '\n\033[1;34m2\033[m - à vista no cartão\n\033[1;34m3\033[m - 2x no cartão'
                  '\n\033[1;34m4\033[m - 3x ou mais no cartão\n'))

if opcao == 1:
    print('O valor total ficará: R$ {:.2f}'.format(preco * 0.90))
elif opcao == 2:
    print('O valor total ficará: R$ {:.2f}'.format(preco * 0.95))
elif opcao == 3:
    print('O valor total ficará: R$ {:.2f}, sendo 2x de R$ {:.2f}'.format(preco, preco / 2))
elif opcao == 4:
    print('O valor total ficará: R$ {:.2f}, sendo 3x de R$ {:.2f}'.format(preco * 1.2, preco / 3))
else:
    print('Opção Inválida! ')
