from time import sleep
def contador():
    print('Contagem de 1 até 10 de 1 em 1')
    sleep(1)
    for x in range(1,11):
        print(x,end=' ')
        sleep(0.2)
    print('Fim!')
    print('Contagem de 10 até 1 de 2 em 2')
    sleep(1)
    for x in range(10, -1, -2):
        print(x,end=' ')
        sleep(0.2)
    print('Fim!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    num = 1
    if passo == 0:
        passo = 1
    elif inicio > fim and passo < 0:
        fim -= 1
    elif fim > inicio and passo > 0:
        fim += 1
    if inicio > fim and passo == 1:
        passo = -abs(passo)
        fim -= 1
    elif inicio > fim and passo > 0:
        passo = -abs(passo)
        num = -abs(num)
        fim += num
        print('test2', passo)
    if fim < 0 and passo > 0:
        passo = -abs(passo)
        num = -abs(num)
        fim += num
        print('test3', passo)
    if passo < 0:
        print(f'Contagem de {inicio} até {fim+1} de {abs(passo)} em {abs(passo)}')
    elif passo > 0:
        print(f'Contagem de {inicio} até {fim-1} de {passo} em {passo}')
    for x in range(inicio, fim, passo):
        print(x, end=' ')
        sleep(0.5)
    print('Fim!')


contador()
