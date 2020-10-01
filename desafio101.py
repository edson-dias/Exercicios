def voto(birth):

    from datetime import date

    age = date.today().year - birth

    if age >= 65:
        return 'Opcional!'

    elif 18 <= age < 65:
        return 'Obrigatório!'

    else:
        return 'Negado!'



ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
