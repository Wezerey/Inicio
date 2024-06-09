from random import randint
computador=randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5 ')
print('-=-'*20)
jogador = int(input('em que numero pensei? '))
if jogador == computador:
    print('Voce acertou!')
else:
    print('Eu pensei no numero {} e nao no {}'.format(jogador,computador))