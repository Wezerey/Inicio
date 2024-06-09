t1 = int(input('Qual o valor da lateral 1: '))
t2 = int(input('Qual o valor da lateral 2: '))
t3 = int(input('Qual o valor da lateral 3: '))
if t1 == t2 == t3:
    t = 'Equilatero'
elif t1 == t2 or t2 == t3 or t3 == t1:
    t = 'Isosceles'
else:
    t = 'Escaleno'
if t1 + t2 > t3:
    print(f'Temos um triangulo \033[30;47m {t} \033[m')
else:
    print('Nao temos um triangulo')