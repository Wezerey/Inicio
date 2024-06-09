def aumentar (preco = 0, taxa = 0, formato = False):
    res = preco + ( preco * taxa/100)
    return res if formato is False else sifrao(res)

def diminuir (preco = 0 , taxa = 0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else sifrao(res)


def dobro(preco = 0, formato = False):
    res = preco*2
    return res if formato is False else sifrao(res)

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if formato is False else sifrao(res)


def sifrao(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(num=0, porcA=0, porcB=0):
    print('-' * 31)
    print('        RESUMO DO VALOR')
    print('-' * 31)
    print(f'Preco analizado:\t{sifrao(num)}')
    print(f'Dobro do preco:\t\t{dobro(num,True)}')
    print(f'Metade do preço:\t{metade(num,True)}')
    print(f'{porcA}% de aumento:\t\t{aumentar(num, porcA,True)}')
    print(f'{porcB}% de Reducao:\t\t{diminuir(num, porcB,True)}')
    print('-' * 31)