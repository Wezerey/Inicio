pt = int(input('Primeiro termo: '))
rz = int(input('Razao: '))
for x in range(pt, rz*10, rz):
    print(x,end="-> ")
print('acabou')