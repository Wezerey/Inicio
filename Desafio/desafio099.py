from time import sleep
def valor(*num):
    print('-='*30)
    maior = 0
    print('Analisando os valores passados...')
    for x in num:
        print(x,end=' ')
        sleep(.5)
        if x > maior:
            maior = x
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


valor(9,2,3,6,9)
valor(11,9,5,10)
valor(10,6,7,4,5,9)
valor(1,2,0)
valor()