num = int(input('Digite um numero: '))
tote = num
print(f'{tote}!=',end=' ')
while num > 0:
        if num == tote:
            num -= 1
            tot = tote * num
        else:
            tot = tot * num
            num -= 1
        if num < num:
            print(f'{tote}',end='')
            print(' x ' if num > 0 else ' =', end='')
        if num == 0:
            print(f' {tote} {tot}')
print(tot)