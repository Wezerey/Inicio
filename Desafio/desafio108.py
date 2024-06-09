from ex107 import moedas
p = float(input('Digite um valor: '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumatado 10%, temos {moedas.aumentar(p,10)}')
print(f'Reduzindo 13%, temos {moedas.deminuir(p,13)}')