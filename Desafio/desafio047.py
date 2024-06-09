from time import sleep
n = int(input('Digite um numero: '))
for c in range (1 , n+1):
    if c % 2 == 0:
        print(c,end=' ')
        sleep(1)
print("acabou")