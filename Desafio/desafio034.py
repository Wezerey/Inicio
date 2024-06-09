salario=float(input('Qual o salario?'))
if salario < 1250:
    salario=salario+((salario*15)/100)
    print('Seu salario novo é 15% mais alto: R${}'.format(salario))
else:
    salario = salario + ((salario * 10) / 100)
    print('Seu salario novo é 10% mais alto: R${}'.format(salario))