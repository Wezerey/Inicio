clubes_brasileiros = ("Flamengo", "Internacional", "Juventude", "Bragantino", "Cruzeiro", "Fortaleza", "Athletico-PR", "Grêmio", "Vasco da Gama", "Bahia")
print('**'*20)
print(f'brasileirao os 5 primeiros: {clubes_brasileiros[0:5]}')
print('**'*20)
print(f'brasileirao os 5 primeiros: {clubes_brasileiros[6:10]}')
print('**'*20)
print(sorted(clubes_brasileiros))
print('**'*20)
for cont in range (0, len(clubes_brasileiros)):
    if clubes_brasileiros[cont] == 'Cruzeiro':
        print(f'{clubes_brasileiros[cont]} esta na posicao {cont} na lista')
