vel=float(input('Qual é a velocidade atual do carro? '))
if vel> 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80')
    mul = (vel - 80) * 7.00
    print('Voce foi multado em {:.2f}'.format(mul))
print('Tenha um bom dia')