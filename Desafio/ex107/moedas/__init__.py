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

def resumo(num=0,porcA=0, porcB=0):
     print('-'*31)
     print('        RESUMO DO VALOR')
     print('-' * 31)
     print(f'Preco analizado:     {moeda(num)}')
     print(f'Dobro do preco:      {dobro(num)}')
     print(f'Metade do preço:     {metade(num)}')
     print(f'{porcA}% de aumento:      {aumentar(num,porcA)}')
     print(f'{porcB}% de Reducao:      {deminuir(num,porcB)}')
     print('-' * 31)


def leiaDinheiro(msg):
    valor = str(input(msg))
    while True:
        if valor.isnumeric():
            break
        else:
            print('Erro')
            valor = str(input(msg))
    return float(valor)
