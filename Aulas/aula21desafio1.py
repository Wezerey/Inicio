def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: Nao vota'
    elif 16 >= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto Obrigadotio'


Nascimento = int(input('Nascimento: '))
print(voto(Nascimento))

