vol=int(input('Qual a velocidade?'))
if vol <= 80:
    print('Voce nao foi multado')
else:
    mul=(vol-80)*7.00
    print('Voce foi multado em R${:.2f}'.format(mul))