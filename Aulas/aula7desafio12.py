preco=float(input('Qual o preco do item:R$'))
porc=(preco*5)/100
pref=preco-porc
print('O item terá um desconto de 5%. O preco final é: R${}'.format(pref))
print(type(pref))
print(type(porc))
