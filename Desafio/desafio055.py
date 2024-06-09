pesado = 0
leve = 1000
for x in range(1,6):
    peso=int(input(f'Qual o peso da {x}! pessoa'))
    if peso > pesado:
        pesado = peso
    elif peso < leve:
        leve = peso
print(f'O mais magro pesa {leve}')
print(f'O mais gordo pesa {pesado}')

