s = count = 0

while True:
    n = int(input('Digite um valor: [Para parar digite 999] '))
    if n == 999:
        break
    s += n
    count += 1

print(f'Foram digitados {count} e a soma entre eles é: {s}')
