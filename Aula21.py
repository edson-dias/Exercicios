# help(print)


# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela.
#     :param i: inicio da contagem.
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """


# para fazer documentação da função, basta usar 3 aspas duplas como o exemplo anterior

# help(contador)

# def somar(a, b=0, c=0):  Igualando o parâmetro a zero, ele se torna opcional dentro da função. Assim
# na chamada da função eu posso colocar menos argumentos. Ex: somar(2,4)

# global a - Declara a variavel a como global, mesmo se usada dentro de uma função

# return s - No uso de uma função com return, é necessário que esse return seja armazenado em algo
# exemplo: print(soma(2,3,4)) ou r = soma(2,5,8)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')