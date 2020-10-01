try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# except:
#     print('Infelizmente tivemos um problema!')  # Condição se der erro.

except (ValueError, TypeError):
    print('Tivemos um probma com os tipos de dados que você digitou')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

else:
    print(f'O resultado é {r:.1f}') # O que vai executar caso de certo. OPCIONAL!!

finally:
    print('Volte sempre! Muito obrigado!') # O que sempre vai mostrar, independente se der falha ou não. OPCIONAL!!

# except Exception as erro:
    # print(f'Problema encontrado foi {erro.__class__}') Para mostrar qual o erro.

