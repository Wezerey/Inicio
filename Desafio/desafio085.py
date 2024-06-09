Numeros = [[],[]]
for c in range(6):
    n=int(input('Digite um numero'))
    if n % 2 == 0:
        Numeros[0].append(n)
    else:
        Numeros[1].append(n)
Numeros[1].sort()
Numeros[0].sort()
print(f'Os valores pares {Numeros[0]}')
print(f'Os valores impares {Numeros[1]}')