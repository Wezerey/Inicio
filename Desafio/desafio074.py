import random
maior = 0
menor = 0
key = random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)
print('Os numero escolhidos sao: ',end='')
for c in range (0,5):
    if c == 0:
        maior = key[c]
        menor = key[c]
    if key[c] > maior:
        maior = key[c]
    if key[c] < menor:
        menor = key[c]
print(key)
print(f'Maior {maior}')
print(f'Menor {menor}')