from random import randint
from time import sleep
def valor():
    soma = 0
    sorteia = list()
    print('Sorteando 5 valores da lista ',end='')
    for x in range(5):
        numero=randint(1,10)
        print(numero,end=' ')
        sleep(.5)
        sorteia.append(numero)
    print('pronto')
    for x in sorteia:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {sorteia}, temos {soma}')

valor()