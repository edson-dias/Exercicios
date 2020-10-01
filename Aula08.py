import math # from math import sqrt, floor, outras funçoes.
num = int(input('Digite um número: '))
raiz = math.sqrt(num) # se usar o método from math... não precisa chamar math novamente, apenas a função.
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # função ceil arredonda o número para cima.


