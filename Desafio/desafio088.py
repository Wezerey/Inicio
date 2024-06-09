import random,time
JogosMega = []
Qtd_jogos = int(input('Quantos jogos voce quer ?'))
print("*"*30)
for x in range(Qtd_jogos):
    for num in range(6):
        JogosMega.append(random.randint(1, 60))

    for Primeiro_contador in range (6):
        for Segundo_contador in range (1,6):
            if Primeiro_contador != Segundo_contador:
                if JogosMega[Primeiro_contador] == JogosMega[Segundo_contador]:
                    JogosMega.remove(JogosMega[Primeiro_contador])
                    JogosMega.append(random.randint(1, 60))
                    Primeiro_contador = 0
                    Segundo_contador = 1

    JogosMega.sort()
    print(JogosMega)
    print('=*=')
    time.sleep(2)
    JogosMega.clear()
print("*"*30)