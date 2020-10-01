from modulos.interface import *
from modulos.sistema import *

arq = 'arquivodetexto.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho(42, 'Menu Principal')
menu(['1 - Ver pessoas cadastradas', '2 - Cadastrar Nova Pessoa', '3 - Sair do Sistema'])

while True:
    n = validationNumber(f'\033[33mSua opção:\033[m ')

    if n == 1:
        showDados(arq)

    elif n == 2:
        cabecalho(42, 'Cadastro de Pessoas')
        validationName(arq)

    elif n == 3:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('Valor incorreto, digite uma opção válida!')
        cabecalho(42, 'Menu Principal')
        menu(['1 - Ver pessoas cadastradas', '2 - Cadastrar Nova Pessoa', '3 - Sair do Sistema'])

    cabecalho(42, 'Menu Principal')
    menu(['1 - Ver pessoas cadastradas', '2 - Cadastrar Nova Pessoa', '3 - Sair do Sistema'])
