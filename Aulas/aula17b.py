valores = list()
valores.append(5)
valores.append(3)
valores.append(4)
for x in range(0,2):
    valores.append(int(input('Digite um valor')))
for c,v in enumerate(valores):
    print(f'Na posicao {c} esta o valor {v}')
print('final da lista')