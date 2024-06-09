prc=float(input('Qual o valor do item? R$'))
avista=prc-(prc*10)/100
aprazo=prc+(prc*5)/100
print('O item que custa R${:.2f} a vista ele sai por R${} e a prazo sai por R${:.2f} '.format(prc,avista,aprazo))
