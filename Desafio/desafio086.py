Matriz=[[],[],[],]
for x in range(3):
    for z in range(3):
        Matriz[x].append(int(input(f'Digite um valor para {x, z}')))
for c in range(3):
    print(Matriz[c])
