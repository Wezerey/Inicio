peso = int(input('Qual seu peso (KG)? '))
h = float(input('Qual sua altura (CM)? '))
imc = peso / (h**2)
if imc < 18.5:
    print(f'voce esta abaixo do peso - {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'voce esta com o peso ideal - {imc:.1f}')
elif 25 <= imc < 30:
    print(f'voce esta com o sobrepeso - {imc:.1f}')
elif 30 <= imc < 40:
    print(f'voce esta com o obesidade - {imc:.1f}')
elif imc >= 40:
    print(f'voce esta com o obesidade morbida - {imc:.1f}')
