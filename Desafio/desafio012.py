prc=float(input('Qual o preco do item? R$ '))
print('O produto que custava R${}, na promoçao de 5% de desconto o produto saira com o preco de R${:.2f}'.format(prc,(prc-(prc*5)/100)))
print('OU')
novo= prc - (prc*5)/100
print('O produto que custava R${}, na promoçao de 5% de desconto o produto saira com o preco de R${:.2f}'.format(prc,novo))