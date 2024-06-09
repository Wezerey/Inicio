lanche = ('pizza','Hamburguer','suco', 'pudim','batata frita')
print('='*40)
for pos, comida in enumerate (lanche):
    print (comida,f'{pos}')
print('=' * 40)
for comida in lanche:
    print(comida)
print('='*40)
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
print('='*40)