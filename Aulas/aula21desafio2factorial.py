def factorail(num=1,show=False):
    """

    :param num: O numero a ser calculado
    :param show: Opcional para mostrar a conta
    :return: O valor do Fatorial de um numero
    """
    f=1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *=c
    return f


print(factorail(5,show=True))
help(factorail)


def factorial(n):
    f = 1
    for x in range(1, n + 1):
        print(x)
        f *= x
        print(f'depois {f}')
    return f
