import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.sifrao(p,'US$')} é R${moeda.sifrao(moeda.metade(p))}')
print(f'O dobro de {moeda.sifrao(p)} é R${moeda.sifrao(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.sifrao(moeda.aumentar(p,10))}')
print(f'Diminuindo 10%, temos R${moeda.sifrao(moeda.diminuir(p,10))}')