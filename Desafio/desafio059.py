x=0
print('*-*' * 20)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
print('*-*'*20)
while x != 5:
    ntot = 0
    print('''          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos numeros
          [5] Sair do programa''')
    print('*-*' * 20)
    x = int(input('>> Qual sua Opcao? '))
    if x == 1:
        ntot = n1 + n2
        print(f'{n1} + {n2} = {ntot}')
        print('*-*' * 20)
    elif x == 2:
        ntot = n1 * n2
        print(f'{n1} x {n2} = {ntot}')
        print('*-*' * 20)
    elif x == 3:
        if n1 > n2:
            print(f'O numero maior é o {n1}')
            print('*-*' * 20)
        elif n1 == n2:
            print(f'Os numeros Sao iguais')
            print('*-*' * 20)
        else:
            print(f'O numero maior é o {n2}')
            print('*-*' * 20)
    elif x == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
        print('*-*' * 20)
print('Programa encerrado!')