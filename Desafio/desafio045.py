import random
eu = str(input('Pedra, Papel, Tesoura? '))
pc = random.choice(['pedra','papel', 'tesoura'])
print(f'eu-{eu} x pc-{pc}')
if eu == pc:
    print('Empate!! vamos tentar novamente!')
elif eu == 'pedra' and pc == 'tesoura':
    print('Voce ganhou!!')
elif eu == 'tesoura' and pc == 'papel':
    print('Voce ganhou!!')
elif eu == 'papel' and pc == 'pedra':
    print('Voce ganhou!!')
elif pc == 'pedra' and eu == 'tesoura':
    print('Voce perdeu!!')
elif pc == 'tesoura' and eu == 'papel':
    print('Voce perdeu!!')
elif pc == 'papel' and eu == 'pedra':
    print('Voce perdeu!!')
else:
    print('jogada invalida')

