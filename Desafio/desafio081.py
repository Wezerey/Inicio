r = resposta = ''
cont5 = 0
lista = list()
while r != 'N':
    lista.append(int(input('Digite um numero:')))
    r = str(input('Deseja continuar?[s/n] ')).upper().strip()
for x in range(0,len(lista)):
    if lista[x] == 5:
        cont5 += 1
    if cont5 >= 1:
        resposta = 'foi encontrado na lista'
    else:
        resposta = 'nao foi encontrado na lista'
lista.sort()
print(len(lista))
print(lista)
print(f'O numero 5 {resposta}')