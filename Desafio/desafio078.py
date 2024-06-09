maior = menor = posN = posM = 0
lista = list ()
LM = list ()
LN = list ()
for x in range(0,3):
    lista.append(int(input('digite um valor: ')))
    if x == 0:
        menor = lista[0]
        maior = lista[0]
    else:
        if lista[x] > maior:
            maior = lista[x]
        elif lista[x] < menor:
            menor = lista[x]
for p,x in enumerate(lista):
    if x == maior:
        LM.append(p)
    elif x == menor:
        LN.append(p)
print(f'Maior {maior} Na posicao ',end='')
for x in range (0,len(LM)):
    print(f'{LM[x]}...',end='')
print('')
print(f'Menor {menor} Na posicao ',end='')
for x in range (0,len(LN)):
    print(f'{LN[x]}...',end='')
print('')
