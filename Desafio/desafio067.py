cont = 0
while True:
    print('-'*30)
    n = int(input('Qual o valor da tabuada: '))
    print('-' * 30)
    if n <= 0:
        break
    while cont != 10:
        cont += 1
        tabuada = n * cont
        print(f'{n} x {cont} = {tabuada}')
    if cont == 10:
        cont = 0
print('Obrigado!')