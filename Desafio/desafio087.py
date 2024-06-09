matriz=[[],[],[],]
maior = n = n2 = 0
for x in range(3):
    for z in range(3):
        matriz[x].append(int(input(f'Digite um valor para {x, z}')))
print('*' * 30)
for c in range(3):
    print(matriz[c])
for l in matriz:
    n2 += l[2]
    for k in l:
        if k % 2 == 0:
            n += k
    maior=matriz[2][1]
for y in matriz[2]:
    if y > maior:
        maior = y
print('*'*30)
print('A soma do coluna 3 é ',n2)
print('A soma dos pares é ',n)
print('O maior numero na linha 3 é ',maior)