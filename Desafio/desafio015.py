dia=int(input('Quantos do dia ficou com o carro? '))
km=float(input('Quantos KM rodou com o carro? '))
valor= dia*60 + km*0.15
print('O valor a ser pago é R${:.2f}'.format(valor))