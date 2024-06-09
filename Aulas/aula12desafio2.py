from datetime import date
atual = date.today().year
nascimento = int(input(('Ano de nascimento')))
idade = atual - nascimento
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