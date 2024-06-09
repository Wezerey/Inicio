preco=float(input('Preco das compras: '))
print('[1]a vista no dinhiro')
print('[2]a vista no cartao')
print('[3]2x no cartao')
print('[4]3x ou mais')
opcao=int(input('Qual das opcoes: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua ccompra sera parcelada em 2x de R${}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc=int(input('Quantas parcelas: '))
    print('Sua compra sera parcelada em {}x de R${:} com juros'.format(totalparc,total))
else:
    print('Opcao invalida')
print(f'Sua compra de R${preco} sera R${total}')