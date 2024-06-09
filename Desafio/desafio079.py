r = ''
lista = list()

while r != 'N':
    lista.append(int(input('Digite um numero:')))
    for x in range(0,len(lista)):
        for j in range(x+1,len(lista)):
            if lista[x] == lista[j]:
                del lista[j]
                print('valor duplicado')
    r = str(input('Deseja continuar?[s/n] ')).upper().strip()
print(sorted(lista))
