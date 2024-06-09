n = 0
cont = 0
for x in range (1,7):
    inp=int(input('Digite um numero: '))
    cont += 1
    if inp % 2 == 0:
        n+=inp
print(n)
print(cont)
