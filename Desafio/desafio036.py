casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salario? '))
anos = int(input('Por quantos anos voce quer pagar a casa? '))
trinta = (sal*30) / 100
parcela = casa / (anos*12)
if trinta >= parcela:
    print(f'Seu financiamento foi aprovado com uma parcela de {parcela:.2f} que sera paga por {anos}anos ({anos*12} meses)')
else:
    print(f'Infelizmente seu parcela exedeu o 30% do seu salario {trinta}, seu financiamento foi reprovado. O valor da parcela ficaria em {parcela:.2f}')