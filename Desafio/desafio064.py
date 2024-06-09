cont = 0
cont2 = 0
verdadeiro = False
while verdadeiro == False:
    n = int(input('Digite um numero '))
    if n != 999:
        cont += 1
        cont2 += n
    else:
        verdadeiro = True
print(f'Ao todo voce digitou {cont} e a soma entre eles é {cont2}')