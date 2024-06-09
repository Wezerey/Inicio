cont = 0
maior = 0
menor = 0
n2 = 0
r = 'S'
while r == 'S':
    cont += 1
    n = int(input('Digite um numero:'))
    if n == 0:
        cont -= 1
    elif cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    n2 += n
    r = str(input('Deseja continuar [S/N] ')).upper()
n3 = n2 / cont
print(f'o total de numeros digitados é {cont} e a media ente eles é {n3}')
print(f'[menor {menor}][maior {maior}]')