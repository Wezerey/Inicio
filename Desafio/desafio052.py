cont=0
num = int(input('Digite um numero: '))
for c in range (1,num+1):
    if num % c == 0:
        cont += 1
        print(f"\033[;34m{c}", end=' ')
    else:
        print(f"\033[;31m{c}", end=' ')
print('')
if cont == 2:
    print('Este numero é primo')
else:
    print('Este numero nao é primo, pois foi dividido {} vezes'.format(cont))
