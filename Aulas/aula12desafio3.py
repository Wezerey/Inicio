t1 = int(input('Qual o valor da lateral 1: '))
t2 = int(input('Qual o valor da lateral 2: '))
t3 = int(input('Qual o valor da lateral 3: '))

if t1 + t2 > t3 and t3 + t2 > t1 and t1 + t3 > t2:
    print(f'Temos um triangulo ',end='')
    if t1 == t2 == t3:
       print('Equilatero')
    elif t1 == t2 or t2 == t3 or t3 == t1:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Nao temos um triangulo')
