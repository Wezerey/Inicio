def factorial(num=1,show=False):
    f=1
    print('--'*30)
    for c in range(num, 0, -1):
        f *= c
        print(f,'valor de c')
        if show:
            if c == 1:
                print(f'{c} = ',end='')
            else:
                print(f'{c} x ',end='')
    return f


valor = (int(input('Valor fatorial: ')))
print(factorial(valor,show=True))


def factorial(n):
    f = 1
    for c in range(1, n + 1):
        print(c)
        f *= c
        print(f'depois {f}')
    return f

