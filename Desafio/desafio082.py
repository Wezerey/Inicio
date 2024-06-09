r = ''
c = 0
lista = list()
lista_impar = list()
lista_par = list()
while r != 'N':
    lista.append(int(input('Digite um numero:')))
    r = str(input('Deseja continuar?[s/n] ')).upper().strip()
for x in lista:
    if x%2 == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)
print(lista_par)
print(lista_impar)