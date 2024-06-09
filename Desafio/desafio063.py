J = 0
A = 1
x = int(input("Quantos termos quer mostrar??"))
print(f'>> {J} >> {A}',end=' >>')
while x - 2 > 0:
    fibo = A + J
    J = A
    A = fibo
    x -= 1
    print(f' {fibo}',end=' >>')
print('Pause')