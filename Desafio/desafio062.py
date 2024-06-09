pt = int(input('Primeiro termo: '))
rz = int(input('Razao: '))
x = rz
c = 10
total = pt
contador = 0
while c != 0:
    for cont in range(0,c):
        print(f'>>{total} ',end='')
        total = total + rz
        contador += 1
    print('PAUSA')
    c = int(input('Quer fazer mais quantos: '))
print(f'Ao total voce solicitou {contador} vezes')
