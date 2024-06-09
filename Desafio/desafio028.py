import random
rand=random.randrange(5)
n=int(input('Em que numero estou pensando de 1 a 5? '))
if rand == n:
    print('Voce acertou!! {}'.format(rand))
else:
    print('Voce errou!! {}'.format(rand))