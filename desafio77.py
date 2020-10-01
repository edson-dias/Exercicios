n = 'estudar', 'programar', 'linguagem', 'Juliane', 'trabalhando', 'para', 'Nutrimental'
for p in n:
    print(f'\nNa palava {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' {letra}', end='')

