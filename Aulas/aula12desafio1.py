from datetime import date
atual = date.today().year
data = int(input('Qual o ano de nacimento: '))
idade = atual - data
print(f'quem nasceu em {data} tem {idade} anos de idade em {atual}')
if idade == 18:
    print('Esta no ano de se alistar')
elif idade < 18:
    print(f'Falta {18-idade} anos para voce se alistar')
else:
    print(f'voce ja se alistou a {idade - 18} anos atras')