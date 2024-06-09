cont = cont2 = 0
n = int(input('Digite um numero '))
while n != 999:
    cont += 1
    cont2 += n
    n = int(input('Digite um numero '))
print(f'Ao todo voce digitou {cont} e a soma entre eles é {cont2}')