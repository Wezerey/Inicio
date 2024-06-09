viagem=int(input('Quantos KM de viagem? '))
if viagem <= 200:
    duz=viagem*0.50
    print('O preco da sua viagem é mais cara R${:.2f}'.format(duz))
else:
    duz=viagem * 0.45
    print('O preco da sua viagem é mais barata R${:.2f}'.format(duz))