def metade(num, format = True):
    if format:
        return moeda(num / 2)
    else:
        return num / 2


def dobro(num, format = True):
    if format:
        return moeda(num * 2)
    else:
        return num * 2

def aumentar(num, porc, format = True):
    res = num - ((num * porc) / 100)
    return res if format is False else moeda(res)
    # maneira 1 = guanabara

def deminuir(num, porc, format = True):
    if format:
        return moeda(num - ((num * porc) / 100))
    else:
        return num - ((num * porc) / 100)
    # maneira 2 = minha


def moeda(num):
    return f'R${num:.2f}'.replace('.',',')


def resumo(num=0, porcA=0, porcB=0):
    print('-' * 31)
    print('        RESUMO DO VALOR')
    print('-' * 31)
    lista = ['Preco analizado:','Dobro do preco:','Metade do preço:',f'{porcA}% de aumento:',f'{porcB}% de Reducao:']
    print(f'{lista[0]:22}{moeda(num)}')
    print(f'{lista[1]:22}{dobro(num)}')
    print(f'{lista[2]:22}{metade(num)}')
    print(f'{lista[3]:22}{aumentar(num, porcA)}')
    print(f'{lista[4]:22}{deminuir(num, porcB)}')
    print('-' * 31)


