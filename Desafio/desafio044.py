produto = float(input('Qual o preco do produto: '))
fp = str(input('Qual a forma de pagamento? [ Dinheiro,Cartao ]')).lower()
vezes = 0
if fp == 'cartao':
    vezes = int(input('Quantas vezes ?'))
elif fp == 'dinheiro':
    produto = produto - ((produto*10)/100)
    print(f'Seu produto recebe 10% de desconto e o preco a ser pago é R${produto}')
if vezes == 1:
    produto = produto - ((produto*5)/100)
    print(f'Seu produto recebe 5% de desconto e o preco a ser pago é R${produto}')
elif vezes == 2:
    print(f'Seu produto nao tem desconto e o preco a ser pago é R${produto}')
elif vezes >= 3:
    produto = produto + ((produto*20)/100)
    print(f'Seu produto recebe juros do cartao e o preco a ser pago é R${produto}')
