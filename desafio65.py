flag = 1
soma = count = 0

while flag != 0:

    flag = int(input('Digite números inteiros! Para parar digite 0: '))

    if flag != 0:

        soma += flag
        count += 1

        if count == 1:
            maior = menor = flag

        if maior < flag:
            maior = flag

        if menor > flag:
            menor = flag

print('Foram digitados {} números, a media entre eles é {}, o maior número é {} e o menor {}'.format(count, soma / count, maior, menor))

#while resp in 'Ss':