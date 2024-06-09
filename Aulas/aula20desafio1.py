def area(larg, comp):
    total=larg*comp
    print(f'A soma de {larg}x{comp} é de {total}m².')


print('Controle de terrenos')
print('-'*20)
l=float(input('Largura (m)'))
c=float(input('Comprimento (m)'))
area(l,c)