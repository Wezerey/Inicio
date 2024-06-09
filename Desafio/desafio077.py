produto =  ('Caderno', 'Caneta', 'Borracha', 'Lapiseira', 'Fichario', 'Charuto', 'Cigarrilha', 'Maconha')
vogais = ('a','e','i','o','u')
for i in range (0,len(produto)):
    print(f'Na palavra {produto[i]} temos',end=' ')
    for j in range (0,len(produto[i])):
        for k in range (0,len(vogais)):
            if produto[i][j] == vogais[k]:
                print(vogais[k], end=" ")
    print('')