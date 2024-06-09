produto =  ('Caderno', 15.50, 'Caneta', 1.20, 'Borracha', 0.75, 'Lapiseira', 12.90, 'Fichario', 33.00, 'Charuto', 15.00, 'Cigarrilha', 90.15, 'Maconha', 250.00)
texto = 'LISTAGEM DE PREÇOS'
print(texto.center(50))
print(50*'-')
for i in range (0,16,2):
    print(f'{produto[i]:.<20}','R$',f'{produto[i+1]:>7}')
print(50*'-')