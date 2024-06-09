from time import sleep
def valor(*num):
    print('-='*30)
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(valor,end=' ')
        sleep(.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


valor(9,2,3,6,9)
valor(11,9,5,10)
valor(10,6,7,4,5,9)
valor(1,2,0)
valor()