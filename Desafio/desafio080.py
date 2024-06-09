lista = list()
for x in range(5):
    n = int(input('Digite um numero:'))
    if x == 0:
        lista.append(n)
        print(lista)
    elif n > lista[len(lista)-1]:
        lista.append(n)
        print(lista)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(lista)
                break
            pos+=1
print(lista)