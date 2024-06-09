from random import randint
t = 1
print('Sou seu computador...')
n = randint(0,10)
print('Acabei de pensar em um numero de 1 a 9. Sera que voce consegue acertar?')
print(n)
r = int(input('Qual o seu palpite? '))
while r != n:
    if r < n:
        print('Mais ... Tente mais uma vez.')
        r = int(input('Qual o seu palpite? '))
        t += 1
    elif r > 9:
        print('Tente um numero de 1 a 9 ... Tente mais uma vez.')
        r = int(input('Qual o seu palpite? '))
        t += 1
    else:
        print('Menos ... Tente mais uma vez.')
        r = int(input('Qual o seu palpite? '))
        t += 1
print(f'Voce acertou com {t} tentativas! parabens!')