num = [1,5,9,2]
num[2] = 89
num.append(77)
num.sort()
print(f'{'essa lista contem apend e sort':<35}',num)
num.insert(2,3)
print(f'{'essa lista contem insert':<35}',num)
num.pop(5)
print(f'{'essa lista contem pop':<35}',num)
print(f'{"tamanho da lista em leitura":37}',end='')
for x in range(0,len(num)):
    if x == len(num)-1:
        print(f'{x} ', end='')
    else:
        print(f'{x}, ',end='')
print(' ')
if 4 in num:
    num.remove(5)
else:
    print('Nao achei')