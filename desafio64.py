flag = soma = count = 0

while flag != 999:
    flag = int(input('Digite números inteiros! Para parar digite 999: '))
    if flag != 999:
        soma += flag
        count += 1
print('Foram digitados {} números e a soma entre els é: {}'.format(count, soma))
