import random
from operator import itemgetter
Jogadores = dict ()
Listajogadores = list ()
maior = 0
for x in range (4):
    Jogadores['nome']=str(input(''))
    Jogadores['numero'] = random.randint(1,6)
    Listajogadores.append(Jogadores.copy())
print('*'*20)
for x in range(4):
    print(f'O {Listajogadores[x]["nome"]} tirou {Listajogadores[x]["numero"]}')