ano = int(input('Qual o ano de nascimento'))
idade = 2024 - ano
if idade <= 9:
    print('Atleta Mirim')
elif idade <= 14:
    print('Atleta Infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade == 20:
    print('Atleta Senhor')
else:
    print('Atleta Master')