m1 = float(input('Qual a Nota? '))
m2 = float(input('Qual a Nota? '))
m3 = (m1+m2)/2
if m3 <= 5.0:
    print(f'Reprovado {m3:.1f}')
elif m3 <= 6.9:
    print(f'Recuperacao {m3:.1f}')
else:
    print(f'Aprovado {m3:.1f}')