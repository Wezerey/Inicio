cont3=0
cont9=0
posi = 0
n1 = int(input("Digite um numero "))
n2 = int(input("Digite um numero "))
n3 = int(input("Digite um numero "))
n4 = int(input("Digite um numero "))
tupla = (n1,n2,n3,n4)
print(f'Voce digitou {tupla}')
for c in range (0, 4):
    if tupla[c] == 9:
        cont9 += 1
    elif tupla[c] == 3:
        posi = tupla.index(3)+1
print(posi)
