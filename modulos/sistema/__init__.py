from modulos.interface import cabecalho


def arquivoExiste(x):
    try:
        a = open(x, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(x):
    try:
        a = open(x, 'wt+')
        a.close()
    except:
        print('Houve um erro com a criação do arquivo!')
    else:
        print(f'Arquivo {x} criado com sucesso!')


def showDados(x):
    try:
        a = open(x, 'rt')
    except:
        print('Houve um erro com o arquivo!')
    else:
        cabecalho(42, 'Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def validationName(arq):
    while True:
        try:
            n = str(input('Nome: ')).strip()
            i = int(input('Idade: '))

        except (TypeError, ValueError):
            print('Erro! Digite um nome válido!')
            continue

        else:
            try:
                a = open(arq, 'at')
            except FileNotFoundError:
                print('Houve um erro na abertura do arquivo.')
            else:
                try:
                    a.write(f'{n}; {i}\n')
                except:
                    print('Houve um erro ao inserir os dados')
                else:
                    print('Dados registrados com sucesso!')
                    a.close()
            break


def validationNumber(msg=''):
    while True:
        try:
            n = int(input(msg))

        except (TypeError, ValueError):
            print('Erro: Digite um número válido!')
            continue

        else:
            return n
