futebol = dict()
gols = list()
soma = 0
futebol['nome']=str(input('Nome:'))
futebol['partidas']=int(input(f'Quantas partidas {futebol['nome']} jogou? '))
for x in range(futebol['partidas']):
    gols.append(int(input(f'Quantos gols na partida {x+1}: ')))
futebol['gols']=gols[:]
futebol['total']=sum(gols)
print(futebol)
for k,v in futebol.items():
    print(f'O campo "{k}" tem o valor {v}')
print(f'O jogador {futebol['nome']} jogou {futebol['partidas']} partida')

for x in range(futebol['partidas']):
    print(f'    => Na partida {x + 1}, fez {futebol['gols'][x]} gols.')
print(f'foi um total de {soma} gols.')
