from datetime import date
maiorridade=0
menorridade=0
for x in range (0,7):
    nas=int(input('Qual o ano de nascimento?'))
    ano=date.today().year
    idade = ano - nas
    if idade >= 18:
        maiorridade += 1
    else:
        menorridade += 1
print(f'Ao todo tivemos {maiorridade} pessoas maiores de idade')
print(f'Ao todo tivemos {menorridade} pessoas menores de idade')