pt = int(input('Primeiro termo: '))
rz = int(input('Razao: '))
x = 10
total = pt
while x > 0:
    print(f'>> {total}')
    total= total+rz
    x -= 1
print('Acabou!')