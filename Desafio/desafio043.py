peso = int(input('Qual seu peso (KG)? '))
h = float(input('Qual sua altura (CM)? '))
imc = peso / (h*h)
if imc <= 18.5:
    print('voce esta abaixo do peso')
elif imc <= 25:
    print('voce esta com o peso ideal')
elif imc <= 30:
    print('voce esta com o sobrepeso')
elif imc <= 40:
    print('voce esta com o obesidade')
else:
    print('voce esta com o obesidade morbida')

print(f"{imc:.1f}")